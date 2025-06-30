#!/usr/bin/env python3
"""
Real-Time Data Collection System for BWGA Nexus
Pulls live market data, economic indicators, and public information
"""

import os
import asyncio
import aiohttp
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import json
import time
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class MarketData:
    """Market data structure"""
    symbol: str
    price: float
    change: float
    change_percent: float
    volume: int
    market_cap: float
    pe_ratio: float
    dividend_yield: float
    timestamp: str

@dataclass
class EconomicIndicator:
    """Economic indicator data"""
    indicator: str
    value: float
    previous_value: float
    change: float
    change_percent: float
    date: str
    frequency: str
    source: str

@dataclass
class NewsData:
    """News and sentiment data"""
    title: str
    description: str
    url: str
    published_at: str
    source: str
    sentiment: str
    relevance_score: float

class RealTimeDataCollector:
    """Real-time data collection system"""
    
    def __init__(self):
        # API Keys (use environment variables for security)
        self.alpha_vantage_key = os.getenv('ALPHA_VANTAGE_API_KEY', 'demo')
        self.fred_api_key = os.getenv('FRED_API_KEY', 'demo')
        self.news_api_key = os.getenv('NEWS_API_KEY', 'demo')
        self.yahoo_finance_enabled = True
        
        # Data storage
        self.market_data_cache = {}
        self.economic_data_cache = {}
        self.news_cache = {}
        self.last_update = {}
        
        # Cache expiration (5 minutes)
        self.cache_expiry = 300
        
    async def get_market_data(self, symbols: List[str]) -> Dict[str, MarketData]:
        """Get real-time market data for multiple symbols"""
        current_time = time.time()
        
        # Check cache first
        if (current_time - self.last_update.get('market_data', 0)) < self.cache_expiry:
            return self.market_data_cache
        
        market_data = {}
        
        try:
            # Use Yahoo Finance for real-time data
            if self.yahoo_finance_enabled:
                import yfinance as yf
                
                for symbol in symbols:
                    try:
                        ticker = yf.Ticker(symbol)
                        info = ticker.info
                        
                        # Get current price
                        hist = ticker.history(period="2d")
                        if len(hist) >= 2:
                            current_price = hist['Close'].iloc[-1]
                            previous_price = hist['Close'].iloc[-2]
                            change = current_price - previous_price
                            change_percent = (change / previous_price) * 100
                        else:
                            current_price = info.get('currentPrice', 0)
                            change = 0
                            change_percent = 0
                        
                        market_data[symbol] = MarketData(
                            symbol=symbol,
                            price=current_price,
                            change=change,
                            change_percent=change_percent,
                            volume=info.get('volume', 0),
                            market_cap=info.get('marketCap', 0),
                            pe_ratio=info.get('trailingPE', 0),
                            dividend_yield=info.get('dividendYield', 0),
                            timestamp=datetime.now().isoformat()
                        )
                        
                    except Exception as e:
                        print(f"Error fetching data for {symbol}: {e}")
                        continue
            
            # Fallback to Alpha Vantage if Yahoo Finance fails
            if not market_data and self.alpha_vantage_key != 'demo':
                for symbol in symbols:
                    try:
                        url = f"https://www.alphavantage.co/query"
                        params = {
                            'function': 'GLOBAL_QUOTE',
                            'symbol': symbol,
                            'apikey': self.alpha_vantage_key
                        }
                        
                        response = requests.get(url, params=params)
                        data = response.json()
                        
                        if 'Global Quote' in data:
                            quote = data['Global Quote']
                            market_data[symbol] = MarketData(
                                symbol=symbol,
                                price=float(quote.get('05. price', 0)),
                                change=float(quote.get('09. change', 0)),
                                change_percent=float(quote.get('10. change percent', '0%').replace('%', '')),
                                volume=int(quote.get('06. volume', 0)),
                                market_cap=0,  # Alpha Vantage doesn't provide this
                                pe_ratio=0,
                                dividend_yield=0,
                                timestamp=datetime.now().isoformat()
                            )
                    except Exception as e:
                        print(f"Error fetching Alpha Vantage data for {symbol}: {e}")
                        continue
            
            # Update cache
            self.market_data_cache = market_data
            self.last_update['market_data'] = current_time
            
        except Exception as e:
            print(f"Error in market data collection: {e}")
        
        return market_data
    
    async def get_economic_indicators(self, indicators: List[str]) -> Dict[str, EconomicIndicator]:
        """Get economic indicators from FRED API"""
        current_time = time.time()
        
        # Check cache first
        if (current_time - self.last_update.get('economic_data', 0)) < self.cache_expiry:
            return self.economic_data_cache
        
        economic_data = {}
        
        try:
            if self.fred_api_key != 'demo':
                from fredapi import Fred
                fred = Fred(api_key=self.fred_api_key)
                
                for indicator in indicators:
                    try:
                        # Get latest data
                        series = fred.get_series(indicator, limit=2)
                        
                        if len(series) >= 2:
                            current_value = series.iloc[-1]
                            previous_value = series.iloc[-2]
                            change = current_value - previous_value
                            change_percent = (change / previous_value) * 100
                            
                            economic_data[indicator] = EconomicIndicator(
                                indicator=indicator,
                                value=current_value,
                                previous_value=previous_value,
                                change=change,
                                change_percent=change_percent,
                                date=series.index[-1].strftime('%Y-%m-%d'),
                                frequency='Monthly',
                                source='FRED'
                            )
                    except Exception as e:
                        print(f"Error fetching economic indicator {indicator}: {e}")
                        continue
            
            # Fallback to public data sources
            if not economic_data:
                economic_data = await self._get_public_economic_data(indicators)
            
            # Update cache
            self.economic_data_cache = economic_data
            self.last_update['economic_data'] = current_time
            
        except Exception as e:
            print(f"Error in economic data collection: {e}")
        
        return economic_data
    
    async def _get_public_economic_data(self, indicators: List[str]) -> Dict[str, EconomicIndicator]:
        """Get economic data from public sources"""
        economic_data = {}
        
        # Common economic indicators with public data
        public_indicators = {
            'GDP': {'url': 'https://api.worldbank.org/v2/country/US/indicator/NY.GDP.MKTP.CD?format=json&per_page=2'},
            'INFLATION': {'url': 'https://api.worldbank.org/v2/country/US/indicator/FP.CPI.TOTL.ZG?format=json&per_page=2'},
            'UNEMPLOYMENT': {'url': 'https://api.worldbank.org/v2/country/US/indicator/SL.UEM.TOTL.ZS?format=json&per_page=2'}
        }
        
        for indicator in indicators:
            if indicator in public_indicators:
                try:
                    response = requests.get(public_indicators[indicator]['url'])
                    data = response.json()
                    
                    if len(data) > 1 and len(data[1]) >= 2:
                        current_value = data[1][0]['value']
                        previous_value = data[1][1]['value']
                        change = current_value - previous_value
                        change_percent = (change / previous_value) * 100 if previous_value else 0
                        
                        economic_data[indicator] = EconomicIndicator(
                            indicator=indicator,
                            value=current_value,
                            previous_value=previous_value,
                            change=change,
                            change_percent=change_percent,
                            date=data[1][0]['date'],
                            frequency='Annual',
                            source='World Bank'
                        )
                except Exception as e:
                    print(f"Error fetching public economic data for {indicator}: {e}")
                    continue
        
        return economic_data
    
    async def get_news_and_sentiment(self, keywords: List[str], region: str = 'us') -> List[NewsData]:
        """Get news and sentiment analysis"""
        current_time = time.time()
        
        # Check cache first
        if (current_time - self.last_update.get('news', 0)) < self.cache_expiry:
            return self.news_cache
        
        news_data = []
        
        try:
            if self.news_api_key != 'demo':
                # Use NewsAPI for real-time news
                for keyword in keywords:
                    try:
                        url = "https://newsapi.org/v2/everything"
                        params = {
                            'q': keyword,
                            'language': 'en',
                            'sortBy': 'publishedAt',
                            'pageSize': 10,
                            'apiKey': self.news_api_key
                        }
                        
                        response = requests.get(url, params=params)
                        data = response.json()
                        
                        if 'articles' in data:
                            for article in data['articles'][:5]:  # Top 5 articles
                                # Simple sentiment analysis
                                sentiment = self._analyze_sentiment(article['title'] + ' ' + article['description'])
                                
                                news_data.append(NewsData(
                                    title=article['title'],
                                    description=article['description'],
                                    url=article['url'],
                                    published_at=article['publishedAt'],
                                    source=article['source']['name'],
                                    sentiment=sentiment,
                                    relevance_score=self._calculate_relevance(article, keyword)
                                ))
                    except Exception as e:
                        print(f"Error fetching news for {keyword}: {e}")
                        continue
            
            # Fallback to RSS feeds
            if not news_data:
                news_data = await self._get_rss_news(keywords)
            
            # Update cache
            self.news_cache = news_data
            self.last_update['news'] = current_time
            
        except Exception as e:
            print(f"Error in news collection: {e}")
        
        return news_data
    
    async def _get_rss_news(self, keywords: List[str]) -> List[NewsData]:
        """Get news from RSS feeds as fallback"""
        news_data = []
        
        # Popular RSS feeds
        rss_feeds = [
            'https://feeds.reuters.com/reuters/businessNews',
            'https://feeds.bbci.co.uk/news/business/rss.xml',
            'https://www.cnbc.com/id/100003114/device/rss/rss.html'
        ]
        
        try:
            import feedparser
            
            for feed_url in rss_feeds:
                try:
                    feed = feedparser.parse(feed_url)
                    
                    for entry in feed.entries[:10]:
                        # Check if article contains any keywords
                        content = entry.title + ' ' + entry.get('summary', '')
                        
                        for keyword in keywords:
                            if keyword.lower() in content.lower():
                                sentiment = self._analyze_sentiment(content)
                                
                                news_data.append(NewsData(
                                    title=entry.title,
                                    description=entry.get('summary', ''),
                                    url=entry.link,
                                    published_at=entry.get('published', datetime.now().isoformat()),
                                    source=feed.feed.get('title', 'RSS Feed'),
                                    sentiment=sentiment,
                                    relevance_score=self._calculate_relevance({'title': entry.title, 'description': entry.get('summary', '')}, keyword)
                                ))
                                break
                except Exception as e:
                    print(f"Error parsing RSS feed {feed_url}: {e}")
                    continue
        
        except ImportError:
            print("feedparser not available, skipping RSS feeds")
        
        return news_data
    
    def _analyze_sentiment(self, text: str) -> str:
        """Simple sentiment analysis"""
        positive_words = ['positive', 'growth', 'increase', 'profit', 'success', 'up', 'gain', 'bullish']
        negative_words = ['negative', 'decline', 'decrease', 'loss', 'failure', 'down', 'bearish', 'crash']
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'
    
    def _calculate_relevance(self, article: Dict, keyword: str) -> float:
        """Calculate relevance score for article"""
        title = article.get('title', '').lower()
        description = article.get('description', '').lower()
        keyword_lower = keyword.lower()
        
        title_score = title.count(keyword_lower) * 2
        desc_score = description.count(keyword_lower)
        
        return min(1.0, (title_score + desc_score) / 10)
    
    async def get_regional_data(self, city: str, country: str) -> Dict[str, Any]:
        """Get regional economic and demographic data"""
        regional_data = {}
        
        try:
            # Get population data
            population_data = await self._get_population_data(city, country)
            regional_data.update(population_data)
            
            # Get cost of living data
            cost_data = await self._get_cost_of_living_data(city, country)
            regional_data.update(cost_data)
            
            # Get infrastructure data
            infrastructure_data = await self._get_infrastructure_data(city, country)
            regional_data.update(infrastructure_data)
            
        except Exception as e:
            print(f"Error fetching regional data: {e}")
        
        return regional_data
    
    async def _get_population_data(self, city: str, country: str) -> Dict[str, Any]:
        """Get population and demographic data"""
        try:
            # Use World Bank API for population data
            url = f"https://api.worldbank.org/v2/country/{country}/indicator/SP.POP.TOTL?format=json&per_page=1"
            response = requests.get(url)
            data = response.json()
            
            if len(data) > 1 and data[1]:
                population = data[1][0]['value']
                return {
                    'population': population,
                    'population_density': population / 1000000,  # Rough estimate
                    'growth_rate': 0.01  # Default growth rate
                }
        except Exception as e:
            print(f"Error fetching population data: {e}")
        
        return {
            'population': 1000000,  # Default values
            'population_density': 100,
            'growth_rate': 0.01
        }
    
    async def _get_cost_of_living_data(self, city: str, country: str) -> Dict[str, Any]:
        """Get cost of living data"""
        # This would typically use a cost of living API
        # For now, return estimated values based on country
        cost_multipliers = {
            'USA': 1.0,
            'Canada': 0.9,
            'UK': 1.1,
            'Germany': 0.95,
            'Japan': 1.2,
            'Australia': 1.05
        }
        
        base_cost = cost_multipliers.get(country, 1.0)
        
        return {
            'cost_of_living': base_cost,
            'housing_cost': base_cost * 0.3,
            'transportation_cost': base_cost * 0.15,
            'food_cost': base_cost * 0.2
        }
    
    async def _get_infrastructure_data(self, city: str, country: str) -> Dict[str, Any]:
        """Get infrastructure data"""
        # This would typically use infrastructure APIs
        # For now, return estimated values
        return {
            'infrastructure_score': 0.8,
            'digital_infrastructure': 0.85,
            'transportation_score': 0.75,
            'utility_score': 0.9
        }
    
    async def get_comprehensive_data(self, symbols: List[str], indicators: List[str], 
                                   keywords: List[str], city: str, country: str) -> Dict[str, Any]:
        """Get all real-time data in one call"""
        tasks = [
            self.get_market_data(symbols),
            self.get_economic_indicators(indicators),
            self.get_news_and_sentiment(keywords),
            self.get_regional_data(city, country)
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        return {
            'market_data': results[0] if not isinstance(results[0], Exception) else {},
            'economic_data': results[1] if not isinstance(results[1], Exception) else {},
            'news_data': results[2] if not isinstance(results[2], Exception) else [],
            'regional_data': results[3] if not isinstance(results[3], Exception) else {},
            'timestamp': datetime.now().isoformat()
        }

# Global instance
data_collector = RealTimeDataCollector()

# Example usage
async def main():
    """Example of how to use the real-time data collector"""
    collector = RealTimeDataCollector()
    
    # Get comprehensive data
    data = await collector.get_comprehensive_data(
        symbols=['AAPL', 'GOOGL', 'MSFT'],
        indicators=['GDP', 'INFLATION', 'UNEMPLOYMENT'],
        keywords=['investment', 'economy', 'technology'],
        city='Austin',
        country='USA'
    )
    
    print("Real-time data collected:")
    print(json.dumps(data, indent=2, default=str))

if __name__ == "__main__":
    asyncio.run(main()) 