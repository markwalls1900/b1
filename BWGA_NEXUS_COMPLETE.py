#!/usr/bin/env python3
"""
BWGA Nexus - Complete Investment Intelligence System (All-in-One Blueprint)
----------------------------------------------------------------------------
This file contains:
- The full advanced investment algorithm (with all metrics, tiers, and logic)
- A Flask web server
- A modern Bootstrap dashboard UI
- Form input for all relevant company/region/market data
- 3-tier report output (with explanations)
- Clear code structure and comments

To run:
    pip install flask
    python BWGA_NEXUS_COMPLETE.py
Then open http://localhost:8000 in your browser.
"""

from flask import Flask, render_template_string, request
from datetime import datetime

app = Flask(__name__)

# ---------------------- Advanced Investment Algorithm ----------------------
class InvestmentTier:
    TIER_1 = "Tier 1 - Premium Investment"
    TIER_2 = "Tier 2 - Strategic Investment"
    TIER_3 = "Tier 3 - Emerging Opportunity"

def advanced_investment_algorithm(data):
    """
    Advanced algorithm for calculating investment score, tier, ROI, and risk.
    Uses multiple weighted metrics and provides detailed output.
    """
    # Extract and normalize input (default values for demo)
    try:
        infra = float(data.get('infrastructure_score', 0.7))
        talent = float(data.get('talent_availability', 0.7))
        cost = float(data.get('cost_of_living', 0.5))
        market = float(data.get('market_access', 0.7))
        risk = float(data.get('risk_factor', 0.5))
        growth = float(data.get('growth_rate', 0.05))
        regulatory = float(data.get('regulatory_ease', 0.7))
        political = float(data.get('political_stability', 0.7))
        digital = float(data.get('digital_infrastructure', 0.7))
        supply_chain = float(data.get('supply_chain_efficiency', 0.7))
        innovation = float(data.get('innovation_index', 0.7))
        sustainability = float(data.get('sustainability_score', 0.7))
        geo_risk = float(data.get('geopolitical_risk', 0.3))
        volatility = float(data.get('market_volatility', 0.4))
    except Exception:
        infra = talent = cost = market = risk = growth = regulatory = political = digital = supply_chain = innovation = sustainability = 0.7
        geo_risk = 0.3
        volatility = 0.4

    # Weighted sum (customize weights as needed)
    score = (
        infra * 0.12 +
        talent * 0.10 +
        (1 - cost) * 0.15 +
        market * 0.12 +
        regulatory * 0.08 +
        political * 0.07 +
        growth * 0.10 * 10 +  # growth_rate is usually 0.01-0.1, scale up
        (1 - risk) * 0.08 +
        digital * 0.06 +
        sustainability * 0.05 +
        innovation * 0.04 +
        supply_chain * 0.03 -
        geo_risk * 0.05 -
        volatility * 0.05
    ) * 100

    # Tier logic
    if score >= 85:
        tier = InvestmentTier.TIER_1
    elif score >= 70:
        tier = InvestmentTier.TIER_2
    else:
        tier = InvestmentTier.TIER_3

    # ROI and risk assessment (demo logic)
    roi = round(8 + (score - 70) * 0.3, 2)
    risk_level = "Low" if score >= 85 else ("Medium" if score >= 70 else "High")

    # Detailed component scores for report
    components = {
        'Infrastructure': infra,
        'Talent Availability': talent,
        'Cost Efficiency': 1 - cost,
        'Market Access': market,
        'Regulatory Ease': regulatory,
        'Political Stability': political,
        'Growth Rate': growth,
        'Risk Factor': 1 - risk,
        'Digital Infrastructure': digital,
        'Sustainability': sustainability,
        'Innovation': innovation,
        'Supply Chain Efficiency': supply_chain,
        'Geopolitical Risk': 1 - geo_risk,
        'Market Volatility': 1 - volatility
    }

    return {
        'score': round(score, 2),
        'tier': tier,
        'roi': roi,
        'risk_level': risk_level,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'components': components
    }

# ---------------------- HTML Dashboard Template ----------------------
DASHBOARD_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BWGA Nexus Investment Intelligence</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body { background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%); color: #fff; }
        .navbar { background: #1a237e; }
        .card { background: #181828; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.3); }
        .card-header { background: linear-gradient(135deg, #1a237e, #0d47a1); color: #fff; border-radius: 16px 16px 0 0; }
        .btn-primary { background: linear-gradient(135deg, #1a237e, #0d47a1); border: none; border-radius: 25px; }
        .tier-badge { font-size: 1.1em; padding: 8px 18px; border-radius: 20px; font-weight: bold; }
        .tier-1 { background: linear-gradient(135deg, #00c853, #64dd17); color: #fff; }
        .tier-2 { background: linear-gradient(135deg, #ff6f00, #ffab00); color: #fff; }
        .tier-3 { background: linear-gradient(135deg, #d50000, #ff1744); color: #fff; }
        .score-table td, .score-table th { color: #fff; }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark mb-4">
  <div class="container-fluid">
    <a class="navbar-brand" href="#"><i class="fas fa-brain me-2"></i>BWGA Nexus Investment Intelligence</a>
    <span class="navbar-text">v7.1.0</span>
  </div>
</nav>
<div class="container">
  <div class="row mb-4">
    <div class="col-12">
      <div class="card">
        <div class="card-header text-center">
          <h2><i class="fas fa-chart-line me-2"></i>Investment Intelligence Dashboard</h2>
          <p class="lead">Advanced 3-Tier Analysis for Seed Capital & Strategic Decisions</p>
        </div>
        <div class="card-body">
          <form method="POST" class="row g-3">
            <div class="col-md-4">
              <label class="form-label">Infrastructure Score (0-1)</label>
              <input type="number" step="0.01" min="0" max="1" name="infrastructure_score" class="form-control" value="{{ formdata.infrastructure_score or 0.7 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Talent Availability (0-1)</label>
              <input type="number" step="0.01" min="0" max="1" name="talent_availability" class="form-control" value="{{ formdata.talent_availability or 0.7 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Cost of Living (0-1, lower is better)</label>
              <input type="number" step="0.01" min="0" max="1" name="cost_of_living" class="form-control" value="{{ formdata.cost_of_living or 0.5 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Market Access (0-1)</label>
              <input type="number" step="0.01" min="0" max="1" name="market_access" class="form-control" value="{{ formdata.market_access or 0.7 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Risk Factor (0-1, lower is better)</label>
              <input type="number" step="0.01" min="0" max="1" name="risk_factor" class="form-control" value="{{ formdata.risk_factor or 0.5 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Growth Rate (0-0.2)</label>
              <input type="number" step="0.001" min="0" max="0.2" name="growth_rate" class="form-control" value="{{ formdata.growth_rate or 0.05 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Regulatory Ease (0-1)</label>
              <input type="number" step="0.01" min="0" max="1" name="regulatory_ease" class="form-control" value="{{ formdata.regulatory_ease or 0.7 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Political Stability (0-1)</label>
              <input type="number" step="0.01" min="0" max="1" name="political_stability" class="form-control" value="{{ formdata.political_stability or 0.7 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Digital Infrastructure (0-1)</label>
              <input type="number" step="0.01" min="0" max="1" name="digital_infrastructure" class="form-control" value="{{ formdata.digital_infrastructure or 0.7 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Supply Chain Efficiency (0-1)</label>
              <input type="number" step="0.01" min="0" max="1" name="supply_chain_efficiency" class="form-control" value="{{ formdata.supply_chain_efficiency or 0.7 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Innovation Index (0-1)</label>
              <input type="number" step="0.01" min="0" max="1" name="innovation_index" class="form-control" value="{{ formdata.innovation_index or 0.7 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Sustainability Score (0-1)</label>
              <input type="number" step="0.01" min="0" max="1" name="sustainability_score" class="form-control" value="{{ formdata.sustainability_score or 0.7 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Geopolitical Risk (0-1, lower is better)</label>
              <input type="number" step="0.01" min="0" max="1" name="geopolitical_risk" class="form-control" value="{{ formdata.geopolitical_risk or 0.3 }}" required>
            </div>
            <div class="col-md-4">
              <label class="form-label">Market Volatility (0-1, lower is better)</label>
              <input type="number" step="0.01" min="0" max="1" name="market_volatility" class="form-control" value="{{ formdata.market_volatility or 0.4 }}" required>
            </div>
            <div class="col-12 text-center mt-3">
              <button type="submit" class="btn btn-primary btn-lg"><i class="fas fa-calculator me-2"></i>Run Analysis</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  {% if result %}
  <div class="row mb-4">
    <div class="col-12">
      <div class="card">
        <div class="card-header text-center">
          <h3>Investment Analysis Result</h3>
        </div>
        <div class="card-body text-center">
          <div class="mb-3">
            <span class="tier-badge tier-1" style="display: {{ 'inline-block' if result.tier.startswith('Tier 1') else 'none' }};">{{ result.tier }}</span>
            <span class="tier-badge tier-2" style="display: {{ 'inline-block' if result.tier.startswith('Tier 2') else 'none' }};">{{ result.tier }}</span>
            <span class="tier-badge tier-3" style="display: {{ 'inline-block' if result.tier.startswith('Tier 3') else 'none' }};">{{ result.tier }}</span>
          </div>
          <h1 class="display-4">Score: {{ result.score }}</h1>
          <h4>Projected ROI: <span class="text-success">{{ result.roi }}%</span></h4>
          <h5>Risk Level: <span class="text-warning">{{ result.risk_level }}</span></h5>
          <p class="mt-3"><strong>Analysis Time:</strong> {{ result.timestamp }}</p>
          <hr>
          <h5>Component Scores</h5>
          <table class="table table-sm score-table">
            <thead><tr><th>Metric</th><th>Score</th></tr></thead>
            <tbody>
            {% for k, v in result.components.items() %}
              <tr><td>{{ k }}</td><td>{{ '%.2f'|format(v*100) }}%</td></tr>
            {% endfor %}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
  {% endif %}
  <div class="row mb-4">
    <div class="col-12">
      <div class="card">
        <div class="card-header"><i class="fas fa-info-circle me-2"></i>About the 3-Tier System</div>
        <div class="card-body">
          <ul>
            <li><b>Tier 1 - Premium Investment:</b> Score 85+, low risk, high confidence, stable returns.</li>
            <li><b>Tier 2 - Strategic Investment:</b> Score 70-84, medium risk, high potential, strategic value.</li>
            <li><b>Tier 3 - Emerging Opportunity:</b> Score below 70, higher risk, high reward, emerging markets.</li>
          </ul>
          <p>This dashboard is a professional demonstration for seed capital and strategic investment decisions. All calculations are transparent and can be customized for your business needs.</p>
        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>
'''

# ---------------------- Flask Routes ----------------------
@app.route('/', methods=['GET', 'POST'])
def dashboard():
    formdata = request.form if request.method == 'POST' else {}
    result = None
    if request.method == 'POST':
        result = advanced_investment_algorithm(formdata)
    return render_template_string(DASHBOARD_HTML, formdata=formdata, result=result)

# ---------------------- Main Entry ----------------------
if __name__ == '__main__':
    print("\n🌍 BWGA Nexus Complete Investment Intelligence System")
    print("Version: 7.1.0 | http://localhost:8000\n")
    app.run(host='0.0.0.0', port=8000, debug=True) 