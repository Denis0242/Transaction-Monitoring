
# Tableau Dashboard Guide

## Dashboard 1: AML Monitoring Overview
Recommended KPI cards:
- Total Alerts
- High-Risk Alerts
- Alert Dollar Volume
- Escalation Rate
- SAR Consideration Rate

Recommended visuals:
- Alerts by Scenario
- Monthly Alert Trend
- Risk Score Distribution
- Alerts by Customer Risk Level
- High-Risk Jurisdiction Exposure
- Disposition Breakdown

## Dashboard 2: Investigator Workbench
Recommended visuals:
- Risk-Ranked Alert Queue
- Customer Risk Profile
- Transaction Timeline
- Transaction Channel Mix
- Counterparty Country Exposure
- Prior Alert History
- Top Counterparties
- Disposition / Escalation Summary

Primary Tableau files:
- data/processed/alerts.csv
- data/processed/transactions_enriched.csv
- data/processed/customer_risk_features.csv


## Final Executive Dashboard Design Standard
- White background with compact spacing and closely aligned views.
- KPI cards across the top.
- Alert Trend as the primary time-series view.
- Alert Scenario Mix displayed as a donut chart.
- Cross-Border Exposure limited to the top 3–5 countries and displayed using full country names, not ISO country codes.
- Supporting views: Customer Risk Distribution, Top Alerted Customers, and Alert Disposition.
- Recommended dashboard size: 1400 x 800 or Automatic with fixed horizontal containers.


## Final approved styling
- White dashboard background.
- No executive-dashboard subtitle.
- Borderless KPI scorecards with generous spacing around values.
- Remove unnecessary divider lines, chart borders, and grid lines.
- Keep dashboard objects close together using tiled horizontal/vertical containers.
- Scenario analysis uses a donut chart.
- Cross-border exposure displays the top five full country names.
