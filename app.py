#!/usr/bin/env python3
"""
BWGA Nexus - Unified Investment Intelligence Platform
Clean, functional tier report developer system
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

# Import our core modules
try:
    from investment_algorithm import AdvancedRegionalInvestmentAlgorithm, RegionalMetrics, CompanyProfile
    ALGORITHM_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Investment algorithm not available: {e}")
    ALGORITHM_AVAILABLE = False

# Flask app setup
app = Flask(__name__)
CORS(app)

# Global system instance
if ALGORITHM_AVAILABLE:
    algorithm = AdvancedRegionalInvestmentAlgorithm()
else:
    algorithm = None

@app.route('/')
def index():
    """Main dashboard"""
    return render_template_string(get_dashboard_html())

@app.route('/api/v1/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "7.1.0",
        "algorithm_available": ALGORITHM_AVAILABLE,
        "message": "BWGA Nexus Investment Intelligence Platform"
    })

@app.route('/api/v1/system-info')
def system_info():
    """System information endpoint"""
    return jsonify({
        "system_name": "BWGA Nexus Investment Intelligence Platform",
        "version": "7.1.0",
        "algorithm_status": "Active" if ALGORITHM_AVAILABLE else "Not Available",
        "features": [
            "3-Tier Investment Analysis",
            "Regional Investment Intelligence", 
            "Real-time Algorithm Processing",
            "Comprehensive Risk Assessment",
            "ROI Projections",
            "Cost Savings Analysis"
        ]
    })

@app.route('/api/v1/analyze/investment', methods=['POST'])
def analyze_investment():
    """Investment analysis endpoint"""
    try:
        request_data = request.get_json()
        if not request_data:
            return jsonify({
                "success": False,
                "error": "No data provided",
                "message": "Please provide investment parameters"
            }), 400
        
        if not ALGORITHM_AVAILABLE:
            return jsonify({
                "success": False,
                "error": "Algorithm not available",
                "message": "Please ensure investment_algorithm.py is properly configured"
            }), 500
        
        # Create regional data
        regional_data = RegionalMetrics(
            city=request_data.get('city', 'Austin'),
            country=request_data.get('country', 'USA'),
            region=request_data.get('region', 'Texas'),
            population=request_data.get('population', 950000),
            gdp_per_capita=request_data.get('gdp_per_capita', 65000),
            infrastructure_score=request_data.get('infrastructure_score', 0.85),
            talent_availability=request_data.get('talent_availability', 0.80),
            cost_of_living=request_data.get('cost_of_living', 0.65),
            tax_rate=request_data.get('tax_rate', 0.25),
            regulatory_ease=request_data.get('regulatory_ease', 0.75),
            market_access=request_data.get('market_access', 0.80),
            political_stability=request_data.get('political_stability', 0.85),
            growth_rate=request_data.get('growth_rate', 0.08),
            inflation_rate=request_data.get('inflation_rate', 0.03),
            currency_stability=request_data.get('currency_stability', 0.95),
            digital_infrastructure=request_data.get('digital_infrastructure', 0.90),
            supply_chain_efficiency=request_data.get('supply_chain_efficiency', 0.75),
            innovation_index=request_data.get('innovation_index', 0.85),
            sustainability_score=request_data.get('sustainability_score', 0.70),
            geopolitical_risk=request_data.get('geopolitical_risk', 0.20),
            market_volatility=request_data.get('market_volatility', 0.35)
        )
        
        # Create company profile
        company_profile = CompanyProfile(
            company_type=request_data.get('company_type', 'technology'),
            investment_size=request_data.get('investment_size', 'large'),
            preferred_region=request_data.get('preferred_region', 'North America'),
            industry_focus=request_data.get('industry_focus', 'technology'),
            risk_tolerance=request_data.get('risk_tolerance', 'medium'),
            timeline=request_data.get('timeline', '3-5 years'),
            technology_requirements=request_data.get('technology_requirements', ['AI/ML', 'Cloud']),
            supply_chain_needs=request_data.get('supply_chain_needs', ['Semiconductors']),
            sustainability_goals=request_data.get('sustainability_goals', ['Carbon neutral', 'Renewable energy']),
            digital_transformation_needs=request_data.get('digital_transformation_needs', ['Automation', 'Data analytics']),
            market_expansion_targets=request_data.get('market_expansion_targets', ['Enterprise', 'SMB'])
        )
        
        # Run algorithm
        result = algorithm.calculate_investment_score(regional_data, company_profile)
        
        return jsonify({
            "success": True,
            "analysis_result": result,
            "algorithm_used": "BWGA Nexus Advanced Algorithm",
            "analysis_timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Analysis failed"
        }), 500

def get_dashboard_html():
    """Get the dashboard HTML template"""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BWGA Nexus - Investment Intelligence Platform</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
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
        .score-display {
            font-size: 4rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }
        .tier-badge {
            display: inline-block;
            padding: 8px 20px;
            border-radius: 25px;
            font-weight: 600;
            color: white;
        }
        .tier-premium { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
        .tier-strategic { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); }
        .tier-emerging { background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); }
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: #667eea;
        }
        .loading { display: none; text-align: center; padding: 2rem; }
        .spinner {
            width: 40px;
            height: 40px;
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="main-container">
        <div class="header">
            <h1><i class="fas fa-chart-line me-3"></i>BWGA Nexus Investment Intelligence</h1>
            <p>Advanced algorithmic analysis with real-time insights</p>
        </div>
        
        <div class="content">
            <div class="row">
                <div class="col-lg-6">
                    <div class="card mb-4">
                        <div class="card-header">
                            <h5 class="mb-0"><i class="fas fa-calculator me-2"></i>Investment Analysis</h5>
                        </div>
                        <div class="card-body">
                            <form id="analysisForm">
                                <div class="row">
                                    <div class="col-md-6 mb-3">
                                        <label class="form-label">Company Type</label>
                                        <select class="form-select" id="companyType" required>
                                            <option value="">Select Type</option>
                                            <option value="technology">Technology</option>
                                            <option value="manufacturing">Manufacturing</option>
                                            <option value="finance">Finance</option>
                                            <option value="logistics">Logistics</option>
                                        </select>
                                    </div>
                                    <div class="col-md-6 mb-3">
                                        <label class="form-label">Investment Size</label>
                                        <select class="form-select" id="investmentSize" required>
                                            <option value="">Select Size</option>
                                            <option value="small">Small ($1M - $10M)</option>
                                            <option value="medium">Medium ($10M - $100M)</option>
                                            <option value="large">Large ($100M+)</option>
                                        </select>
                                    </div>
                                </div>
                                
                                <div class="row">
                                    <div class="col-md-6 mb-3">
                                        <label class="form-label">Risk Tolerance</label>
                                        <select class="form-select" id="riskTolerance" required>
                                            <option value="">Select Risk Level</option>
                                            <option value="low">Conservative</option>
                                            <option value="medium">Moderate</option>
                                            <option value="high">Aggressive</option>
                                        </select>
                                    </div>
                                    <div class="col-md-6 mb-3">
                                        <label class="form-label">Target Region</label>
                                        <select class="form-select" id="region" required>
                                            <option value="">Select Region</option>
                                            <option value="North America">North America</option>
                                            <option value="Europe">Europe</option>
                                            <option value="Asia Pacific">Asia Pacific</option>
                                        </select>
                                    </div>
                                </div>

                                <div class="mb-3">
                                    <label class="form-label">Target City</label>
                                    <input type="text" class="form-control" id="city" placeholder="e.g., Austin, Texas" required>
                                </div>

                                <button type="submit" class="btn btn-primary w-100">
                                    <i class="fas fa-rocket me-2"></i>Run Complete Analysis
                                </button>
                            </form>
                        </div>
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="card">
                        <div class="card-header">
                            <h5 class="mb-0"><i class="fas fa-chart-bar me-2"></i>Analysis Results</h5>
                        </div>
                        <div class="card-body">
                            <div class="loading" id="loadingState">
                                <div class="spinner"></div>
                                <p>Running advanced algorithm analysis...</p>
                            </div>

                            <div id="resultsDisplay" style="display: none;">
                                <div class="text-center mb-4">
                                    <div class="score-display" id="compositeScore">--</div>
                                    <div class="tier-badge" id="tierBadge">--</div>
                                </div>

                                <div class="row mb-4">
                                    <div class="col-6">
                                        <div class="text-center">
                                            <div class="metric-value" id="projectedROI">--</div>
                                            <small class="text-muted">Projected ROI</small>
                                        </div>
                                    </div>
                                    <div class="col-6">
                                        <div class="text-center">
                                            <div class="metric-value" id="annualSavings">--</div>
                                            <small class="text-muted">Annual Savings</small>
                                        </div>
                                    </div>
                                </div>

                                <div class="alert alert-info">
                                    <h6><i class="fas fa-shield-alt me-2"></i>Risk Assessment</h6>
                                    <div id="riskDetails">--</div>
                                </div>

                                <div class="alert alert-success">
                                    <h6><i class="fas fa-lightbulb me-2"></i>Recommendations</h6>
                                    <div id="recommendations">--</div>
                                </div>
                            </div>

                            <div id="initialState" class="text-center text-muted">
                                <i class="fas fa-chart-line fa-3x mb-3"></i>
                                <h5>Ready for Analysis</h5>
                                <p>Fill out the form and click "Run Complete Analysis" to get started</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.getElementById('analysisForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = {
                company_type: document.getElementById('companyType').value,
                investment_size: document.getElementById('investmentSize').value,
                risk_tolerance: document.getElementById('riskTolerance').value,
                preferred_region: document.getElementById('region').value,
                city: document.getElementById('city').value,
                industry_focus: document.getElementById('companyType').value
            };

            // Show loading
            document.getElementById('loadingState').style.display = 'block';
            document.getElementById('resultsDisplay').style.display = 'none';
            document.getElementById('initialState').style.display = 'none';

            try {
                const response = await fetch('/api/v1/analyze/investment', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(formData)
                });
                
                const data = await response.json();
                
                if (data.success) {
                    displayResults(data.analysis_result);
                } else {
                    showError(data.message || 'Analysis failed');
                }
            } catch (error) {
                showError('Connection error. Please try again.');
            } finally {
                document.getElementById('loadingState').style.display = 'none';
            }
        });

        function displayResults(result) {
            document.getElementById('resultsDisplay').style.display = 'block';
            document.getElementById('initialState').style.display = 'none';

            document.getElementById('compositeScore').textContent = result.composite_score;
            
            const tierBadge = document.getElementById('tierBadge');
            tierBadge.textContent = result.tier_level;
            tierBadge.className = 'tier-badge ' + getTierClass(result.investment_tier);

            document.getElementById('projectedROI').textContent = result.roi_projection.projected_roi + '%';
            document.getElementById('annualSavings').textContent = '$' + (result.cost_savings.annual_savings / 1000000).toFixed(1) + 'M';

            document.getElementById('riskDetails').innerHTML = `
                <strong>Risk Level:</strong> ${result.risk_assessment.risk_level}<br>
                <strong>Risk Score:</strong> ${result.risk_assessment.risk_score}/100<br>
                <strong>Break-even:</strong> ${result.roi_projection.break_even_months} months
            `;

            const recommendations = result.recommendations || [
                'Consider phased investment approach',
                'Monitor market conditions closely',
                'Establish risk mitigation strategies'
            ];
            
            document.getElementById('recommendations').innerHTML = 
                recommendations.map(rec => `<div class="mb-2"><i class="fas fa-check me-2"></i>${rec}</div>`).join('');
        }

        function getTierClass(tier) {
            if (tier.includes('TIER_1')) return 'tier-premium';
            if (tier.includes('TIER_2')) return 'tier-strategic';
            if (tier.includes('TIER_3')) return 'tier-emerging';
            return 'tier-premium';
        }

        function showError(message) {
            document.getElementById('resultsDisplay').style.display = 'none';
            document.getElementById('initialState').style.display = 'block';
            
            const alertDiv = document.createElement('div');
            alertDiv.className = 'alert alert-danger alert-dismissible fade show';
            alertDiv.innerHTML = `
                <i class="fas fa-exclamation-triangle me-2"></i>${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            `;
            
            document.querySelector('.content').insertBefore(alertDiv, document.querySelector('.content').firstChild);
        }
    </script>
</body>
</html>
"""

def main():
    """Main function to run the application"""
    print("🌍 Starting BWGA Nexus Investment Intelligence Platform...")
    print("Version: 7.1.0")
    print("Environment: Production (Unified System)")
    print("-" * 50)
    
    if ALGORITHM_AVAILABLE:
        print("✅ Investment algorithm loaded successfully!")
    else:
        print("❌ Investment algorithm not available")
    
    print("🌍 BWGA Nexus Investment Intelligence Platform")
    print("Version: 7.1.0")
    print("Algorithm Status: Active" if ALGORITHM_AVAILABLE else "Algorithm Status: Not Available")
    print("Server running at: http://localhost:8000")
    print("Dashboard: http://localhost:8000")
    print("API Health: http://localhost:8000/api/v1/health")
    print("System Info: http://localhost:8000/api/v1/system-info")
    print("Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Run Flask app
    app.run(host='0.0.0.0', port=8000, debug=False)

if __name__ == "__main__":
    main() 