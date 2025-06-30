#!/usr/bin/env python3
"""
Revolutionary Regional Development System
Live AI Dashboard for Government-Company Matching
Never-before-seen regional development program
"""

import os
import json
import asyncio
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import random

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

class EntityType(Enum):
    GOVERNMENT = "government"
    COMPANY = "company"
    INVESTOR = "investor"
    NONPROFIT = "nonprofit"

class DevelopmentTier(Enum):
    EMERGING = "Emerging Region"
    GROWING = "Growing Region" 
    ESTABLISHED = "Established Region"
    PREMIUM = "Premium Region"

class ProjectType(Enum):
    INFRASTRUCTURE = "Infrastructure Development"
    TECHNOLOGY = "Technology Hub"
    MANUFACTURING = "Manufacturing Center"
    LOGISTICS = "Logistics Hub"
    HEALTHCARE = "Healthcare Facility"
    EDUCATION = "Education Center"
    RENEWABLE_ENERGY = "Renewable Energy"
    SMART_CITY = "Smart City Initiative"

@dataclass
class RegionalProfile:
    """Regional development profile"""
    region_id: str
    name: str
    state: str
    country: str
    population: int
    gdp_per_capita: float
    unemployment_rate: float
    growth_rate: float
    infrastructure_score: float
    talent_availability: float
    cost_of_living: float
    tax_incentives: float
    regulatory_ease: float
    market_access: float
    political_stability: float
    development_tier: DevelopmentTier
    project_opportunities: List[ProjectType]
    current_projects: List[str]
    partner_matches: List[str]
    last_updated: str

@dataclass
class EntityProfile:
    """Government or Company profile"""
    entity_id: str
    name: str
    entity_type: EntityType
    description: str
    capabilities: List[str]
    investment_capacity: float
    preferred_regions: List[str]
    project_interests: List[ProjectType]
    success_history: List[str]
    contact_info: Dict[str, str]
    matching_score: float
    last_updated: str

@dataclass
class MatchResult:
    """Matching result between entity and region"""
    match_id: str
    entity_id: str
    region_id: str
    match_score: float
    compatibility_factors: List[str]
    project_recommendations: List[str]
    risk_assessment: Dict[str, Any]
    roi_projection: Dict[str, Any]
    timeline: str
    next_steps: List[str]
    created_at: str

class RevolutionaryRegionalSystem:
    """Revolutionary regional development matching system"""
    
    def __init__(self):
        self.regions = {}
        self.entities = {}
        self.matches = {}
        self.projects = {}
        self.analytics = {}
        
        # Initialize with sample data
        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        """Initialize system with sample regional and entity data"""
        
        # Sample Regions
        sample_regions = [
            {
                "region_id": "TX-AUS",
                "name": "Austin Metro",
                "state": "Texas",
                "country": "USA",
                "population": 2500000,
                "gdp_per_capita": 75000,
                "unemployment_rate": 3.2,
                "growth_rate": 8.5,
                "infrastructure_score": 0.92,
                "talent_availability": 0.88,
                "cost_of_living": 0.75,
                "tax_incentives": 0.85,
                "regulatory_ease": 0.78,
                "market_access": 0.90,
                "political_stability": 0.95,
                "development_tier": DevelopmentTier.PREMIUM,
                "project_opportunities": [
                    ProjectType.TECHNOLOGY,
                    ProjectType.SMART_CITY,
                    ProjectType.EDUCATION
                ],
                "current_projects": ["Tech Hub Expansion", "Smart Transportation"],
                "partner_matches": [],
                "last_updated": datetime.now().isoformat()
            },
            {
                "region_id": "NC-RAL",
                "name": "Raleigh-Durham",
                "state": "North Carolina", 
                "country": "USA",
                "population": 1800000,
                "gdp_per_capita": 68000,
                "unemployment_rate": 3.8,
                "growth_rate": 7.2,
                "infrastructure_score": 0.85,
                "talent_availability": 0.82,
                "cost_of_living": 0.68,
                "tax_incentives": 0.80,
                "regulatory_ease": 0.75,
                "market_access": 0.85,
                "political_stability": 0.90,
                "development_tier": DevelopmentTier.ESTABLISHED,
                "project_opportunities": [
                    ProjectType.TECHNOLOGY,
                    ProjectType.HEALTHCARE,
                    ProjectType.EDUCATION
                ],
                "current_projects": ["Research Triangle Expansion"],
                "partner_matches": [],
                "last_updated": datetime.now().isoformat()
            },
            {
                "region_id": "TN-NAS",
                "name": "Nashville Metro",
                "state": "Tennessee",
                "country": "USA", 
                "population": 2100000,
                "gdp_per_capita": 62000,
                "unemployment_rate": 4.1,
                "growth_rate": 6.8,
                "infrastructure_score": 0.78,
                "talent_availability": 0.75,
                "cost_of_living": 0.65,
                "tax_incentives": 0.90,
                "regulatory_ease": 0.85,
                "market_access": 0.80,
                "political_stability": 0.88,
                "development_tier": DevelopmentTier.GROWING,
                "project_opportunities": [
                    ProjectType.MANUFACTURING,
                    ProjectType.LOGISTICS,
                    ProjectType.HEALTHCARE
                ],
                "current_projects": ["Music Industry Hub"],
                "partner_matches": [],
                "last_updated": datetime.now().isoformat()
            }
        ]
        
        for region_data in sample_regions:
            self.regions[region_data["region_id"]] = RegionalProfile(**region_data)
        
        # Sample Entities
        sample_entities = [
            {
                "entity_id": "GOV-TX",
                "name": "Texas Economic Development Corporation",
                "entity_type": EntityType.GOVERNMENT,
                "description": "State agency focused on economic development and business attraction",
                "capabilities": ["Tax Incentives", "Infrastructure Development", "Workforce Training"],
                "investment_capacity": 500000000,
                "preferred_regions": ["TX-AUS", "TX-HOU", "TX-DAL"],
                "project_interests": [
                    ProjectType.TECHNOLOGY,
                    ProjectType.MANUFACTURING,
                    ProjectType.INFRASTRUCTURE
                ],
                "success_history": ["Tesla Gigafactory", "Samsung Semiconductor"],
                "contact_info": {
                    "email": "contact@texasedc.org",
                    "phone": "+1-512-555-0123",
                    "website": "www.texasedc.org"
                },
                "matching_score": 0.0,
                "last_updated": datetime.now().isoformat()
            },
            {
                "entity_id": "COMP-TECH",
                "name": "InnovateTech Solutions",
                "entity_type": EntityType.COMPANY,
                "description": "Technology company specializing in AI and automation",
                "capabilities": ["AI Development", "Automation", "Data Analytics"],
                "investment_capacity": 25000000,
                "preferred_regions": ["TX-AUS", "NC-RAL", "CA-SF"],
                "project_interests": [
                    ProjectType.TECHNOLOGY,
                    ProjectType.SMART_CITY,
                    ProjectType.EDUCATION
                ],
                "success_history": ["Smart City Implementation", "AI Education Platform"],
                "contact_info": {
                    "email": "partnerships@innovatetech.com",
                    "phone": "+1-415-555-0456",
                    "website": "www.innovatetech.com"
                },
                "matching_score": 0.0,
                "last_updated": datetime.now().isoformat()
            },
            {
                "entity_id": "INV-GROWTH",
                "name": "Regional Growth Capital",
                "entity_type": EntityType.INVESTOR,
                "description": "Investment firm focused on regional development projects",
                "capabilities": ["Project Financing", "Strategic Planning", "Market Analysis"],
                "investment_capacity": 100000000,
                "preferred_regions": ["TN-NAS", "NC-RAL", "GA-ATL"],
                "project_interests": [
                    ProjectType.INFRASTRUCTURE,
                    ProjectType.RENEWABLE_ENERGY,
                    ProjectType.LOGISTICS
                ],
                "success_history": ["Solar Farm Development", "Port Expansion"],
                "contact_info": {
                    "email": "investments@regionalgrowth.com",
                    "phone": "+1-404-555-0789",
                    "website": "www.regionalgrowth.com"
                },
                "matching_score": 0.0,
                "last_updated": datetime.now().isoformat()
            }
        ]
        
        for entity_data in sample_entities:
            self.entities[entity_data["entity_id"]] = EntityProfile(**entity_data)
    
    def calculate_development_tier(self, region: RegionalProfile) -> DevelopmentTier:
        """Calculate development tier based on regional metrics"""
        score = (
            region.growth_rate * 0.25 +
            region.infrastructure_score * 0.20 +
            region.talent_availability * 0.15 +
            region.gdp_per_capita / 100000 * 0.15 +
            region.political_stability * 0.15 +
            (1 - region.unemployment_rate / 10) * 0.10
        )
        
        if score >= 0.85:
            return DevelopmentTier.PREMIUM
        elif score >= 0.70:
            return DevelopmentTier.ESTABLISHED
        elif score >= 0.55:
            return DevelopmentTier.GROWING
        else:
            return DevelopmentTier.EMERGING
    
    def calculate_match_score(self, entity: EntityProfile, region: RegionalProfile) -> float:
        """Calculate compatibility score between entity and region"""
        
        # Base compatibility factors
        region_preference = 1.0 if region.region_id in entity.preferred_regions else 0.5
        
        # Project interest alignment
        project_alignment = len(set(entity.project_interests) & set(region.project_opportunities)) / max(len(entity.project_interests), 1)
        
        # Economic factors
        economic_compatibility = (
            (region.growth_rate / 10) * 0.3 +
            region.infrastructure_score * 0.25 +
            region.talent_availability * 0.25 +
            (1 - region.cost_of_living) * 0.2
        )
        
        # Risk factors
        risk_score = (
            region.political_stability * 0.4 +
            region.regulatory_ease * 0.3 +
            (1 - region.unemployment_rate / 10) * 0.3
        )
        
        # Calculate final score
        match_score = (
            region_preference * 0.25 +
            project_alignment * 0.30 +
            economic_compatibility * 0.25 +
            risk_score * 0.20
        )
        
        return round(match_score, 3)
    
    def generate_match_recommendations(self, entity: EntityProfile, region: RegionalProfile) -> MatchResult:
        """Generate comprehensive match recommendations"""
        
        match_score = self.calculate_match_score(entity, region)
        
        # Identify compatibility factors
        compatibility_factors = []
        if region.region_id in entity.preferred_regions:
            compatibility_factors.append("Region in preferred locations")
        
        common_projects = set(entity.project_interests) & set(region.project_opportunities)
        if common_projects:
            compatibility_factors.append(f"Shared project interests: {', '.join([p.value for p in common_projects])}")
        
        if region.growth_rate > 5:
            compatibility_factors.append("High growth potential")
        
        if region.infrastructure_score > 0.8:
            compatibility_factors.append("Strong infrastructure")
        
        # Generate project recommendations
        project_recommendations = []
        for project in common_projects:
            if project == ProjectType.TECHNOLOGY:
                project_recommendations.append("Establish technology innovation hub")
            elif project == ProjectType.MANUFACTURING:
                project_recommendations.append("Develop advanced manufacturing facility")
            elif project == ProjectType.INFRASTRUCTURE:
                project_recommendations.append("Invest in critical infrastructure projects")
            elif project == ProjectType.SMART_CITY:
                project_recommendations.append("Implement smart city technologies")
        
        # Risk assessment
        risk_assessment = {
            "overall_risk": "Low" if match_score > 0.7 else "Medium" if match_score > 0.5 else "High",
            "political_risk": "Low" if region.political_stability > 0.8 else "Medium",
            "economic_risk": "Low" if region.growth_rate > 5 else "Medium",
            "infrastructure_risk": "Low" if region.infrastructure_score > 0.8 else "Medium",
            "mitigation_strategies": [
                "Establish local partnerships",
                "Conduct thorough due diligence",
                "Develop contingency plans"
            ]
        }
        
        # ROI projection
        base_roi = match_score * 25  # Base ROI percentage
        roi_projection = {
            "projected_roi": round(base_roi, 1),
            "time_horizon": "3-5 years",
            "break_even_months": int(24 / (base_roi / 100)),
            "confidence_level": "High" if match_score > 0.7 else "Medium"
        }
        
        # Timeline and next steps
        timeline = "6-12 months for initial setup, 2-3 years for full implementation"
        next_steps = [
            "Schedule initial meeting with regional representatives",
            "Conduct site visit and feasibility study",
            "Develop detailed project proposal",
            "Negotiate terms and incentives",
            "Begin implementation planning"
        ]
        
        match_id = f"MATCH-{entity.entity_id}-{region.region_id}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        return MatchResult(
            match_id=match_id,
            entity_id=entity.entity_id,
            region_id=region.region_id,
            match_score=match_score,
            compatibility_factors=compatibility_factors,
            project_recommendations=project_recommendations,
            risk_assessment=risk_assessment,
            roi_projection=roi_projection,
            timeline=timeline,
            next_steps=next_steps,
            created_at=datetime.now().isoformat()
        )
    
    def find_best_matches(self, entity_id: str, limit: int = 5) -> List[MatchResult]:
        """Find best regional matches for an entity"""
        if entity_id not in self.entities:
            return []
        
        entity = self.entities[entity_id]
        matches = []
        
        for region in self.regions.values():
            match = self.generate_match_recommendations(entity, region)
            matches.append(match)
        
        # Sort by match score and return top matches
        matches.sort(key=lambda x: x.match_score, reverse=True)
        return matches[:limit]
    
    def get_regional_analytics(self) -> Dict[str, Any]:
        """Get comprehensive regional development analytics"""
        total_regions = len(self.regions)
        total_entities = len(self.entities)
        total_matches = len(self.matches)
        
        # Tier distribution
        tier_distribution = {}
        for tier in DevelopmentTier:
            tier_distribution[tier.value] = len([r for r in self.regions.values() if r.development_tier == tier])
        
        # Project type distribution
        project_distribution = {}
        for project in ProjectType:
            project_distribution[project.value] = len([r for r in self.regions.values() if project in r.project_opportunities])
        
        # Entity type distribution
        entity_distribution = {}
        for entity_type in EntityType:
            entity_distribution[entity_type.value] = len([e for e in self.entities.values() if e.entity_type == entity_type])
        
        return {
            "total_regions": total_regions,
            "total_entities": total_entities,
            "total_matches": total_matches,
            "tier_distribution": tier_distribution,
            "project_distribution": project_distribution,
            "entity_distribution": entity_distribution,
            "average_match_score": sum([m.match_score for m in self.matches.values()]) / max(len(self.matches), 1),
            "last_updated": datetime.now().isoformat()
        }

# Global system instance
revolutionary_system = RevolutionaryRegionalSystem()

# Flask app
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Main dashboard"""
    return render_template_string(get_dashboard_html())

@app.route('/api/v1/analytics')
def get_analytics():
    """Get system analytics"""
    return jsonify(revolutionary_system.get_regional_analytics())

@app.route('/api/v1/regions')
def get_regions():
    """Get all regions"""
    regions = [asdict(region) for region in revolutionary_system.regions.values()]
    return jsonify({"regions": regions})

@app.route('/api/v1/entities')
def get_entities():
    """Get all entities"""
    entities = [asdict(entity) for entity in revolutionary_system.entities.values()]
    return jsonify({"entities": entities})

@app.route('/api/v1/matches/<entity_id>')
def get_matches(entity_id):
    """Get matches for an entity"""
    matches = revolutionary_system.find_best_matches(entity_id)
    return jsonify({"matches": [asdict(match) for match in matches]})

@app.route('/api/v1/entity/<entity_id>')
def get_entity(entity_id):
    """Get specific entity"""
    if entity_id in revolutionary_system.entities:
        return jsonify(asdict(revolutionary_system.entities[entity_id]))
    return jsonify({"error": "Entity not found"}), 404

@app.route('/api/v1/region/<region_id>')
def get_region(region_id):
    """Get specific region"""
    if region_id in revolutionary_system.regions:
        return jsonify(asdict(revolutionary_system.regions[region_id]))
    return jsonify({"error": "Region not found"}), 404

def get_dashboard_html():
    """Get the revolutionary dashboard HTML"""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Revolutionary Regional Development System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            --primary: #1e40af;
            --secondary: #64748b;
            --success: #059669;
            --warning: #d97706;
            --danger: #dc2626;
            --dark: #0f172a;
            --light: #f8fafc;
            --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --gradient-success: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            --gradient-warning: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            --gradient-danger: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        }

        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .main-container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            margin: 20px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        }

        .header {
            background: var(--gradient-primary);
            color: white;
            padding: 2rem;
            text-align: center;
            border-radius: 20px 20px 0 0;
        }

        .content { padding: 2rem; }

        .card {
            border: none;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .card:hover { transform: translateY(-5px); }

        .card-header {
            background: var(--gradient-primary);
            color: white;
            border-radius: 15px 15px 0 0 !important;
            border: none;
        }

        .btn-primary {
            background: var(--gradient-primary);
            border: none;
            border-radius: 10px;
            padding: 12px 30px;
            font-weight: 600;
        }

        .tier-badge {
            display: inline-block;
            padding: 8px 20px;
            border-radius: 25px;
            font-weight: 600;
            color: white;
        }

        .tier-premium { background: var(--gradient-success); }
        .tier-established { background: var(--gradient-primary); }
        .tier-growing { background: var(--gradient-warning); }
        .tier-emerging { background: var(--gradient-danger); }

        .entity-card {
            border-left: 4px solid var(--primary);
            margin-bottom: 1rem;
        }

        .match-score {
            font-size: 2rem;
            font-weight: 700;
            color: var(--primary);
        }

        .loading {
            display: none;
            text-align: center;
            padding: 2rem;
        }

        .spinner {
            width: 40px;
            height: 40px;
            border: 4px solid #f3f3f3;
            border-top: 4px solid var(--primary);
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .nav-tabs .nav-link {
            border: none;
            border-radius: 10px 10px 0 0;
            margin-right: 5px;
        }

        .nav-tabs .nav-link.active {
            background: var(--gradient-primary);
            color: white;
        }
    </style>
</head>
<body>
    <div class="main-container">
        <div class="header">
            <h1><i class="fas fa-globe-americas me-3"></i>Revolutionary Regional Development System</h1>
            <p>AI-Powered Government-Company Matching for Regional Growth</p>
        </div>
        
        <div class="content">
            <!-- Navigation Tabs -->
            <ul class="nav nav-tabs mb-4" id="mainTabs" role="tablist">
                <li class="nav-item" role="presentation">
                    <button class="nav-link active" id="overview-tab" data-bs-toggle="tab" data-bs-target="#overview" type="button" role="tab">
                        <i class="fas fa-chart-line me-2"></i>System Overview
                    </button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="matching-tab" data-bs-toggle="tab" data-bs-target="#matching" type="button" role="tab">
                        <i class="fas fa-handshake me-2"></i>Smart Matching
                    </button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="regions-tab" data-bs-toggle="tab" data-bs-target="#regions" type="button" role="tab">
                        <i class="fas fa-map-marker-alt me-2"></i>Regional Profiles
                    </button>
                </li>
                <li class="nav-item" role="presentation">
                    <button class="nav-link" id="entities-tab" data-bs-toggle="tab" data-bs-target="#entities" type="button" role="tab">
                        <i class="fas fa-building me-2"></i>Entity Directory
                    </button>
                </li>
            </ul>

            <!-- Tab Content -->
            <div class="tab-content" id="mainTabContent">
                <!-- Overview Tab -->
                <div class="tab-pane fade show active" id="overview" role="tabpanel">
                    <div class="row">
                        <div class="col-md-6">
                            <div class="card mb-4">
                                <div class="card-header">
                                    <h5 class="mb-0"><i class="fas fa-chart-pie me-2"></i>System Analytics</h5>
                                </div>
                                <div class="card-body">
                                    <div id="analyticsDisplay">
                                        <div class="loading">
                                            <div class="spinner"></div>
                                            <p>Loading analytics...</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="card mb-4">
                                <div class="card-header">
                                    <h5 class="mb-0"><i class="fas fa-chart-bar me-2"></i>Development Tiers</h5>
                                </div>
                                <div class="card-body">
                                    <canvas id="tierChart" height="200"></canvas>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Matching Tab -->
                <div class="tab-pane fade" id="matching" role="tabpanel">
                    <div class="row">
                        <div class="col-md-4">
                            <div class="card">
                                <div class="card-header">
                                    <h5 class="mb-0"><i class="fas fa-search me-2"></i>Find Matches</h5>
                                </div>
                                <div class="card-body">
                                    <form id="matchingForm">
                                        <div class="mb-3">
                                            <label class="form-label">Select Entity</label>
                                            <select class="form-select" id="entitySelect" required>
                                                <option value="">Choose an entity...</option>
                                            </select>
                                        </div>
                                        <button type="submit" class="btn btn-primary w-100">
                                            <i class="fas fa-rocket me-2"></i>Find Best Matches
                                        </button>
                                    </form>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-8">
                            <div class="card">
                                <div class="card-header">
                                    <h5 class="mb-0"><i class="fas fa-star me-2"></i>Match Results</h5>
                                </div>
                                <div class="card-body">
                                    <div id="matchResults">
                                        <div class="text-center text-muted">
                                            <i class="fas fa-handshake fa-3x mb-3"></i>
                                            <h5>Ready for Matching</h5>
                                            <p>Select an entity to find the best regional matches</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Regions Tab -->
                <div class="tab-pane fade" id="regions" role="tabpanel">
                    <div class="row" id="regionsDisplay">
                        <div class="loading">
                            <div class="spinner"></div>
                            <p>Loading regional profiles...</p>
                        </div>
                    </div>
                </div>

                <!-- Entities Tab -->
                <div class="tab-pane fade" id="entities" role="tabpanel">
                    <div class="row" id="entitiesDisplay">
                        <div class="loading">
                            <div class="spinner"></div>
                            <p>Loading entity directory...</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Global variables
        let analyticsData = {};
        let tierChart = null;

        // Initialize dashboard
        document.addEventListener('DOMContentLoaded', function() {
            loadAnalytics();
            loadEntities();
            loadRegions();
        });

        // Load system analytics
        async function loadAnalytics() {
            try {
                const response = await fetch('/api/v1/analytics');
                analyticsData = await response.json();
                displayAnalytics();
                createTierChart();
            } catch (error) {
                console.error('Error loading analytics:', error);
            }
        }

        // Display analytics
        function displayAnalytics() {
            const display = document.getElementById('analyticsDisplay');
            display.innerHTML = `
                <div class="row text-center">
                    <div class="col-4">
                        <div class="h3 text-primary">${analyticsData.total_regions || 0}</div>
                        <small class="text-muted">Regions</small>
                    </div>
                    <div class="col-4">
                        <div class="h3 text-success">${analyticsData.total_entities || 0}</div>
                        <small class="text-muted">Entities</small>
                    </div>
                    <div class="col-4">
                        <div class="h3 text-warning">${analyticsData.total_matches || 0}</div>
                        <small class="text-muted">Matches</small>
                    </div>
                </div>
                <div class="mt-3">
                    <div class="d-flex justify-content-between">
                        <span>Average Match Score:</span>
                        <span class="fw-bold">${(analyticsData.average_match_score * 100).toFixed(1)}%</span>
                    </div>
                </div>
            `;
        }

        // Create tier chart
        function createTierChart() {
            const ctx = document.getElementById('tierChart').getContext('2d');
            const tierData = analyticsData.tier_distribution || {};
            
            tierChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: Object.keys(tierData),
                    datasets: [{
                        data: Object.values(tierData),
                        backgroundColor: [
                            '#4facfe',
                            '#667eea', 
                            '#fa709a',
                            '#ff9a9e'
                        ]
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom'
                        }
                    }
                }
            });
        }

        // Load entities
        async function loadEntities() {
            try {
                const response = await fetch('/api/v1/entities');
                const data = await response.json();
                
                const select = document.getElementById('entitySelect');
                select.innerHTML = '<option value="">Choose an entity...</option>';
                
                data.entities.forEach(entity => {
                    const option = document.createElement('option');
                    option.value = entity.entity_id;
                    option.textContent = `${entity.name} (${entity.entity_type})`;
                    select.appendChild(option);
                });
            } catch (error) {
                console.error('Error loading entities:', error);
            }
        }

        // Load regions
        async function loadRegions() {
            try {
                const response = await fetch('/api/v1/regions');
                const data = await response.json();
                
                const display = document.getElementById('regionsDisplay');
                display.innerHTML = '';
                
                data.regions.forEach(region => {
                    const regionCard = createRegionCard(region);
                    display.appendChild(regionCard);
                });
            } catch (error) {
                console.error('Error loading regions:', error);
            }
        }

        // Create region card
        function createRegionCard(region) {
            const col = document.createElement('div');
            col.className = 'col-md-6 col-lg-4 mb-4';
            
            const tierClass = `tier-${region.development_tier.toLowerCase().replace(' ', '-')}`;
            
            col.innerHTML = `
                <div class="card h-100">
                    <div class="card-header">
                        <h6 class="mb-0">${region.name}</h6>
                    </div>
                    <div class="card-body">
                        <div class="mb-2">
                            <span class="tier-badge ${tierClass}">${region.development_tier}</span>
                        </div>
                        <div class="row text-center mb-3">
                            <div class="col-6">
                                <div class="h5 text-primary">${region.population.toLocaleString()}</div>
                                <small class="text-muted">Population</small>
                            </div>
                            <div class="col-6">
                                <div class="h5 text-success">${region.growth_rate}%</div>
                                <small class="text-muted">Growth Rate</small>
                            </div>
                        </div>
                        <div class="mb-2">
                            <strong>Projects:</strong>
                            <div class="mt-1">
                                ${region.project_opportunities.map(p => `<span class="badge bg-light text-dark me-1">${p}</span>`).join('')}
                            </div>
                        </div>
                    </div>
                </div>
            `;
            
            return col;
        }

        // Handle matching form
        document.getElementById('matchingForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const entityId = document.getElementById('entitySelect').value;
            if (!entityId) return;
            
            const resultsDiv = document.getElementById('matchResults');
            resultsDiv.innerHTML = '<div class="loading"><div class="spinner"></div><p>Finding best matches...</p></div>';
            
            try {
                const response = await fetch(`/api/v1/matches/${entityId}`);
                const data = await response.json();
                
                displayMatches(data.matches);
            } catch (error) {
                resultsDiv.innerHTML = '<div class="alert alert-danger">Error finding matches</div>';
            }
        });

        // Display matches
        function displayMatches(matches) {
            const resultsDiv = document.getElementById('matchResults');
            
            if (matches.length === 0) {
                resultsDiv.innerHTML = '<div class="alert alert-info">No matches found</div>';
                return;
            }
            
            resultsDiv.innerHTML = matches.map(match => `
                <div class="card mb-3">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-8">
                                <h6 class="card-title">${match.region_id}</h6>
                                <div class="mb-2">
                                    <span class="match-score">${(match.match_score * 100).toFixed(1)}%</span>
                                    <span class="text-muted">Match Score</span>
                                </div>
                                <div class="mb-2">
                                    <strong>Compatibility:</strong>
                                    <ul class="mb-2">
                                        ${match.compatibility_factors.map(factor => `<li>${factor}</li>`).join('')}
                                    </ul>
                                </div>
                                <div class="mb-2">
                                    <strong>Projects:</strong>
                                    <ul class="mb-2">
                                        ${match.project_recommendations.map(project => `<li>${project}</li>`).join('')}
                                    </ul>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="card bg-light">
                                    <div class="card-body">
                                        <h6>ROI Projection</h6>
                                        <div class="h4 text-success">${match.roi_projection.projected_roi}%</div>
                                        <small class="text-muted">${match.roi_projection.time_horizon}</small>
                                        <hr>
                                        <div class="mb-2">
                                            <strong>Risk Level:</strong> ${match.risk_assessment.overall_risk}
                                        </div>
                                        <div class="mb-2">
                                            <strong>Timeline:</strong> ${match.timeline}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `).join('');
        }
    </script>
</body>
</html>
"""

def main():
    """Main function"""
    print("🚀 Starting Revolutionary Regional Development System...")
    print("Version: 1.0.0 - Never-Before-Seen Regional Development Program")
    print("-" * 60)
    print("🌍 AI-Powered Government-Company Matching System")
    print("📊 Live Tier-Based Regional Development Analysis")
    print("🤝 Intelligent Partner Matching Algorithm")
    print("📈 Real-Time ROI Projections and Risk Assessment")
    print("-" * 60)
    print("🌐 Server running at: http://localhost:8000")
    print("📱 Dashboard: http://localhost:8000")
    print("🔗 API Health: http://localhost:8000/api/v1/analytics")
    print("Press Ctrl+C to stop the server")
    print("-" * 60)
    
    # Run Flask app
    app.run(host='0.0.0.0', port=8000, debug=False)

if __name__ == "__main__":
    main() 