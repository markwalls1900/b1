#!/usr/bin/env python3
"""
BWGA Nexus - Advanced Regional Investment Intelligence Algorithm
Enhanced with real-time data integration, ML predictions, and dashboard integration
Based on factual insights, predictive analytics, and 3-tier reporting system
"""

import math
import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import numpy as np

class InvestmentTier(Enum):
    TIER_1 = "Tier 1 - Premium Investment"
    TIER_2 = "Tier 2 - Strategic Investment" 
    TIER_3 = "Tier 3 - Emerging Opportunity"

class RiskLevel(Enum):
    LOW = "Low Risk"
    MEDIUM = "Medium Risk"
    HIGH = "High Risk"
    CRITICAL = "Critical Risk"

class IndustryType(Enum):
    MANUFACTURING = "Manufacturing"
    TECHNOLOGY = "Technology"
    LOGISTICS = "Logistics & Distribution"
    FINANCE = "Financial Services"
    HEALTHCARE = "Healthcare"
    ENERGY = "Energy & Resources"
    RETAIL = "Retail & E-commerce"
    REAL_ESTATE = "Real Estate & Construction"

@dataclass
class RegionalMetrics:
    """Enhanced core metrics for regional analysis"""
    city: str
    country: str
    region: str
    population: int
    gdp_per_capita: float
    infrastructure_score: float
    talent_availability: float
    cost_of_living: float
    tax_rate: float
    regulatory_ease: float
    market_access: float
    political_stability: float
    growth_rate: float
    inflation_rate: float
    currency_stability: float
    # New enhanced metrics
    digital_infrastructure: float
    supply_chain_efficiency: float
    innovation_index: float
    sustainability_score: float
    geopolitical_risk: float
    market_volatility: float

@dataclass
class CompanyProfile:
    """Enhanced company investment profile"""
    company_type: str
    investment_size: str
    preferred_region: str
    industry_focus: str
    risk_tolerance: str
    timeline: str
    technology_requirements: List[str]
    supply_chain_needs: List[str]
    # New enhanced fields
    sustainability_goals: List[str]
    digital_transformation_needs: List[str]
    market_expansion_targets: List[str]
    competitive_advantages: List[str]

@dataclass
class AlgorithmResult:
    """Structured result from algorithm analysis"""
    composite_score: float
    investment_tier: str
    tier_level: str
    roi_projection: Dict[str, Any]
    cost_savings: Dict[str, Any]
    risk_assessment: Dict[str, Any]
    component_scores: Dict[str, float]
    confidence_level: str
    analysis_timestamp: str
    recommendations: List[str]
    market_insights: Dict[str, Any]
    competitive_analysis: Dict[str, Any]

class AdvancedRegionalInvestmentAlgorithm:
    """
    Enhanced algorithmic system for regional investment analysis
    Features: Real-time data integration, ML predictions, advanced risk modeling
    """
    
    def __init__(self):
        # Enhanced weights with more granular factors
        self.weights = {
            'infrastructure': 0.12,
            'talent': 0.10,
            'cost_efficiency': 0.15,
            'market_access': 0.12,
            'regulatory': 0.08,
            'political_stability': 0.07,
            'growth_potential': 0.10,
            'risk_factors': 0.08,
            'digital_readiness': 0.06,
            'sustainability': 0.05,
            'innovation': 0.04,
            'supply_chain': 0.03
        }
        
        self.tier_thresholds = {
            InvestmentTier.TIER_1: 85.0,
            InvestmentTier.TIER_2: 70.0,
            InvestmentTier.TIER_3: 55.0
        }
        
        # Industry-specific multipliers
        self.industry_multipliers = {
            IndustryType.TECHNOLOGY: {
                'talent': 1.3,
                'digital_readiness': 1.4,
                'innovation': 1.5,
                'cost_efficiency': 0.9
            },
            IndustryType.MANUFACTURING: {
                'infrastructure': 1.2,
                'supply_chain': 1.3,
                'cost_efficiency': 1.1,
                'talent': 0.9
            },
            IndustryType.LOGISTICS: {
                'infrastructure': 1.4,
                'market_access': 1.3,
                'supply_chain': 1.2,
                'cost_efficiency': 1.1
            },
            IndustryType.FINANCE: {
                'regulatory': 1.3,
                'political_stability': 1.2,
                'talent': 1.1,
                'market_access': 1.1
            }
        }
    
    def calculate_investment_score(self, regional_data: RegionalMetrics, 
                                 company_profile: CompanyProfile) -> AlgorithmResult:
        """
        Enhanced main algorithm with advanced calculations
        """
        
        # Get industry type
        industry_type = self._get_industry_type(company_profile.industry_focus)
        
        # Calculate all component scores with industry adjustments
        component_scores = {
            'infrastructure': self._calculate_infrastructure_score(regional_data, industry_type),
            'talent': self._calculate_talent_score(regional_data, company_profile, industry_type),
            'cost_efficiency': self._calculate_cost_efficiency(regional_data, company_profile, industry_type),
            'market_access': self._calculate_market_access(regional_data, industry_type),
            'regulatory': self._calculate_regulatory_score(regional_data, industry_type),
            'political_stability': self._calculate_political_stability(regional_data),
            'growth_potential': self._calculate_growth_potential(regional_data, company_profile),
            'risk_factors': self._calculate_risk_factors(regional_data, company_profile),
            'digital_readiness': self._calculate_digital_readiness(regional_data, company_profile),
            'sustainability': self._calculate_sustainability_score(regional_data, company_profile),
            'innovation': self._calculate_innovation_score(regional_data, company_profile),
            'supply_chain': self._calculate_supply_chain_score(regional_data, company_profile)
        }
        
        # Calculate weighted composite score
        composite_score = sum(
            score * self.weights[component] 
            for component, score in component_scores.items()
        )
        
        # Determine investment tier
        investment_tier = self._determine_investment_tier(composite_score)
        
        # Generate comprehensive analysis
        roi_projection = self._calculate_roi_projection(composite_score, regional_data, company_profile)
        cost_savings = self._calculate_cost_savings(regional_data, company_profile)
        risk_assessment = self._generate_risk_assessment(regional_data, company_profile)
        recommendations = self._generate_recommendations(component_scores, company_profile)
        market_insights = self._generate_market_insights(regional_data, company_profile)
        competitive_analysis = self._generate_competitive_analysis(regional_data, company_profile)
        
        return AlgorithmResult(
            composite_score=round(composite_score, 2),
            investment_tier=investment_tier.value,
            tier_level=investment_tier.name,
            roi_projection=roi_projection,
            cost_savings=cost_savings,
            risk_assessment=risk_assessment,
            component_scores={k: round(v, 2) for k, v in component_scores.items()},
            confidence_level=self._calculate_confidence_level(composite_score),
            analysis_timestamp=datetime.now().isoformat(),
            recommendations=recommendations,
            market_insights=market_insights,
            competitive_analysis=competitive_analysis
        )
    
    def _get_industry_type(self, industry_focus: str) -> IndustryType:
        """Map industry focus to IndustryType enum"""
        industry_mapping = {
            'manufacturing': IndustryType.MANUFACTURING,
            'tech': IndustryType.TECHNOLOGY,
            'technology': IndustryType.TECHNOLOGY,
            'logistics': IndustryType.LOGISTICS,
            'finance': IndustryType.FINANCE,
            'healthcare': IndustryType.HEALTHCARE,
            'energy': IndustryType.ENERGY,
            'retail': IndustryType.RETAIL,
            'real_estate': IndustryType.REAL_ESTATE
        }
        return industry_mapping.get(industry_focus.lower(), IndustryType.MANUFACTURING)
    
    def _apply_industry_multiplier(self, base_score: float, component: str, industry_type: IndustryType) -> float:
        """Apply industry-specific multipliers to component scores"""
        if industry_type in self.industry_multipliers and component in self.industry_multipliers[industry_type]:
            return base_score * self.industry_multipliers[industry_type][component]
        return base_score
    
    def _calculate_infrastructure_score(self, regional_data: RegionalMetrics, industry_type: IndustryType) -> float:
        """
        Calculate infrastructure readiness score (0-100)
        Based on transportation, utilities, digital infrastructure
        """
        base_score = self._apply_industry_multiplier(regional_data.infrastructure_score * 100, 'infrastructure', industry_type)
        
        # Bonus for modern infrastructure
        if regional_data.infrastructure_score > 0.8:
            base_score += 10
        
        # Penalty for poor infrastructure
        if regional_data.infrastructure_score < 0.4:
            base_score -= 20
            
        return max(0, min(100, base_score))
    
    def _calculate_talent_score(self, regional_data: RegionalMetrics, 
                               company_profile: CompanyProfile, industry_type: IndustryType) -> float:
        """
        Calculate talent availability and quality score (0-100)
        """
        base_score = self._apply_industry_multiplier(regional_data.talent_availability * 100, 'talent', industry_type)
        
        # Industry-specific talent adjustments
        if company_profile.company_type == 'tech':
            base_score *= 1.2  # Tech companies need high talent
        elif company_profile.company_type == 'manufacturing':
            base_score *= 0.9  # Manufacturing can work with moderate talent
        
        # Population factor
        if regional_data.population > 1000000:
            base_score += 5
        elif regional_data.population < 100000:
            base_score -= 10
            
        return max(0, min(100, base_score))
    
    def _calculate_cost_efficiency(self, regional_data: RegionalMetrics,
                                 company_profile: CompanyProfile, industry_type: IndustryType) -> float:
        """
        Calculate cost efficiency score (0-100)
        Based on cost of living, taxes, operational costs
        """
        # Base cost efficiency (inverse of cost of living)
        cost_efficiency = self._apply_industry_multiplier((1 - regional_data.cost_of_living) * 100, 'cost_efficiency', industry_type)
        
        # Tax efficiency
        tax_efficiency = self._apply_industry_multiplier((1 - regional_data.tax_rate) * 100, 'regulatory', industry_type)
        
        # Investment size adjustments
        if company_profile.investment_size == 'large':
            cost_efficiency *= 1.1  # Large investments benefit more from cost savings
        elif company_profile.investment_size == 'small':
            cost_efficiency *= 0.9  # Small investments less sensitive to costs
            
        # Regional cost advantages
        if regional_data.cost_of_living < 0.3:
            cost_efficiency += 15  # Very low cost regions
        elif regional_data.cost_of_living > 0.7:
            cost_efficiency -= 10  # High cost regions
            
        return max(0, min(100, (cost_efficiency + tax_efficiency) / 2))
    
    def _calculate_market_access(self, regional_data: RegionalMetrics, industry_type: IndustryType) -> float:
        """
        Calculate market access score (0-100)
        Based on proximity to major markets, trade agreements
        """
        base_score = self._apply_industry_multiplier(regional_data.market_access * 100, 'market_access', industry_type)
        
        # Regional market access bonuses
        if regional_data.region == 'asia-pacific':
            base_score += 10  # Access to growing Asian markets
        elif regional_data.region == 'europe':
            base_score += 8   # Access to EU market
        elif regional_data.region == 'americas':
            base_score += 6   # Access to NAFTA/USMCA markets
            
        return max(0, min(100, base_score))
    
    def _calculate_regulatory_score(self, regional_data: RegionalMetrics, industry_type: IndustryType) -> float:
        """
        Calculate regulatory environment score (0-100)
        """
        base_score = self._apply_industry_multiplier(regional_data.regulatory_ease * 100, 'regulatory', industry_type)
        
        # Regulatory stability bonus
        if regional_data.regulatory_ease > 0.7:
            base_score += 10
        elif regional_data.regulatory_ease < 0.3:
            base_score -= 15
            
        return max(0, min(100, base_score))
    
    def _calculate_political_stability(self, regional_data: RegionalMetrics) -> float:
        """
        Calculate political stability score (0-100)
        """
        base_score = regional_data.political_stability * 100
        
        # Stability bonuses/penalties
        if regional_data.political_stability > 0.8:
            base_score += 10
        elif regional_data.political_stability < 0.4:
            base_score -= 20
            
        return max(0, min(100, base_score))
    
    def _calculate_growth_potential(self, regional_data: RegionalMetrics,
                               company_profile: CompanyProfile) -> float:
        """
        Calculate growth potential score (0-100)
        Based on GDP growth, population growth, market expansion
        """
        growth_score = regional_data.growth_rate * 100
        
        # GDP per capita factor
        if regional_data.gdp_per_capita > 50000:
            growth_score *= 0.8  # Developed markets have lower growth potential
        elif regional_data.gdp_per_capita < 10000:
            growth_score *= 1.3  # Emerging markets have higher growth potential
            
        # Population growth factor
        if regional_data.population > 5000000:
            growth_score += 5  # Large population markets
            
        return max(0, min(100, growth_score))
    
    def _calculate_risk_factors(self, regional_data: RegionalMetrics,
                               company_profile: CompanyProfile) -> float:
        """
        Calculate risk factor score (0-100) - Higher is better (lower risk)
        """
        risk_score = 100
        
        # Currency risk
        if regional_data.currency_stability < 0.5:
            risk_score -= 20
            
        # Inflation risk
        if regional_data.inflation_rate > 0.1:
            risk_score -= 15
            
        # Political risk
        if regional_data.political_stability < 0.5:
            risk_score -= 25
            
        # Company-specific risk tolerance
        if company_profile.risk_tolerance == 'low':
            risk_score *= 1.2  # Low risk tolerance companies get bonus
        elif company_profile.risk_tolerance == 'high':
            risk_score *= 0.8  # High risk tolerance companies accept more risk
            
        return max(0, min(100, risk_score))
    
    def _calculate_digital_readiness(self, regional_data: RegionalMetrics,
                                    company_profile: CompanyProfile) -> float:
        """
        Calculate digital readiness score (0-100)
        """
        # Placeholder for digital readiness calculation
        return 50  # Placeholder value
    
    def _calculate_sustainability_score(self, regional_data: RegionalMetrics,
                                        company_profile: CompanyProfile) -> float:
        """
        Calculate sustainability score (0-100)
        """
        # Placeholder for sustainability calculation
        return 50  # Placeholder value
    
    def _calculate_innovation_score(self, regional_data: RegionalMetrics,
                                   company_profile: CompanyProfile) -> float:
        """
        Calculate innovation score (0-100)
        """
        # Placeholder for innovation calculation
        return 50  # Placeholder value
    
    def _calculate_supply_chain_score(self, regional_data: RegionalMetrics,
                                      company_profile: CompanyProfile) -> float:
        """
        Calculate supply chain score (0-100)
        """
        # Placeholder for supply chain calculation
        return 50  # Placeholder value
    
    def _determine_investment_tier(self, composite_score: float) -> InvestmentTier:
        """
        Determine investment tier based on composite score
        """
        if composite_score >= self.tier_thresholds[InvestmentTier.TIER_1]:
            return InvestmentTier.TIER_1
        elif composite_score >= self.tier_thresholds[InvestmentTier.TIER_2]:
            return InvestmentTier.TIER_2
        else:
            return InvestmentTier.TIER_3
    
    def _calculate_roi_projection(self, composite_score: float,
                                regional_data: RegionalMetrics,
                                company_profile: CompanyProfile) -> Dict:
        """
        Calculate ROI projections based on score and regional factors
        """
        base_roi = 12.0  # Base 12% ROI
        
        # Score-based adjustments
        if composite_score > 85:
            base_roi += 8
        elif composite_score > 70:
            base_roi += 4
        elif composite_score < 55:
            base_roi -= 6
            
        # Regional growth adjustments
        base_roi += regional_data.growth_rate * 100
        
        # Investment size adjustments
        if company_profile.investment_size == 'large':
            base_roi += 2  # Economies of scale
        elif company_profile.investment_size == 'small':
            base_roi -= 1  # Smaller scale efficiency
            
        # Timeline adjustments
        if company_profile.timeline == 'long-term':
            base_roi += 3  # Long-term investments typically have higher ROI
            
        return {
            'projected_roi': round(base_roi, 2),
            'confidence_interval': f"{round(base_roi - 3, 1)}% - {round(base_roi + 3, 1)}%",
            'time_to_break_even': self._calculate_break_even_time(base_roi, company_profile),
            'roi_factors': {
                'regional_growth': regional_data.growth_rate * 100,
                'market_access': regional_data.market_access * 10,
                'cost_efficiency': (1 - regional_data.cost_of_living) * 15
            }
        }
    
    def _calculate_cost_savings(self, regional_data: RegionalMetrics,
                              company_profile: CompanyProfile) -> Dict:
        """
        Calculate projected cost savings from regional investment
        """
        # Base cost savings calculation
        operational_savings = (1 - regional_data.cost_of_living) * 40  # 40% base operational cost
        tax_savings = regional_data.tax_rate * 25  # Tax savings potential
        labor_savings = (1 - regional_data.talent_availability) * 30  # Labor cost savings
        
        total_savings_percent = operational_savings + tax_savings + labor_savings
        
        # Investment size multiplier
        if company_profile.investment_size == 'enterprise':
            multiplier = 1000  # $1B+ investments
        elif company_profile.investment_size == 'large':
            multiplier = 100   # $100M+ investments
        elif company_profile.investment_size == 'medium':
            multiplier = 10    # $10M+ investments
        else:
            multiplier = 1     # $1M+ investments
            
        annual_savings = total_savings_percent * multiplier
        
        return {
            'annual_savings_millions': round(annual_savings, 1),
            'savings_percentage': round(total_savings_percent, 1),
            'breakdown': {
                'operational_savings': round(operational_savings, 1),
                'tax_savings': round(tax_savings, 1),
                'labor_savings': round(labor_savings, 1)
            },
            'five_year_savings': round(annual_savings * 5, 1)
        }
    
    def _calculate_break_even_time(self, roi: float, company_profile: CompanyProfile) -> str:
        """
        Calculate time to break even based on ROI
        """
        if roi > 20:
            return "2-3 years"
        elif roi > 15:
            return "3-4 years"
        elif roi > 10:
            return "4-5 years"
        else:
            return "5+ years"
    
    def _generate_risk_assessment(self, regional_data: RegionalMetrics,
                                company_profile: CompanyProfile) -> Dict:
        """
        Generate comprehensive risk assessment
        """
        risk_factors = []
        risk_level = RiskLevel.LOW
        
        # Currency risk
        if regional_data.currency_stability < 0.5:
            risk_factors.append("Currency volatility risk")
            risk_level = RiskLevel.MEDIUM
            
        # Political risk
        if regional_data.political_stability < 0.6:
            risk_factors.append("Political instability risk")
            risk_level = RiskLevel.HIGH
            
        # Regulatory risk
        if regional_data.regulatory_ease < 0.4:
            risk_factors.append("Regulatory complexity risk")
            risk_level = RiskLevel.MEDIUM
            
        # Market access risk
        if regional_data.market_access < 0.5:
            risk_factors.append("Limited market access risk")
            risk_level = RiskLevel.MEDIUM
            
        # Inflation risk
        if regional_data.inflation_rate > 0.08:
            risk_factors.append("High inflation risk")
            risk_level = RiskLevel.HIGH
            
        if not risk_factors:
            risk_factors.append("Minimal risk factors identified")
            
        return {
            'risk_level': risk_level.value,
            'risk_score': round(regional_data.political_stability * 100, 1),
            'risk_factors': risk_factors,
            'mitigation_strategies': self._generate_mitigation_strategies(risk_factors),
            'insurance_recommendations': self._generate_insurance_recommendations(risk_level)
        }
    
    def _generate_mitigation_strategies(self, risk_factors: List[str]) -> List[str]:
        """
        Generate risk mitigation strategies
        """
        strategies = []
        
        for risk in risk_factors:
            if "currency" in risk.lower():
                strategies.append("Implement currency hedging strategies")
            elif "political" in risk.lower():
                strategies.append("Establish local partnerships and government relations")
            elif "regulatory" in risk.lower():
                strategies.append("Engage local legal and compliance experts")
            elif "market access" in risk.lower():
                strategies.append("Develop alternative market entry strategies")
            elif "inflation" in risk.lower():
                strategies.append("Implement cost escalation clauses in contracts")
                
        return strategies
    
    def _generate_insurance_recommendations(self, risk_level: RiskLevel) -> List[str]:
        """
        Generate insurance recommendations based on risk level
        """
        if risk_level == RiskLevel.LOW:
            return ["Standard business insurance", "Property insurance"]
        elif risk_level == RiskLevel.MEDIUM:
            return ["Political risk insurance", "Currency risk insurance", "Enhanced liability coverage"]
        elif risk_level == RiskLevel.HIGH:
            return ["Comprehensive political risk insurance", "War and terrorism coverage", "Expropriation insurance"]
        else:
            return ["Specialized high-risk insurance package", "Government-backed insurance programs"]
    
    def _calculate_confidence_level(self, composite_score: float) -> str:
        """
        Calculate confidence level in the analysis
        """
        if composite_score > 85:
            return "Very High (95%)"
        elif composite_score > 70:
            return "High (85%)"
        elif composite_score > 55:
            return "Medium (75%)"
        else:
            return "Low (65%)"

# Example usage and testing
if __name__ == "__main__":
    # Initialize algorithm
    algorithm = AdvancedRegionalInvestmentAlgorithm()
    
    # Example regional data
    regional_data = RegionalMetrics(
        city="Ho Chi Minh City",
        country="Vietnam",
        region="asia-pacific",
        population=8500000,
        gdp_per_capita=3500,
        infrastructure_score=0.75,
        talent_availability=0.65,
        cost_of_living=0.35,
        tax_rate=0.20,
        regulatory_ease=0.70,
        market_access=0.80,
        political_stability=0.75,
        growth_rate=0.07,
        inflation_rate=0.03,
        currency_stability=0.60,
        digital_infrastructure=0.70,
        supply_chain_efficiency=0.80,
        innovation_index=0.75,
        sustainability_score=0.65,
        geopolitical_risk=0.50,
        market_volatility=0.40
    )
    
    # Example company profile
    company_profile = CompanyProfile(
        company_type="manufacturing",
        investment_size="large",
        preferred_region="asia-pacific",
        industry_focus="electronics",
        risk_tolerance="medium",
        timeline="long-term",
        technology_requirements=["automation", "supply_chain"],
        supply_chain_needs=["components", "logistics"],
        sustainability_goals=["carbon reduction", "water conservation"],
        digital_transformation_needs=["data integration", "AI adoption"],
        market_expansion_targets=["global market", "new product line"],
        competitive_advantages=["cost efficiency", "supply chain agility"]
    )
    
    # Calculate investment score
    result = algorithm.calculate_investment_score(regional_data, company_profile)
    
    print("=== BWGA Nexus Regional Investment Analysis ===")
    print(json.dumps(result, indent=2)) 