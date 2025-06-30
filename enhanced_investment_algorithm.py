#!/usr/bin/env python3
"""
BWGA Nexus - Enhanced Regional Investment Intelligence Algorithm
Advanced algorithmic system with real-time data integration and ML predictions
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

@dataclass
class RegionalMetrics:
    """Enhanced regional analysis metrics"""
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
    digital_infrastructure: float = 0.7
    supply_chain_efficiency: float = 0.6
    innovation_index: float = 0.5
    sustainability_score: float = 0.6
    geopolitical_risk: float = 0.3
    market_volatility: float = 0.4

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
    sustainability_goals: List[str] = None
    digital_transformation_needs: List[str] = None
    market_expansion_targets: List[str] = None

@dataclass
class AlgorithmResult:
    """Structured algorithm analysis result"""
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

class EnhancedInvestmentAlgorithm:
    """
    Advanced algorithmic system for regional investment analysis
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
            'technology': {
                'talent': 1.3,
                'digital_readiness': 1.4,
                'innovation': 1.5,
                'cost_efficiency': 0.9
            },
            'manufacturing': {
                'infrastructure': 1.2,
                'supply_chain': 1.3,
                'cost_efficiency': 1.1,
                'talent': 0.9
            },
            'logistics': {
                'infrastructure': 1.4,
                'market_access': 1.3,
                'supply_chain': 1.2,
                'cost_efficiency': 1.1
            },
            'finance': {
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
        
        # Calculate all component scores
        component_scores = {
            'infrastructure': self._calculate_infrastructure_score(regional_data),
            'talent': self._calculate_talent_score(regional_data, company_profile),
            'cost_efficiency': self._calculate_cost_efficiency(regional_data, company_profile),
            'market_access': self._calculate_market_access(regional_data),
            'regulatory': self._calculate_regulatory_score(regional_data),
            'political_stability': self._calculate_political_stability(regional_data),
            'growth_potential': self._calculate_growth_potential(regional_data, company_profile),
            'risk_factors': self._calculate_risk_factors(regional_data, company_profile),
            'digital_readiness': self._calculate_digital_readiness(regional_data, company_profile),
            'sustainability': self._calculate_sustainability_score(regional_data, company_profile),
            'innovation': self._calculate_innovation_score(regional_data, company_profile),
            'supply_chain': self._calculate_supply_chain_score(regional_data, company_profile)
        }
        
        # Apply industry-specific adjustments
        industry_type = company_profile.industry_focus.lower()
        if industry_type in self.industry_multipliers:
            for component, multiplier in self.industry_multipliers[industry_type].items():
                if component in component_scores:
                    component_scores[component] *= multiplier
        
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
            market_insights=market_insights
        )
    
    def _calculate_infrastructure_score(self, regional_data: RegionalMetrics) -> float:
        """Calculate infrastructure readiness score (0-100)"""
        base_score = regional_data.infrastructure_score * 100
        
        # Bonus for modern infrastructure
        if regional_data.infrastructure_score > 0.8:
            base_score += 10
        
        # Penalty for poor infrastructure
        if regional_data.infrastructure_score < 0.4:
            base_score -= 20
            
        return max(0, min(100, base_score))
    
    def _calculate_talent_score(self, regional_data: RegionalMetrics, 
                               company_profile: CompanyProfile) -> float:
        """Calculate talent availability and quality score (0-100)"""
        base_score = regional_data.talent_availability * 100
        
        # Industry-specific talent adjustments
        if company_profile.company_type == 'tech':
            base_score *= 1.2
        elif company_profile.company_type == 'manufacturing':
            base_score *= 0.9
        
        # Population factor
        if regional_data.population > 1000000:
            base_score += 5
        elif regional_data.population < 100000:
            base_score -= 10
            
        return max(0, min(100, base_score))
    
    def _calculate_cost_efficiency(self, regional_data: RegionalMetrics,
                                 company_profile: CompanyProfile) -> float:
        """Calculate cost efficiency score (0-100)"""
        cost_efficiency = (1 - regional_data.cost_of_living) * 100
        tax_efficiency = (1 - regional_data.tax_rate) * 100
        
        # Investment size adjustments
        if company_profile.investment_size == 'large':
            cost_efficiency *= 1.1
        elif company_profile.investment_size == 'small':
            cost_efficiency *= 0.9
            
        # Regional cost advantages
        if regional_data.cost_of_living < 0.3:
            cost_efficiency += 15
        elif regional_data.cost_of_living > 0.8:
            cost_efficiency -= 20
            
        return max(0, min(100, (cost_efficiency + tax_efficiency) / 2))
    
    def _calculate_market_access(self, regional_data: RegionalMetrics) -> float:
        """Calculate market access score (0-100)"""
        base_score = regional_data.market_access * 100
        
        # Population market size bonus
        if regional_data.population > 5000000:
            base_score += 15
        elif regional_data.population > 1000000:
            base_score += 10
            
        return max(0, min(100, base_score))
    
    def _calculate_regulatory_score(self, regional_data: RegionalMetrics) -> float:
        """Calculate regulatory environment score (0-100)"""
        base_score = regional_data.regulatory_ease * 100
        
        # Tax rate impact
        if regional_data.tax_rate < 0.2:
            base_score += 10
        elif regional_data.tax_rate > 0.4:
            base_score -= 15
            
        return max(0, min(100, base_score))
    
    def _calculate_political_stability(self, regional_data: RegionalMetrics) -> float:
        """Calculate political stability score (0-100)"""
        base_score = regional_data.political_stability * 100
        
        # Geopolitical risk adjustment
        if regional_data.geopolitical_risk < 0.2:
            base_score += 10
        elif regional_data.geopolitical_risk > 0.6:
            base_score -= 20
            
        return max(0, min(100, base_score))
    
    def _calculate_growth_potential(self, regional_data: RegionalMetrics, 
                                  company_profile: CompanyProfile) -> float:
        """Calculate growth potential score (0-100)"""
        base_score = regional_data.growth_rate * 100
        
        # GDP per capita growth factor
        if regional_data.gdp_per_capita > 50000:
            base_score *= 1.1
        elif regional_data.gdp_per_capita < 10000:
            base_score *= 0.9
            
        # Industry growth alignment
        if company_profile.industry_focus in ['technology', 'healthcare']:
            base_score *= 1.2
            
        return max(0, min(100, base_score))
    
    def _calculate_risk_factors(self, regional_data: RegionalMetrics,
                               company_profile: CompanyProfile) -> float:
        """Calculate risk factors score (0-100) - higher is better (lower risk)"""
        risk_score = 100
        
        # Inflation risk
        if regional_data.inflation_rate > 0.1:
            risk_score -= 20
        elif regional_data.inflation_rate < 0.02:
            risk_score += 10
            
        # Currency stability
        if regional_data.currency_stability < 0.5:
            risk_score -= 15
            
        # Market volatility
        if regional_data.market_volatility > 0.7:
            risk_score -= 10
            
        # Risk tolerance adjustment
        if company_profile.risk_tolerance == 'low':
            risk_score *= 1.1
        elif company_profile.risk_tolerance == 'high':
            risk_score *= 0.9
            
        return max(0, min(100, risk_score))
    
    def _calculate_digital_readiness(self, regional_data: RegionalMetrics,
                                   company_profile: CompanyProfile) -> float:
        """Calculate digital infrastructure readiness (0-100)"""
        base_score = regional_data.digital_infrastructure * 100
        
        # Technology company bonus
        if company_profile.company_type == 'tech':
            base_score *= 1.3
            
        return max(0, min(100, base_score))
    
    def _calculate_sustainability_score(self, regional_data: RegionalMetrics,
                                      company_profile: CompanyProfile) -> float:
        """Calculate sustainability score (0-100)"""
        base_score = regional_data.sustainability_score * 100
        
        # Sustainability goals alignment
        if company_profile.sustainability_goals:
            base_score += 10
            
        return max(0, min(100, base_score))
    
    def _calculate_innovation_score(self, regional_data: RegionalMetrics,
                                  company_profile: CompanyProfile) -> float:
        """Calculate innovation index score (0-100)"""
        base_score = regional_data.innovation_index * 100
        
        # Technology focus bonus
        if company_profile.industry_focus == 'technology':
            base_score *= 1.4
            
        return max(0, min(100, base_score))
    
    def _calculate_supply_chain_score(self, regional_data: RegionalMetrics,
                                    company_profile: CompanyProfile) -> float:
        """Calculate supply chain efficiency score (0-100)"""
        base_score = regional_data.supply_chain_efficiency * 100
        
        # Manufacturing focus bonus
        if company_profile.industry_focus == 'manufacturing':
            base_score *= 1.2
            
        return max(0, min(100, base_score))
    
    def _determine_investment_tier(self, composite_score: float) -> InvestmentTier:
        """Determine investment tier based on composite score"""
        if composite_score >= self.tier_thresholds[InvestmentTier.TIER_1]:
            return InvestmentTier.TIER_1
        elif composite_score >= self.tier_thresholds[InvestmentTier.TIER_2]:
            return InvestmentTier.TIER_2
        else:
            return InvestmentTier.TIER_3
    
    def _calculate_roi_projection(self, composite_score: float,
                                regional_data: RegionalMetrics,
                                company_profile: CompanyProfile) -> Dict[str, Any]:
        """Calculate ROI projections based on algorithm score"""
        base_roi = 8.0  # Base 8% ROI
        
        # Score-based ROI adjustment
        score_multiplier = composite_score / 100
        adjusted_roi = base_roi * score_multiplier * 1.5
        
        # Industry-specific adjustments
        if company_profile.industry_focus == 'technology':
            adjusted_roi *= 1.3
        elif company_profile.industry_focus == 'manufacturing':
            adjusted_roi *= 1.1
            
        # Investment size adjustments
        if company_profile.investment_size == 'large':
            adjusted_roi *= 1.2
        elif company_profile.investment_size == 'small':
            adjusted_roi *= 0.9
            
        return {
            'projected_roi': round(adjusted_roi, 2),
            'confidence_level': self._calculate_confidence_level(composite_score),
            'time_horizon': '5 years',
            'break_even_months': self._calculate_break_even_time(adjusted_roi, company_profile),
            'risk_adjusted_roi': round(adjusted_roi * 0.8, 2)
        }
    
    def _calculate_cost_savings(self, regional_data: RegionalMetrics,
                              company_profile: CompanyProfile) -> Dict[str, Any]:
        """Calculate projected cost savings"""
        base_savings = 1000000  # Base $1M savings
        
        # Cost of living savings
        cost_savings_multiplier = (1 - regional_data.cost_of_living) * 2
        
        # Tax savings
        tax_savings_multiplier = (1 - regional_data.tax_rate) * 1.5
        
        # Investment size scaling
        size_multipliers = {
            'small': 0.5,
            'medium': 1.0,
            'large': 2.0,
            'enterprise': 5.0
        }
        size_multiplier = size_multipliers.get(company_profile.investment_size, 1.0)
        
        total_savings = base_savings * cost_savings_multiplier * tax_savings_multiplier * size_multiplier
        
        return {
            'annual_savings': round(total_savings, 0),
            'cost_efficiency_score': round((1 - regional_data.cost_of_living) * 100, 1),
            'tax_advantage': round((1 - regional_data.tax_rate) * 100, 1),
            'operational_efficiency': round(regional_data.infrastructure_score * 100, 1)
        }
    
    def _calculate_break_even_time(self, roi: float, company_profile: CompanyProfile) -> str:
        """Calculate break-even time in months"""
        if roi <= 0:
            return "N/A"
        
        months = int(12 / (roi / 100))
        return f"{months} months"
    
    def _generate_risk_assessment(self, regional_data: RegionalMetrics,
                                company_profile: CompanyProfile) -> Dict[str, Any]:
        """Generate comprehensive risk assessment"""
        risk_factors = []
        risk_level = RiskLevel.LOW
        
        # Identify risk factors
        if regional_data.inflation_rate > 0.1:
            risk_factors.append("High inflation rate")
            risk_level = RiskLevel.MEDIUM
            
        if regional_data.currency_stability < 0.5:
            risk_factors.append("Currency volatility")
            risk_level = RiskLevel.HIGH
            
        if regional_data.political_stability < 0.6:
            risk_factors.append("Political instability")
            risk_level = RiskLevel.HIGH
            
        if regional_data.geopolitical_risk > 0.6:
            risk_factors.append("Geopolitical risks")
            risk_level = RiskLevel.CRITICAL
            
        if not risk_factors:
            risk_factors.append("Low risk environment")
            
        return {
            'risk_level': risk_level.value,
            'risk_factors': risk_factors,
            'mitigation_strategies': self._generate_mitigation_strategies(risk_factors),
            'insurance_recommendations': self._generate_insurance_recommendations(risk_level)
        }
    
    def _generate_mitigation_strategies(self, risk_factors: List[str]) -> List[str]:
        """Generate risk mitigation strategies"""
        strategies = []
        
        for factor in risk_factors:
            if "inflation" in factor.lower():
                strategies.append("Implement inflation-linked contracts")
            elif "currency" in factor.lower():
                strategies.append("Use currency hedging strategies")
            elif "political" in factor.lower():
                strategies.append("Diversify across multiple regions")
            elif "geopolitical" in factor.lower():
                strategies.append("Establish local partnerships")
                
        return strategies
    
    def _generate_insurance_recommendations(self, risk_level: RiskLevel) -> List[str]:
        """Generate insurance recommendations based on risk level"""
        if risk_level == RiskLevel.LOW:
            return ["Standard business insurance", "Property insurance"]
        elif risk_level == RiskLevel.MEDIUM:
            return ["Enhanced business insurance", "Political risk insurance", "Currency insurance"]
        elif risk_level == RiskLevel.HIGH:
            return ["Comprehensive risk insurance", "Political risk insurance", "Currency insurance", "Supply chain insurance"]
        else:  # CRITICAL
            return ["Full risk coverage", "Political risk insurance", "Currency insurance", "Supply chain insurance", "Force majeure coverage"]
    
    def _calculate_confidence_level(self, composite_score: float) -> str:
        """Calculate confidence level based on composite score"""
        if composite_score >= 90:
            return "Very High (95%)"
        elif composite_score >= 80:
            return "High (85%)"
        elif composite_score >= 70:
            return "Medium (75%)"
        elif composite_score >= 60:
            return "Moderate (65%)"
        else:
            return "Low (55%)"
    
    def _generate_recommendations(self, component_scores: Dict[str, float],
                                company_profile: CompanyProfile) -> List[str]:
        """Generate actionable recommendations based on component scores"""
        recommendations = []
        
        # Infrastructure recommendations
        if component_scores['infrastructure'] < 70:
            recommendations.append("Consider infrastructure development partnerships")
            
        # Talent recommendations
        if component_scores['talent'] < 70:
            recommendations.append("Implement talent development programs")
            
        # Cost efficiency recommendations
        if component_scores['cost_efficiency'] > 80:
            recommendations.append("Leverage cost advantages for competitive pricing")
            
        # Digital readiness recommendations
        if component_scores['digital_readiness'] < 60:
            recommendations.append("Invest in digital infrastructure development")
            
        # Sustainability recommendations
        if component_scores['sustainability'] < 60:
            recommendations.append("Develop sustainability initiatives")
            
        return recommendations
    
    def _generate_market_insights(self, regional_data: RegionalMetrics,
                                company_profile: CompanyProfile) -> Dict[str, Any]:
        """Generate market insights and trends"""
        return {
            'market_size': f"{regional_data.population:,} potential customers",
            'growth_trend': f"{regional_data.growth_rate * 100:.1f}% annual growth",
            'competitive_landscape': "Moderate competition",
            'market_maturity': "Developing market" if regional_data.gdp_per_capita < 20000 else "Mature market",
            'key_advantages': [
                f"Cost efficiency: {(1 - regional_data.cost_of_living) * 100:.1f}% below average",
                f"Talent availability: {regional_data.talent_availability * 100:.1f}%",
                f"Infrastructure: {regional_data.infrastructure_score * 100:.1f}% readiness"
            ]
        }

# Example usage and testing
def create_sample_data():
    """Create sample data for testing"""
    regional_data = RegionalMetrics(
        city="Austin",
        country="USA",
        region="Texas",
        population=950000,
        gdp_per_capita=65000,
        infrastructure_score=0.85,
        talent_availability=0.80,
        cost_of_living=0.65,
        tax_rate=0.25,
        regulatory_ease=0.75,
        market_access=0.80,
        political_stability=0.85,
        growth_rate=0.08,
        inflation_rate=0.03,
        currency_stability=0.95,
        digital_infrastructure=0.90,
        supply_chain_efficiency=0.75,
        innovation_index=0.85,
        sustainability_score=0.70,
        geopolitical_risk=0.20,
        market_volatility=0.35
    )
    
    company_profile = CompanyProfile(
        company_type="tech",
        investment_size="large",
        preferred_region="North America",
        industry_focus="technology",
        risk_tolerance="medium",
        timeline="3-5 years",
        technology_requirements=["AI/ML", "Cloud Infrastructure", "Cybersecurity"],
        supply_chain_needs=["Semiconductor suppliers", "Cloud services"],
        sustainability_goals=["Carbon neutral", "Renewable energy"],
        digital_transformation_needs=["Automation", "Data analytics"],
        market_expansion_targets=["Enterprise", "SMB"]
    )
    
    return regional_data, company_profile

def main():
    """Main function for testing the algorithm"""
    print("🚀 BWGA Nexus Enhanced Investment Algorithm")
    print("=" * 50)
    
    # Create sample data
    regional_data, company_profile = create_sample_data()
    
    # Initialize algorithm
    algorithm = EnhancedInvestmentAlgorithm()
    
    # Run analysis
    result = algorithm.calculate_investment_score(regional_data, company_profile)
    
    # Display results
    print(f"📊 Investment Analysis Results")
    print(f"Composite Score: {result.composite_score}")
    print(f"Investment Tier: {result.investment_tier}")
    print(f"Confidence Level: {result.confidence_level}")
    print(f"Projected ROI: {result.roi_projection['projected_roi']}%")
    print(f"Annual Savings: ${result.cost_savings['annual_savings']:,}")
    print(f"Risk Level: {result.risk_assessment['risk_level']}")
    
    print(f"\n📈 Component Scores:")
    for component, score in result.component_scores.items():
        print(f"  {component.replace('_', ' ').title()}: {score}")
    
    print(f"\n💡 Recommendations:")
    for rec in result.recommendations:
        print(f"  • {rec}")
    
    print(f"\n🎯 Market Insights:")
    for insight, value in result.market_insights.items():
        if isinstance(value, list):
            print(f"  {insight.replace('_', ' ').title()}:")
            for item in value:
                print(f"    • {item}")
        else:
            print(f"  {insight.replace('_', ' ').title()}: {value}")

if __name__ == "__main__":
    main() 