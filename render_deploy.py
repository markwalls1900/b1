#!/usr/bin/env python3
"""
BWGA Nexus - Render.com Deployment Script
Free hosting for seed capital presentation
"""

import os
import json
from pathlib import Path

def create_render_files():
    """Create files needed for Render.com deployment"""
    
    # Create requirements.txt for Render
    requirements = """Flask==2.3.3
numpy==1.24.3
gunicorn==21.2.0
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    
    # Create render.yaml for easy deployment
    render_yaml = """services:
  - type: web
    name: bwga-nexus
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
"""
    
    with open('render.yaml', 'w') as f:
        f.write(render_yaml)
    
    # Create app.py for Flask deployment
    app_py = '''#!/usr/bin/env python3
"""
BWGA Nexus - Flask App for Render.com Deployment
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory
import threading
import time

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

app = Flask(__name__)

# Import the real investment algorithm
try:
    from investment_algorithm import AdvancedRegionalInvestmentAlgorithm, RegionalMetrics, CompanyProfile
    ALGORITHM_AVAILABLE = True
    algorithm = AdvancedRegionalInvestmentAlgorithm()
    print("✅ Real investment algorithm loaded successfully!")
except ImportError as e:
    print(f"❌ Error importing algorithm: {e}")
    ALGORITHM_AVAILABLE = False

@app.route('/')
def dashboard():
    """Serve the main dashboard"""
    return send_from_directory('static', 'dashboard.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files"""
    return send_from_directory('static', filename)

@app.route('/api/v1/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "7.1.0",
        "algorithm_available": ALGORITHM_AVAILABLE,
        "message": "BWGA Nexus Investment Intelligence Platform is running!"
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
        ],
        "tier_system": {
            "tier_1": {
                "name": "Premium Investment",
                "description": "High-confidence, low-risk opportunities",
                "threshold": "85+ score"
            },
            "tier_2": {
                "name": "Strategic Investment",
                "description": "Medium-risk, high-potential opportunities", 
                "threshold": "70-84 score"
            },
            "tier_3": {
                "name": "Emerging Opportunity",
                "description": "High-risk, high-reward emerging markets",
                "threshold": "55-69 score"
            }
        }
    })

@app.route('/api/v1/analyze/investment', methods=['POST'])
def analyze_investment():
    """Investment analysis endpoint"""
    try:
        request_data = request.get_json()
        
        if ALGORITHM_AVAILABLE:
            response = run_real_analysis(request_data)
        else:
            response = {
                "success": False,
                "error": "Real algorithm not available",
                "message": "Please ensure investment_algorithm.py is properly configured"
            }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Analysis failed"
        })

def run_real_analysis(request_data):
    """Run real algorithm analysis"""
    try:
        # Create regional data with all required parameters
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
            # Additional required parameters
            digital_infrastructure=request_data.get('digital_infrastructure', 0.90),
            supply_chain_efficiency=request_data.get('supply_chain_efficiency', 0.75),
            innovation_index=request_data.get('innovation_index', 0.85),
            sustainability_score=request_data.get('sustainability_score', 0.70),
            geopolitical_risk=request_data.get('geopolitical_risk', 0.20),
            market_volatility=request_data.get('market_volatility', 0.35)
        )
        
        # Create company profile with all required parameters
        company_profile = CompanyProfile(
            company_type=request_data.get('company_type', 'tech'),
            investment_size=request_data.get('investment_size', 'large'),
            preferred_region=request_data.get('preferred_region', 'North America'),
            industry_focus=request_data.get('industry_focus', 'technology'),
            risk_tolerance=request_data.get('risk_tolerance', 'medium'),
            timeline=request_data.get('timeline', '3-5 years'),
            technology_requirements=request_data.get('technology_requirements', ['AI/ML', 'Cloud']),
            supply_chain_needs=request_data.get('supply_chain_needs', ['Semiconductors']),
            # Additional required parameters
            sustainability_goals=request_data.get('sustainability_goals', ['Carbon neutral', 'Renewable energy']),
            digital_transformation_needs=request_data.get('digital_transformation_needs', ['Automation', 'Data analytics']),
            market_expansion_targets=request_data.get('market_expansion_targets', ['Enterprise', 'SMB']),
            competitive_advantages=request_data.get('competitive_advantages', ['Technology leadership', 'Cost efficiency'])
        )
        
        # Run algorithm
        result = algorithm.calculate_investment_score(regional_data, company_profile)
        
        return {
            "success": True,
            "analysis_result": result,
            "algorithm_used": "Real BWGA Nexus Algorithm",
            "analysis_timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Real algorithm analysis failed"
        }

if __name__ == '__main__':
    # Create static directory and dashboard if it doesn't exist
    static_dir = Path('static')
    static_dir.mkdir(exist_ok=True)
    
    dashboard_path = static_dir / 'dashboard.html'
    if not dashboard_path.exists():
        create_dashboard_html(dashboard_path)
    
    print("🌍 BWGA Nexus Investment Intelligence Platform")
    print("Version: 7.1.0")
    print("Environment: Production (Render.com)")
    print("Algorithm Status: Active" if ALGORITHM_AVAILABLE else "Not Available")
    print("-" * 50)
    
    # Run Flask app
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)

def create_dashboard_html(path):
    """Create the dashboard HTML file"""
    # This would be the same HTML content as before
    # For brevity, I'll create a simplified version
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BWGA Nexus - Investment Intelligence Platform</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            min-height: 100vh;
        }
        .navbar {
            background: rgba(26, 35, 126, 0.95) !important;
            backdrop-filter: blur(10px);
        }
        .card {
            background: #1a1a1a;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        .card-header {
            background: linear-gradient(135deg, #1a237e, #0d47a1);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px 15px 0 0 !important;
        }
        .btn-primary {
            background: linear-gradient(135deg, #1a237e, #0d47a1);
            border: none;
            border-radius: 25px;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <i class="fas fa-brain me-2"></i>
                <strong>BWGA Nexus</strong> Investment Intelligence
            </a>
            <div class="navbar-nav ms-auto">
                <span class="navbar-text me-3">
                    <span class="status-indicator status-online"></span>
                    <span id="algorithmStatus">Algorithm Active</span>
                </span>
                <span class="navbar-text">v7.1.0</span>
            </div>
        </div>
    </nav>

    <div class="container-fluid mt-4">
        <div class="row mb-4">
            <div class="col-12">
                <div class="card">
                    <div class="card-body text-center">
                        <h1 class="display-4 mb-3">
                            <i class="fas fa-calculator text-primary me-3"></i>
                            BWGA Nexus Investment Intelligence Platform
                        </h1>
                        <p class="lead text-muted">
                            Advanced algorithmic system with 3-tier reporting for seed capital investment analysis
                        </p>
                        <div class="row mt-4">
                            <div class="col-md-3">
                                <div class="card text-center">
                                    <div class="card-body">
                                        <i class="fas fa-cogs fa-2x text-primary mb-2"></i>
                                        <h5>Algorithm Engine</h5>
                                        <span class="badge bg-success">Active</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="card text-center">
                                    <div class="card-body">
                                        <i class="fas fa-file-alt fa-2x text-primary mb-2"></i>
                                        <h5>3-Tier Reports</h5>
                                        <span class="badge bg-success">AI Generated</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="card text-center">
                                    <div class="card-body">
                                        <i class="fas fa-chart-line fa-2x text-primary mb-2"></i>
                                        <h5>Real-time Analysis</h5>
                                        <span class="badge bg-success">Live</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="card text-center">
                                    <div class="card-body">
                                        <i class="fas fa-shield-alt fa-2x text-primary mb-2"></i>
                                        <h5>Risk Assessment</h5>
                                        <span class="badge bg-success">Comprehensive</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-lg-8">
                <div class="card mb-4">
                    <div class="card-header">
                        <h5 class="mb-0">
                            <i class="fas fa-calculator me-2"></i>
                            Investment Analysis for Seed Capital
                        </h5>
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-6">
                                <form id="analysisForm">
                                    <div class="mb-3">
                                        <label for="companyType" class="form-label">Company Type</label>
                                        <select class="form-select" id="companyType" required>
                                            <option value="">Select Company Type</option>
                                            <option value="tech">Technology</option>
                                            <option value="manufacturing">Manufacturing</option>
                                            <option value="finance">Financial Services</option>
                                            <option value="healthcare">Healthcare</option>
                                        </select>
                                    </div>
                                    <div class="mb-3">
                                        <label for="investmentSize" class="form-label">Investment Size</label>
                                        <select class="form-select" id="investmentSize" required>
                                            <option value="">Select Investment Size</option>
                                            <option value="small">Small ($1M - $10M)</option>
                                            <option value="medium">Medium ($10M - $100M)</option>
                                            <option value="large">Large ($100M - $1B)</option>
                                        </select>
                                    </div>
                                    <div class="mb-3">
                                        <label for="riskTolerance" class="form-label">Risk Tolerance</label>
                                        <select class="form-select" id="riskTolerance" required>
                                            <option value="">Select Risk Tolerance</option>
                                            <option value="low">Low Risk</option>
                                            <option value="medium">Medium Risk</option>
                                            <option value="high">High Risk</option>
                                        </select>
                                    </div>
                                    <button type="submit" class="btn btn-primary">
                                        <i class="fas fa-calculator me-2"></i>
                                        Run Investment Analysis
                                    </button>
                                </form>
                            </div>
                            <div class="col-md-6">
                                <div id="analysisResults">
                                    <div class="alert alert-info">
                                        <i class="fas fa-info-circle me-2"></i>
                                        Fill out the form to generate comprehensive investment analysis for seed capital evaluation.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-lg-4">
                <div class="card">
                    <div class="card-header">
                        <h5 class="mb-0">
                            <i class="fas fa-star me-2"></i>
                            Algorithm Performance
                        </h5>
                    </div>
                    <div class="card-body text-center">
                        <div class="h1 text-primary mb-3" id="algorithmScore">--</div>
                        <h6 class="mb-3">Composite Algorithm Score</h6>
                        <div class="row text-center">
                            <div class="col-6">
                                <h5 class="text-success" id="projectedROI">--</h5>
                                <small class="text-muted">Projected ROI</small>
                            </div>
                            <div class="col-6">
                                <h5 class="text-primary" id="annualSavings">--</h5>
                                <small class="text-muted">Annual Savings</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.getElementById('analysisForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = {
                company_type: document.getElementById('companyType').value,
                investment_size: document.getElementById('investmentSize').value,
                risk_tolerance: document.getElementById('riskTolerance').value,
                industry_focus: document.getElementById('companyType').value
            };

            const resultsDiv = document.getElementById('analysisResults');
            resultsDiv.innerHTML = '<div class="alert alert-info">Running analysis...</div>';

            try {
                const response = await fetch('/api/v1/analyze/investment', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(formData)
                });
                
                const data = await response.json();
                
                if (data.success) {
                    const result = data.analysis_result;
                    resultsDiv.innerHTML = `
                        <div class="alert alert-success">
                            <h6><i class="fas fa-check-circle me-2"></i>Analysis Complete</h6>
                            <div class="row mt-3">
                                <div class="col-6">
                                    <h4 class="text-primary">${result.composite_score}</h4>
                                    <small>Composite Score</small>
                                </div>
                                <div class="col-6">
                                    <span class="badge bg-success">${result.investment_tier}</span>
                                    <br><small>Investment Tier</small>
                                </div>
                            </div>
                            <div class="mt-3">
                                <strong>ROI Projection:</strong> ${result.roi_projection.projected_roi}%<br>
                                <strong>Annual Savings:</strong> $${result.cost_savings.annual_savings.toLocaleString()}<br>
                                <strong>Risk Level:</strong> ${result.risk_assessment.risk_level}
                            </div>
                        </div>
                    `;
                    
                    document.getElementById('algorithmScore').textContent = result.composite_score;
                    document.getElementById('projectedROI').textContent = result.roi_projection.projected_roi + '%';
                    document.getElementById('annualSavings').textContent = '$' + (result.cost_savings.annual_savings / 1000000).toFixed(1) + 'M';
                } else {
                    resultsDiv.innerHTML = `
                        <div class="alert alert-danger">
                            <h6><i class="fas fa-exclamation-triangle me-2"></i>Analysis Failed</h6>
                            <p>${data.message}</p>
                        </div>
                    `;
                }
            } catch (error) {
                resultsDiv.innerHTML = `
                    <div class="alert alert-danger">
                        <h6><i class="fas fa-exclamation-triangle me-2"></i>Connection Error</h6>
                        <p>Could not connect to the analysis server.</p>
                    </div>
                `;
            }
        });
    </script>
</body>
</html>"""
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == '__main__':
    create_render_files()
    print("✅ Render.com deployment files created!")
    print("📋 Next steps:")
    print("1. Go to render.com and create a free account")
    print("2. Connect your GitHub repository")
    print("3. Deploy using the render.yaml file")
    print("4. Your app will be live at: https://your-app-name.onrender.com") 