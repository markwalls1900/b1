#!/usr/bin/env python3
"""
Revolutionary Regional Development System
AI-Powered Government-Company Matching
"""

import os
import json
import requests
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from enum import Enum

class EntityType(Enum):
    GOVERNMENT = "government"
    COMPANY = "company"
    INVESTOR = "investor"

class DevelopmentTier(Enum):
    EMERGING = "Emerging"
    GROWING = "Growing"
    ESTABLISHED = "Established"
    PREMIUM = "Premium"

class RevolutionarySystem:
    def __init__(self):
        self.regions = {
            "TX-AUS": {
                "name": "Austin Metro",
                "tier": DevelopmentTier.PREMIUM,
                "population": 2500000,
                "growth_rate": 8.5,
                "projects": ["Technology", "Smart City", "Education"],
                "match_score": 0.0
            },
            "NC-RAL": {
                "name": "Raleigh-Durham",
                "tier": DevelopmentTier.ESTABLISHED,
                "population": 1800000,
                "growth_rate": 7.2,
                "projects": ["Technology", "Healthcare", "Education"],
                "match_score": 0.0
            },
            "TN-NAS": {
                "name": "Nashville Metro",
                "tier": DevelopmentTier.GROWING,
                "population": 2100000,
                "growth_rate": 6.8,
                "projects": ["Manufacturing", "Logistics", "Healthcare"],
                "match_score": 0.0
            }
        }
        
        self.entities = {
            "GOV-TX": {
                "name": "Texas Economic Development",
                "type": EntityType.GOVERNMENT,
                "capabilities": ["Tax Incentives", "Infrastructure"],
                "interests": ["Technology", "Manufacturing"]
            },
            "COMP-TECH": {
                "name": "InnovateTech Solutions",
                "type": EntityType.COMPANY,
                "capabilities": ["AI Development", "Automation"],
                "interests": ["Technology", "Smart City"]
            },
            "INV-GROWTH": {
                "name": "Regional Growth Capital",
                "type": EntityType.INVESTOR,
                "capabilities": ["Project Financing", "Strategic Planning"],
                "interests": ["Infrastructure", "Renewable Energy"]
            }
        }
    
    def calculate_match(self, entity_id, region_id):
        """Calculate match score between entity and region"""
        entity = self.entities.get(entity_id, {})
        region = self.regions.get(region_id, {})
        
        if not entity or not region:
            return 0.0
        
        # Calculate compatibility
        common_interests = len(set(entity.get('interests', [])) & set(region.get('projects', [])))
        base_score = common_interests / max(len(entity.get('interests', [])), 1)
        
        # Adjust for growth rate
        growth_bonus = region.get('growth_rate', 0) / 10
        
        # Adjust for tier
        tier_multiplier = {
            DevelopmentTier.PREMIUM: 1.2,
            DevelopmentTier.ESTABLISHED: 1.0,
            DevelopmentTier.GROWING: 0.9,
            DevelopmentTier.EMERGING: 0.8
        }.get(region.get('tier'), 1.0)
        
        final_score = (base_score + growth_bonus) * tier_multiplier
        return min(1.0, final_score)
    
    def find_matches(self, entity_id, limit=3):
        """Find best matches for an entity"""
        matches = []
        
        for region_id in self.regions:
            score = self.calculate_match(entity_id, region_id)
            if score > 0.3:  # Only include meaningful matches
                matches.append({
                    "region_id": region_id,
                    "region_name": self.regions[region_id]["name"],
                    "match_score": round(score, 3),
                    "tier": self.regions[region_id]["tier"].value,
                    "projects": self.regions[region_id]["projects"],
                    "roi_projection": round(score * 25, 1),
                    "risk_level": "Low" if score > 0.7 else "Medium" if score > 0.5 else "High"
                })
        
        # Sort by score and return top matches
        matches.sort(key=lambda x: x["match_score"], reverse=True)
        return matches[:limit]

# Global system
system = RevolutionarySystem()

# Flask app
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template_string(get_dashboard_html())

@app.route('/api/entities')
def get_entities():
    return jsonify({"entities": system.entities})

@app.route('/api/regions')
def get_regions():
    return jsonify({"regions": system.regions})

@app.route('/api/matches/<entity_id>')
def get_matches(entity_id):
    matches = system.find_matches(entity_id)
    return jsonify({"matches": matches})

def get_dashboard_html():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Revolutionary Regional Development System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px 15px 0 0 !important;
            border: none;
        }
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
        .tier-Premium { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
        .tier-Established { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .tier-Growing { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); }
        .tier-Emerging { background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); }
        .match-score {
            font-size: 2rem;
            font-weight: 700;
            color: #667eea;
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
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Load entities
        async function loadEntities() {
            try {
                const response = await fetch('/api/entities');
                const data = await response.json();
                
                const select = document.getElementById('entitySelect');
                select.innerHTML = '<option value="">Choose an entity...</option>';
                
                Object.entries(data.entities).forEach(([id, entity]) => {
                    const option = document.createElement('option');
                    option.value = id;
                    option.textContent = `${entity.name} (${entity.type})`;
                    select.appendChild(option);
                });
            } catch (error) {
                console.error('Error loading entities:', error);
            }
        }

        // Handle matching form
        document.getElementById('matchingForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const entityId = document.getElementById('entitySelect').value;
            if (!entityId) return;
            
            const resultsDiv = document.getElementById('matchResults');
            resultsDiv.innerHTML = '<div class="text-center"><div class="spinner-border text-primary"></div><p>Finding matches...</p></div>';
            
            try {
                const response = await fetch(`/api/matches/${entityId}`);
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
                                <h6 class="card-title">${match.region_name}</h6>
                                <div class="mb-2">
                                    <span class="match-score">${(match.match_score * 100).toFixed(1)}%</span>
                                    <span class="text-muted">Match Score</span>
                                </div>
                                <div class="mb-2">
                                    <span class="tier-badge tier-${match.tier}">${match.tier}</span>
                                </div>
                                <div class="mb-2">
                                    <strong>Projects:</strong>
                                    ${match.projects.map(p => `<span class="badge bg-light text-dark me-1">${p}</span>`).join('')}
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="card bg-light">
                                    <div class="card-body">
                                        <h6>ROI Projection</h6>
                                        <div class="h4 text-success">${match.roi_projection}%</div>
                                        <small class="text-muted">3-5 years</small>
                                        <hr>
                                        <div class="mb-2">
                                            <strong>Risk Level:</strong> ${match.risk_level}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `).join('');
        }

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            loadEntities();
        });
    </script>
</body>
</html>
"""

def main():
    print("🚀 Revolutionary Regional Development System")
    print("🌍 AI-Powered Government-Company Matching")
    print("📊 Live Tier-Based Analysis")
    print("🌐 Server: http://localhost:8000")
    app.run(host='0.0.0.0', port=8000, debug=False)

if __name__ == "__main__":
    main() 