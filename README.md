# AML Transaction Monitoring & Alert Investigation Analytics

**AML / Financial Crime Analytics Portfolio Project**

An end-to-end AML transaction-monitoring and alert-investigation project
using **Python, SQL, Tableau, and Streamlit** to analyze customer
behavior, transaction patterns, monitoring alerts, risk scores,
dispositions, and investigation-prioritization decisions.

> **Portfolio scope:** This project uses synthetic data created for
> educational and portfolio purposes. Monitoring scenarios, risk scores,
> thresholds, dispositions, and recommendations are illustrative and do
> not represent any financial institution's production AML program.

------------------------------------------------------------------------

## Project Overview

Transaction-monitoring teams must combine customer KYC context with
transaction behavior, monitoring scenarios, alert risk, counterparties,
geographic exposure, and prior activity before deciding whether an alert
can be closed or requires escalation.

This project demonstrates that workflow across:

-   **300 synthetic customers**
-   **15,000 transactions**
-   **169 AML alerts**
-   **300 customer-level AML risk records**
-   A feature-engineered transaction layer containing behavioral and
    monitoring indicators

The analytical workflow moves from customer and transaction data through
EDA, feature engineering, monitoring alerts, investigation review, and
decision support.

------------------------------------------------------------------------

## Business & Investigation Questions

-   Which customers and alerts should investigators prioritize first?
-   Which monitoring scenarios generate the most alerts?
-   Which alerts carry the highest AML risk scores?
-   Which customers show unusual transaction volume relative to expected
    activity?
-   Which customers have elevated cross-border or high-risk-country
    exposure?
-   Which alerts were escalated to cases or SAR consideration?
-   Which counterparties and jurisdictions contribute to elevated risk?
-   How can customer-level AML risk and transaction behavior support
    alert disposition?
-   Which patterns may indicate structuring, high-risk wires, unusual
    volume, or rapid movement of funds?

------------------------------------------------------------------------

## Data Model

  ------------------------------------------------------------------------------------
  Dataset                                                Rows Purpose
  ------------------------------ ---------------------------- ------------------------
  Customer reference                                      300 KYC profile and baseline
                                                              AML context

  Raw transactions                                     15,000 Transaction-monitoring
                                                              and behavior analysis

  `alerts.csv`                                            169 AML alerts and
                                                              investigation outcomes

  `customer_risk_features.csv`                            300 Customer-level AML risk
                                                              and behavioral features

  `transactions_enriched.csv`                          15,000 Analytics-ready
                                                              transaction layer
  ------------------------------------------------------------------------------------

See [`docs/data_dictionary.md`](docs/data_dictionary.md) for field
definitions and dataset relationships.

------------------------------------------------------------------------

## Exploratory Data Analysis & Data Quality

The notebook includes a practical AML-focused EDA workflow:

-   Dataset/schema review
-   Missing-value analysis
-   Duplicate validation
-   Datatype and range checks
-   Summary statistics
-   IQR-based outlier review
-   KPI and business-rule validation
-   Transaction-channel review
-   Geographic-risk review
-   Alert-scenario analysis
-   Final dataset validation

Potentially unusual or extreme transactions are **flagged for
investigation rather than automatically removed**, because outliers may
represent meaningful AML activity.

------------------------------------------------------------------------

## Feature Engineering

The customer risk layer contains explainable AML features including:

-   `total_transactions`
-   `total_volume`
-   `avg_transaction_amount`
-   `max_transaction_amount`
-   `cross_border_ratio`
-   `high_risk_country_ratio`
-   `cash_ratio`
-   `wire_ratio`
-   `unique_counterparties`
-   `max_expected_ratio`
-   `risk_score`
-   `risk_level`

The notebook additionally demonstrates:

-   `high_risk_country_flag`
-   `structuring_amount_flag`
-   `amount_band`
-   `high_customer_risk_flag`

These features are intentionally simple and interpretable so they can be
clearly explained during an AML or Financial Crime Analytics interview.

------------------------------------------------------------------------

## AML Transaction Monitoring Analysis

The project demonstrates:

**Customer profile review** --- KYC risk, PEP status, expected monthly
activity, occupation/industry, and account context.

**Transaction behavior analysis** --- transaction volume, channel,
direction, counterparties, cross-border behavior, cash/wire activity,
and high-risk jurisdictions.

**Monitoring scenarios** --- alert analysis across unusual volume,
high-risk wires, structuring-like activity, rapid movement, and related
scenarios.

**Alert prioritization** --- ranking alerts by risk score and alert
amount.

**Investigation decision support** --- combining alert history with
customer AML risk, expected activity, cross-border behavior, prior
escalation, and PEP status.

------------------------------------------------------------------------

## SQL Analysis

The SQL file contains **12 analytical queries/statements** supporting
customer risk analysis, transaction-monitoring patterns, scenario
review, alert prioritization, geographic exposure, customer behavior,
and investigation workflow analysis.

See [`sql/`](sql/) for the complete SQL analysis.

------------------------------------------------------------------------

## Verified Current KPIs

  KPI                                        Current Result
  --------------------------------------- -----------------
  Total Customers                                   **300**
  Total Transactions                             **15,000**
  Total AML Alerts                                  **169**
  Alerted Customers                                  **68**
  High-Risk Alerts (score ≥80)              **115 (68.0%)**
  Escalation / SAR-Consideration Alerts      **53 (31.4%)**
  SAR-Consideration Alerts                           **11**
  Alerted Amount                                 **\$9.5M**
  Average Alert Risk Score                         **87.5**

------------------------------------------------------------------------

## Key Findings

-   The portfolio contains **169 AML alerts across 68 alerted
    customers**.
-   **115 alerts (68.0%)** have risk scores of 80 or above.
-   **53 alerts (31.4%)** are marked for case escalation or SAR
    consideration.
-   **11 alerts** specifically reached SAR consideration.
-   The largest alert scenario is **Unusual Volume Spike (90 alerts)**.
-   Total alerted transaction activity is approximately **\$9.5M**.
-   The customer-risk layer is dominated by **Moderate risk (190
    customers)**, with higher-risk customers isolated for focused
    investigation.

These findings support investigation prioritization and analyst review;
they do not automate SAR filing or regulatory decisions.

------------------------------------------------------------------------

## Streamlit AML Investigator Workbench

The Streamlit application provides an interactive investigation
environment.

### Filters

-   Scenario
-   Disposition
-   Minimum Alert Risk Score

### Portfolio Decision Support

The application classifies the selected alert population as:

-   **Routine Monitoring**
-   **Targeted Investigation Required**
-   **Heightened AML Risk**

The decision logic considers High-Risk alert concentration and the share
of alerts already at case-escalation or SAR-consideration stage.

### Customer Investigation Summary

For a selected customer, the application combines:

-   KYC risk
-   AML risk score and level
-   PEP status
-   Expected monthly volume
-   Observed transaction volume
-   Cross-border ratio
-   Unique counterparties
-   Alert history
-   High-risk alerts
-   Prior escalations

It then produces an explainable recommendation:

-   **Escalate for Further Investigation**
-   **Enhanced Review Required**
-   **Targeted AML Review**
-   **Close / Continue Routine Monitoring**

The recommendation is clearly presented as analyst decision support
rather than an automated SAR-filing decision.

### Interactive Tabs

-   Risk-Ranked Alert Queue
-   Customer 360
-   Portfolio Analytics
-   Tableau Gallery

The **Tableau Gallery already follows the preferred portfolio structure
and displays only the Executive Dashboard**.

------------------------------------------------------------------------

## Tableau Executive Dashboard

The executive dashboard is synchronized to the current processed datasets and presents:

1. Alerts Over Time
2. Alerts by Scenario
3. Top 5 Countries by Alerted Amount
4. Customer Risk Distribution
5. Top 5 Alerted Customers
6. Alert Disposition

### Dashboard Preview

![AML Transaction Monitoring & Alert Investigation Dashboard](images/02_executive_dashboard.png)

**Dashboard KPI reconciliation:** 300 customers, 15,000 transactions, 169 alerts, 115 high-risk alerts, 68 alerted customers, and approximately $9.5M in alerted amount. Alert dispositions reconcile to 62 Close - No Suspicion, 54 Pending, 42 Escalate to Case, and 11 SAR Consideration.

> This dashboard uses synthetic portfolio data for educational and demonstration purposes.

------------------------------------------------------------------------

## Analytical Workflow

``` text
Customer Profile
       ↓
Raw Transactions
       ↓
EDA & Data Quality Validation
       ↓
Feature Engineering
       ↓
Enriched Transactions
       ↓
Transaction-Monitoring Alerts
       ↓
Alert Investigation & Customer Risk Review
       ↓
Escalation / Closure Decision Support
       ↓
Tableau + Streamlit Reporting
```

------------------------------------------------------------------------

## Tools & Technologies

  -----------------------------------------------------------------------
  Tool                                Use
  ----------------------------------- -----------------------------------
  **Python / Pandas**                 EDA, feature engineering,
                                      customer-risk and alert analysis

  **SQL**                             Transaction monitoring, scenarios,
                                      alert and customer analysis

  **Tableau**                         Executive AML dashboard

  **Streamlit**                       Investigator workbench and decision
                                      support

  **Jupyter Notebook**                Reproducible analytical workflow

  **Git / GitHub**                    Version control and portfolio
                                      presentation
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Repository Structure

``` text
Transaction-Monitoring/
├── app/             # Streamlit investigator workbench
├── data/            # Synthetic raw and processed datasets
├── docs/            # Data dictionary and supporting documentation
├── images/          # Executive dashboard
├── notebooks/       # EDA and feature engineering
├── sql/             # AML analytical queries
├── src/             # Supporting analytical logic
├── tableau/         # Tableau workbook
├── .gitignore
├── .python-version
├── main.py
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

------------------------------------------------------------------------

## How to Run

``` bash
git clone https://github.com/Denis0242/Transaction-Monitoring.git
cd Transaction-Monitoring
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

------------------------------------------------------------------------

## Skills Demonstrated

### AML / Financial Crime

-   Transaction Monitoring
-   AML Alert Investigation
-   Alert Triage & Prioritization
-   Customer Risk Assessment
-   KYC Context Review
-   PEP Risk Review
-   Structuring Analysis
-   High-Risk Wire Analysis
-   Cross-Border Risk
-   High-Risk Jurisdiction Analysis
-   Counterparty Review
-   Alert Escalation
-   SAR-Consideration Analysis
-   Investigation Documentation

### Data & Analytics

-   Exploratory Data Analysis
-   Feature Engineering
-   Data Quality Validation
-   SQL
-   Python / Pandas
-   Risk Scoring
-   KPI Development
-   Trend Analysis
-   Behavioral Analysis
-   Business-Rule Validation

### Visualization & Decision Support

-   Tableau
-   Streamlit
-   Alert Queues
-   Customer 360
-   Executive Dashboards
-   Interactive Filtering
-   Investigation Storytelling

------------------------------------------------------------------------

## Disclaimer

This project uses **synthetic data** created for educational and
portfolio purposes. No real customer, transaction, account, AML alert,
SAR, bank, or confidential financial-institution information is
included.

Monitoring scenarios, thresholds, risk scores, dispositions, engineered
features, alert-prioritization logic, and decision-support
recommendations are illustrative. They should not be interpreted as
actual financial-institution policy, regulatory filing determinations,
or production transaction-monitoring rules.
