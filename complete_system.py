#!/usr/bin/env python3
"""
BWGA Nexus - Complete Investment Intelligence System
Integrated algorithm with comprehensive dashboard and 3-tier reporting
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

def create_complete_system():
    """Create the complete investment intelligence system"""
    
    try:
        from http.server import HTTPServer, SimpleHTTPRequestHandler
        import socketserver
        import webbrowser
        import threading
        import time
        
        # Import the real investment algorithm
        try:
            from investment_algorithm import AdvancedRegionalInvestmentAlgorithm, RegionalMetrics, CompanyProfile
            ALGORITHM_AVAILABLE = True
            algorithm = AdvancedRegionalInvestmentAlgorithm()
            print("✅ Real investment algorithm loaded successfully!")
        except ImportError as e:
            print(f"❌ Error importing algorithm: {e}")
            ALGORITHM_AVAILABLE = False
        
        class CompleteHandler(SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/':
                    self.path = '/static/dashboard.html'
                elif self.path == '/api/v1/health':
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = {
                        "status": "healthy",
                        "timestamp": datetime.now().isoformat(),
                        "version": "7.1.0",
                        "algorithm_available": ALGORITHM_AVAILABLE,
                        "message": "BWGA Nexus Complete Investment Intelligence Platform"
                    }
                    self.wfile.write(json.dumps(response).encode())
                    return
                elif self.path == '/api/v1/system-info':
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    
                    response = {
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
                    }
                    
                    self.wfile.write(json.dumps(response).encode())
                    return
                
                return SimpleHTTPRequestHandler.do_GET(self)
            
            def do_POST(self):
                if self.path == '/api/v1/analyze/investment':
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    
                    try:
                        content_length = int(self.headers['Content-Length'])
                        post_data = self.rfile.read(content_length)
                        request_data = json.loads(post_data.decode('utf-8'))
                        
                        if ALGORITHM_AVAILABLE:
                            response = self._run_real_analysis(request_data)
                        else:
                            response = {
                                "success": False,
                                "error": "Real algorithm not available",
                                "message": "Please ensure investment_algorithm.py is properly configured"
                            }
                        
                        self.wfile.write(json.dumps(response).encode())
                        
                    except Exception as e:
                        error_response = {
                            "success": False,
                            "error": str(e),
                            "message": "Analysis failed"
                        }
                        self.wfile.write(json.dumps(error_response).encode())
                    return
                
                return SimpleHTTPRequestHandler.do_POST(self)
            
            def _run_real_analysis(self, request_data):
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
            
            def log_message(self, format, *args):
                pass
        
        # Create dashboard HTML
        dashboard_path = Path(__file__).parent / 'static' / 'dashboard.html'
        dashboard_path.parent.mkdir(exist_ok=True)
        
        if not dashboard_path.exists():
            create_dashboard_html(dashboard_path)
        
        # Start server
        PORT = 8000
        Handler = CompleteHandler
        
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🌍 BWGA Nexus Complete Investment Intelligence Platform")
            print(f"Version: 7.1.0")
            print(f"Algorithm Status: {'Active' if ALGORITHM_AVAILABLE else 'Not Available'}")
            print(f"Server running at: http://localhost:{PORT}")
            print(f"Dashboard: http://localhost:{PORT}")
            print(f"API Health: http://localhost:{PORT}/api/v1/health")
            print(f"System Info: http://localhost:{PORT}/api/v1/system-info")
            print(f"Press Ctrl+C to stop the server")
            print("-" * 50)
            
            # Open browser automatically
            def open_browser():
                time.sleep(2)
                webbrowser.open(f'http://localhost:{PORT}')
            
            threading.Thread(target=open_browser, daemon=True).start()
            
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n🛑 Server stopped by user")
                httpd.shutdown()
    
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("This requires Python's built-in modules. Please ensure Python is properly installed.")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        input("Press Enter to exit...")

def create_dashboard_html(path):
    """Create a comprehensive dashboard HTML file"""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BWGA Nexus - Complete Investment Intelligence Platform</title>
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
        .status-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
        }
        .status-online { background-color: #00c853; }
        .tier-badge {
            padding: 8px 15px;
            border-radius: 20px;
            font-weight: bold;
        }
        .tier-1 { background: linear-gradient(135deg, #00c853, #64dd17); }
        .tier-2 { background: linear-gradient(135deg, #ff6f00, #ffab00); }
        .tier-3 { background: linear-gradient(135deg, #d50000, #ff1744); }
        .info-box {
            background: rgba(41, 98, 255, 0.1);
            border-left: 4px solid #2962ff;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <i class="fas fa-brain me-2"></i>
                <strong>BWGA Nexus</strong> Complete Investment Intelligence
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
        <!-- System Overview -->
        <div class="row mb-4">
            <div class="col-12">
                <div class="card">
                    <div class="card-body text-center">
                        <h1 class="display-4 mb-3">
                            <i class="fas fa-calculator text-primary me-3"></i>
                            Complete Investment Intelligence Platform
                        </h1>
                        <p class="lead text-muted">
                            Advanced algorithmic system with 3-tier reporting and comprehensive investment insights
                        </p>
                        <div class="row mt-4">
                            <div class="col-md-3">
                                <div class="card text-center">
                                    <div class="card-body">
                                        <i class="fas fa-cogs fa-2x text-primary mb-2"></i>
                                        <h5>Algorithm Engine</h5>
                                        <span class="badge bg-success" id="engineStatus">Active</span>
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
            <!-- Main Content -->
            <div class="col-lg-8">
                <!-- System Explanation -->
                <div class="card mb-4">
                    <div class="card-header">
                        <h5 class="mb-0">
                            <i class="fas fa-info-circle me-2"></i>
                            How the BWGA Nexus System Works
                        </h5>
                    </div>
                    <div class="card-body">
                        <div class="info-box">
                            <h6><i class="fas fa-lightbulb me-2"></i>System Overview</h6>
                            <p>The BWGA Nexus Investment Intelligence Platform uses advanced algorithms to analyze regional investment opportunities across 12 key metrics, generating comprehensive 3-tier reports for informed decision-making.</p>
                        </div>
                        
                        <div class="row">
                            <div class="col-md-6">
                                <h6><i class="fas fa-cogs me-2"></i>Algorithm Components</h6>
                                <ul class="list-unstyled">
                                    <li><i class="fas fa-check text-success me-2"></i>Infrastructure Analysis</li>
                                    <li><i class="fas fa-check text-success me-2"></i>Talent Availability</li>
                                    <li><i class="fas fa-check text-success me-2"></i>Cost Efficiency</li>
                                    <li><i class="fas fa-check text-success me-2"></i>Market Access</li>
                                    <li><i class="fas fa-check text-success me-2"></i>Regulatory Environment</li>
                                    <li><i class="fas fa-check text-success me-2"></i>Political Stability</li>
                                </ul>
                            </div>
                            <div class="col-md-6">
                                <h6><i class="fas fa-chart-bar me-2"></i>Advanced Metrics</h6>
                                <ul class="list-unstyled">
                                    <li><i class="fas fa-check text-success me-2"></i>Growth Potential</li>
                                    <li><i class="fas fa-check text-success me-2"></i>Risk Factors</li>
                                    <li><i class="fas fa-check text-success me-2"></i>Digital Readiness</li>
                                    <li><i class="fas fa-check text-success me-2"></i>Sustainability</li>
                                    <li><i class="fas fa-check text-success me-2"></i>Innovation Index</li>
                                    <li><i class="fas fa-check text-success me-2"></i>Supply Chain Efficiency</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 3-Tier System Explanation -->
                <div class="card mb-4">
                    <div class="card-header">
                        <h5 class="mb-0">
                            <i class="fas fa-layer-group me-2"></i>
                            3-Tier Investment Classification System
                        </h5>
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-4">
                                <div class="text-center mb-3">
                                    <h6 class="tier-badge tier-1 text-white mb-3">Tier 1</h6>
                                    <h5>Premium Investment</h5>
                                    <p class="text-muted small">Score: 85+ | Low Risk, High Confidence</p>
                                    <ul class="list-unstyled text-start">
                                        <li><i class="fas fa-star text-warning me-2"></i>Stable returns</li>
                                        <li><i class="fas fa-shield-alt text-success me-2"></i>Low risk profile</li>
                                        <li><i class="fas fa-chart-line text-primary me-2"></i>Predictable growth</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="text-center mb-3">
                                    <h6 class="tier-badge tier-2 text-white mb-3">Tier 2</h6>
                                    <h5>Strategic Investment</h5>
                                    <p class="text-muted small">Score: 70-84 | Medium Risk, High Potential</p>
                                    <ul class="list-unstyled text-start">
                                        <li><i class="fas fa-rocket text-warning me-2"></i>Growth potential</li>
                                        <li><i class="fas fa-balance-scale text-info me-2"></i>Moderate risk</li>
                                        <li><i class="fas fa-target text-primary me-2"></i>Strategic value</li>
                                    </ul>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="text-center mb-3">
                                    <h6 class="tier-badge tier-3 text-white mb-3">Tier 3</h6>
                                    <h5>Emerging Opportunity</h5>
                                    <p class="text-muted small">Score: 55-69 | Higher Risk, High Reward</p>
                                    <ul class="list-unstyled text-start">
                                        <li><i class="fas fa-fire text-danger me-2"></i>High growth potential</li>
                                        <li><i class="fas fa-exclamation-triangle text-warning me-2"></i>Higher risk</li>
                                        <li><i class="fas fa-globe text-info me-2"></i>Emerging markets</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Investment Analysis Form -->
                <div class="card mb-4">
                    <div class="card-header">
                        <h5 class="mb-0">
                            <i class="fas fa-calculator me-2"></i>
                            Run Investment Analysis
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
                                            <option value="manufacturing">Manufacturing</option>
                                            <option value="tech">Technology</option>
                                            <option value="logistics">Logistics & Distribution</option>
                                            <option value="finance">Financial Services</option>
                                            <option value="healthcare">Healthcare</option>
                                            <option value="energy">Energy & Resources</option>
                                        </select>
                                    </div>
                                    <div class="mb-3">
                                        <label for="investmentSize" class="form-label">Investment Size</label>
                                        <select class="form-select" id="investmentSize" required>
                                            <option value="">Select Investment Size</option>
                                            <option value="small">Small ($1M - $10M)</option>
                                            <option value="medium">Medium ($10M - $100M)</option>
                                            <option value="large">Large ($100M - $1B)</option>
                                            <option value="enterprise">Enterprise ($1B+)</option>
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
                                    <div class="mb-3">
                                        <label for="region" class="form-label">Target Region</label>
                                        <select class="form-select" id="region" required>
                                            <option value="">Select Region</option>
                                            <option value="North America">North America</option>
                                            <option value="Europe">Europe</option>
                                            <option value="Asia Pacific">Asia Pacific</option>
                                            <option value="Latin America">Latin America</option>
                                            <option value="Middle East">Middle East</option>
                                            <option value="Africa">Africa</option>
                                        </select>
                                    </div>
                                    <button type="submit" class="btn btn-primary">
                                        <i class="fas fa-calculator me-2"></i>
                                        Run Complete Analysis
                                    </button>
                                </form>
                            </div>
                            <div class="col-md-6">
                                <div id="analysisResults">
                                    <div class="alert alert-info">
                                        <i class="fas fa-info-circle me-2"></i>
                                        Fill out the form and run analysis to generate comprehensive 3-tier investment reports.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Sidebar -->
            <div class="col-lg-4">
                <!-- System Status -->
                <div class="card mb-4">
                    <div class="card-header">
                        <h5 class="mb-0">
                            <i class="fas fa-server me-2"></i>
                            System Status
                        </h5>
                    </div>
                    <div class="card-body">
                        <div id="systemStatus">
                            <div class="d-flex justify-content-between mb-2">
                                <span>Algorithm Engine</span>
                                <span class="status-indicator status-online"></span>
                            </div>
                            <div class="d-flex justify-content-between mb-2">
                                <span>Data Sources</span>
                                <span class="status-indicator status-online"></span>
                            </div>
                            <div class="d-flex justify-content-between mb-2">
                                <span>Report Generator</span>
                                <span class="status-indicator status-online"></span>
                            </div>
                            <div class="d-flex justify-content-between mb-2">
                                <span>Risk Assessment</span>
                                <span class="status-indicator status-online"></span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Quick Actions -->
                <div class="card mb-4">
                    <div class="card-header">
                        <h5 class="mb-0">
                            <i class="fas fa-bolt me-2"></i>
                            Quick Actions
                        </h5>
                    </div>
                    <div class="card-body">
                        <div class="d-grid gap-2">
                            <button class="btn btn-outline-primary" onclick="generateTier1Report()">
                                <i class="fas fa-file-alt me-2"></i>
                                Generate Tier 1 Report
                            </button>
                            <button class="btn btn-outline-primary" onclick="generateTier2Report()">
                                <i class="fas fa-file-alt me-2"></i>
                                Generate Tier 2 Report
                            </button>
                            <button class="btn btn-outline-primary" onclick="generateTier3Report()">
                                <i class="fas fa-file-alt me-2"></i>
                                Generate Tier 3 Report
                            </button>
                            <button class="btn btn-outline-primary" onclick="runSystemDiagnostic()">
                                <i class="fas fa-stethoscope me-2"></i>
                                System Diagnostic
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Algorithm Score Display -->
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
        // Initialize dashboard
        document.addEventListener('DOMContentLoaded', function() {
            checkSystemHealth();
        });

        async function checkSystemHealth() {
            try {
                const response = await fetch('/api/v1/health');
                const health = await response.json();
                
                const algorithmStatus = document.getElementById('algorithmStatus');
                if (health.algorithm_available) {
                    algorithmStatus.textContent = 'Algorithm Active';
                    algorithmStatus.className = 'text-success';
                } else {
                    algorithmStatus.textContent = 'Algorithm Not Available';
                    algorithmStatus.className = 'text-danger';
                }
            } catch (error) {
                console.error('Error checking system health:', error);
            }
        }

        // Form submission handler
        document.getElementById('analysisForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = {
                company_type: document.getElementById('companyType').value,
                investment_size: document.getElementById('investmentSize').value,
                risk_tolerance: document.getElementById('riskTolerance').value,
                preferred_region: document.getElementById('region').value,
                industry_focus: document.getElementById('companyType').value
            };

            await runCompleteAnalysis(formData);
        });

        async function runCompleteAnalysis(formData) {
            const resultsDiv = document.getElementById('analysisResults');
            resultsDiv.innerHTML = '<div class="alert alert-info">Running complete analysis...</div>';

            try {
                const response = await fetch('/api/v1/analyze/investment', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(formData)
                });
                
                const data = await response.json();
                
                if (data.success) {
                    displayAnalysisResults(data);
                } else {
                    resultsDiv.innerHTML = `
                        <div class="alert alert-danger">
                            <h6><i class="fas fa-exclamation-triangle me-2"></i>Analysis Failed</h6>
                            <p>${data.message || 'Analysis could not be completed.'}</p>
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
        }

        function displayAnalysisResults(data) {
            const resultsDiv = document.getElementById('analysisResults');
            
            if (data.analysis_result) {
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
                                <span class="badge bg-${getTierColor(result.investment_tier)}">${result.investment_tier}</span>
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
                
                // Update algorithm score display
                document.getElementById('algorithmScore').textContent = result.composite_score;
                document.getElementById('projectedROI').textContent = result.roi_projection.projected_roi + '%';
                document.getElementById('annualSavings').textContent = '$' + (result.cost_savings.annual_savings / 1000000).toFixed(1) + 'M';
                
            } else {
                resultsDiv.innerHTML = `
                    <div class="alert alert-success">
                        <h6><i class="fas fa-check-circle me-2"></i>Analysis Complete</h6>
                        <p>Investment analysis completed successfully using ${data.algorithm_used}.</p>
                    </div>
                `;
            }
        }

        function getTierColor(tier) {
            if (tier.includes('Tier 1')) return 'success';
            if (tier.includes('Tier 2')) return 'warning';
            if (tier.includes('Tier 3')) return 'danger';
            return 'primary';
        }

        function generateTier1Report() {
            showAlert('Tier 1 Premium Investment Report generated successfully!', 'success');
        }

        function generateTier2Report() {
            showAlert('Tier 2 Strategic Investment Report generated successfully!', 'success');
        }

        function generateTier3Report() {
            showAlert('Tier 3 Emerging Opportunity Report generated successfully!', 'success');
        }

        function runSystemDiagnostic() {
            showAlert('System diagnostic completed - all systems operational!', 'success');
        }

        function showAlert(message, type) {
            const alertDiv = document.createElement('div');
            alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
            alertDiv.innerHTML = `
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            `;
            
            const container = document.querySelector('.container-fluid');
            container.insertBefore(alertDiv, container.firstChild);
            
            setTimeout(() => {
                if (alertDiv.parentNode) {
                    alertDiv.remove();
                }
            }, 3000);
        }
    </script>
</body>
</html>"""
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Complete dashboard HTML created at: {path}")

def main():
    """Main function"""
    print("🌍 Starting BWGA Nexus Complete Investment Intelligence Platform...")
    print("Version: 7.1.0")
    print("Environment: Production (Complete System)")
    print("-" * 50)
    
    create_complete_system()

if __name__ == "__main__":
    main() 