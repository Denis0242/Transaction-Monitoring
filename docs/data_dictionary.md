# Data Dictionary

## AML Transaction Monitoring & Alert Investigation Analytics

This data dictionary documents the customer, transaction, AML alert, customer-risk-feature, and enriched-transaction datasets used in this portfolio project. It distinguishes source data from engineered and derived analytical features so the project's EDA and feature-engineering work is clearly visible to GitHub reviewers.

> **Portfolio note:** These datasets are structured for analytical demonstration. Definitions describe their use within this project and do not represent any specific financial institution's production data standards or transaction-monitoring system.

## Dataset Overview

| Dataset | Rows | Columns | Purpose |
|---|---:|---:|---|
| `customers(20260914-025808).csv` | 300 | 9 | Customer reference dataset providing profile and baseline AML risk context. |
| `transactions(20260914-025808).csv` | 15,000 | 8 | Raw transaction-level dataset used for transaction-monitoring and behavioral analysis. |
| `alerts(1).csv` | 169 | 9 | AML alert-level dataset containing monitoring alerts and investigation outcomes. |
| `customer_risk_features.csv` | 300 | 16 | Feature-engineered customer dataset containing behavioral and AML risk indicators. |
| `transactions_enriched(1).csv` | 15,000 | 21 | Analytics-ready transaction dataset containing original transaction attributes plus engineered monitoring features. |

## `customers(20260914-025808).csv`

Customer reference dataset providing profile and baseline AML risk context.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST1000` |
| `customer_name` | String | Source / Operational | Customer or legal-entity name. | `Customer 1` |
| `customer_type` | String | Source / Operational | Field representing customer type within the AML transaction-monitoring analytics workflow. | `Individual` |
| `country` | String | Derived / Analytical | Country associated with the customer or transaction. | `CA` |
| `occupation_industry` | String | Source / Operational | Field representing occupation industry within the AML transaction-monitoring analytics workflow. | `Consulting` |
| `kyc_risk` | String | Source / Operational | Attribute used to assess kyc risk. | `Low` |
| `pep_flag` | Integer | Source / Operational | Indicator identifying whether pep applies. | `0` |
| `expected_monthly_volume` | Float | Source / Operational | Field representing expected monthly volume within the AML transaction-monitoring analytics workflow. | `4304.87` |
| `account_open_date` | String | Derived / Analytical | Date/time attribute associated with account open. | `2024-01-24` |

## `transactions(20260914-025808).csv`

Raw transaction-level dataset used for transaction-monitoring and behavioral analysis.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `transaction_id` | String | Source / Operational | Unique identifier assigned to the transaction. | `TX100000` |
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST1019` |
| `transaction_date` | String | Source / Operational | Date on which the transaction occurred. | `2026-01-23 00:00:00` |
| `channel` | String | Source / Operational | Field representing channel within the AML transaction-monitoring analytics workflow. | `ACH` |
| `direction` | String | Source / Operational | Field representing direction within the AML transaction-monitoring analytics workflow. | `Debit` |
| `amount` | Float | Source / Operational | Monetary value associated with the transaction. | `2111.85` |
| `counterparty_country` | String | Derived / Analytical | Count-based analytical feature representing counterparty country. | `US` |
| `counterparty_id` | String | Derived / Analytical | Unique identifier for the counterparty. | `CP2154` |

## `alerts(1).csv`

AML alert-level dataset containing monitoring alerts and investigation outcomes.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `alert_id` | String | Source / Operational | Unique identifier assigned to the AML transaction-monitoring alert. | `ALT0001` |
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST1019` |
| `scenario` | String | Source / Operational | Field representing scenario within the AML transaction-monitoring analytics workflow. | `Potential Structuring` |
| `alert_date` | String | Source / Operational | Date on which the transaction-monitoring alert was generated. | `2026-08-28` |
| `alert_amount` | Float | Source / Operational | Field representing alert amount within the AML transaction-monitoring analytics workflow. | `63452.72` |
| `risk_score` | Integer | Derived / Analytical | Numeric score representing assessed AML/customer risk. | `88` |
| `recommended_action` | String | Source / Operational | Field representing recommended action within the AML transaction-monitoring analytics workflow. | `Review` |
| `disposition` | String | Source / Operational | Final analyst review outcome for the alert. | `Pending` |
| `risk_level` | String | Source / Operational | Attribute used to assess risk level. | `High` |

## `customer_risk_features.csv`

Feature-engineered customer dataset containing behavioral and AML risk indicators.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `customer_id` | String | Engineered / Analytical | Unique identifier assigned to the customer. | `CUST1000` |
| `total_transactions` | Integer | Engineered / Analytical | Aggregated total representing transactions. | `46` |
| `total_volume` | Float | Engineered / Analytical | Aggregated total representing volume. | `73515.5` |
| `avg_transaction_amount` | Float | Engineered / Analytical | Average measure representing transaction amount. | `1598.163` |
| `max_transaction_amount` | Float | Engineered / Analytical | Field representing max transaction amount within the AML transaction-monitoring analytics workflow. | `7554.27` |
| `cross_border_ratio` | Float | Engineered / Analytical | Derived measure representing cross border ratio. | `0.3261` |
| `high_risk_country_ratio` | Float | Engineered / Analytical | Derived measure representing high risk country ratio. | `0.0652` |
| `cash_ratio` | Float | Engineered / Analytical | Derived measure representing cash ratio. | `0.1957` |
| `wire_ratio` | Float | Engineered / Analytical | Derived measure representing wire ratio. | `0.1957` |
| `unique_counterparties` | Integer | Engineered / Analytical | Count-based analytical feature representing unique counterparties. | `46` |
| `kyc_risk` | String | Engineered / Analytical | Attribute used to assess kyc risk. | `Low` |
| `pep_flag` | Integer | Engineered / Analytical | Indicator identifying whether pep applies. | `0` |
| `expected_monthly_volume` | Float | Engineered / Analytical | Field representing expected monthly volume within the AML transaction-monitoring analytics workflow. | `4304.87` |
| `max_expected_ratio` | Float | Engineered / Analytical | Derived measure representing max expected ratio. | `4.8964` |
| `risk_score` | Integer | Engineered / Analytical | Numeric score representing assessed AML/customer risk. | `50` |
| `risk_level` | String | Engineered / Analytical | Attribute used to assess risk level. | `Moderate` |

## `transactions_enriched(1).csv`

Analytics-ready transaction dataset containing original transaction attributes plus engineered monitoring features.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `transaction_id` | String | Source / Operational | Unique identifier assigned to the transaction. | `TX100000` |
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST1019` |
| `transaction_date` | String | Source / Operational | Date on which the transaction occurred. | `2026-01-23 00:00:00` |
| `channel` | String | Source / Operational | Field representing channel within the AML transaction-monitoring analytics workflow. | `ACH` |
| `direction` | String | Source / Operational | Field representing direction within the AML transaction-monitoring analytics workflow. | `Debit` |
| `amount` | Float | Source / Operational | Monetary value associated with the transaction. | `2111.85` |
| `counterparty_country` | String | Source / Operational | Count-based analytical feature representing counterparty country. | `US` |
| `counterparty_id` | String | Source / Operational | Unique identifier for the counterparty. | `CP2154` |
| `customer_name` | String | Engineered / Enriched | Customer or legal-entity name. | `Customer 20` |
| `customer_type` | String | Engineered / Enriched | Field representing customer type within the AML transaction-monitoring analytics workflow. | `Business` |
| `country` | String | Engineered / Enriched | Country associated with the customer or transaction. | `NG` |
| `occupation_industry` | String | Engineered / Enriched | Field representing occupation industry within the AML transaction-monitoring analytics workflow. | `Education` |
| `kyc_risk` | String | Engineered / Enriched | Attribute used to assess kyc risk. | `Low` |
| `pep_flag` | Integer | Engineered / Enriched | Indicator identifying whether pep applies. | `0` |
| `expected_monthly_volume` | Float | Engineered / Enriched | Field representing expected monthly volume within the AML transaction-monitoring analytics workflow. | `4681.82` |
| `account_open_date` | String | Engineered / Enriched | Date/time attribute associated with account open. | `2019-04-03` |
| `month` | String | Engineered / Enriched | Field representing month within the AML transaction-monitoring analytics workflow. | `2026-01` |
| `is_cross_border` | Integer | Engineered / Enriched | Field representing is cross border within the AML transaction-monitoring analytics workflow. | `0` |
| `is_high_risk_country` | Integer | Engineered / Enriched | Count-based analytical feature representing is high risk country. | `0` |
| `is_cash` | Integer | Engineered / Enriched | Field representing is cash within the AML transaction-monitoring analytics workflow. | `0` |
| `is_wire` | Integer | Engineered / Enriched | Field representing is wire within the AML transaction-monitoring analytics workflow. | `0` |

## Dataset Relationships

- `customers(20260914-025808).csv.customer_id` ↔ `transactions(20260914-025808).csv.customer_id` provides a shared identifier for joins and investigation analysis.
- `customers(20260914-025808).csv.customer_id` ↔ `alerts(1).csv.customer_id` provides a shared identifier for joins and investigation analysis.
- `customers(20260914-025808).csv.customer_id` ↔ `customer_risk_features.csv.customer_id` provides a shared identifier for joins and investigation analysis.
- `customers(20260914-025808).csv.customer_id` ↔ `transactions_enriched(1).csv.customer_id` provides a shared identifier for joins and investigation analysis.
- `transactions(20260914-025808).csv.customer_id` ↔ `alerts(1).csv.customer_id` provides a shared identifier for joins and investigation analysis.
- `transactions(20260914-025808).csv.customer_id` ↔ `customer_risk_features.csv.customer_id` provides a shared identifier for joins and investigation analysis.
- `transactions(20260914-025808).csv.transaction_id` ↔ `transactions_enriched(1).csv.transaction_id` provides a shared identifier for joins and investigation analysis.
- `transactions(20260914-025808).csv.customer_id` ↔ `transactions_enriched(1).csv.customer_id` provides a shared identifier for joins and investigation analysis.
- `transactions(20260914-025808).csv.counterparty_id` ↔ `transactions_enriched(1).csv.counterparty_id` provides a shared identifier for joins and investigation analysis.
- `alerts(1).csv.customer_id` ↔ `customer_risk_features.csv.customer_id` provides a shared identifier for joins and investigation analysis.
- `alerts(1).csv.customer_id` ↔ `transactions_enriched(1).csv.customer_id` provides a shared identifier for joins and investigation analysis.
- `customer_risk_features.csv.customer_id` ↔ `transactions_enriched(1).csv.customer_id` provides a shared identifier for joins and investigation analysis.

## AML Analytics Workflow

**Customer Profile → Raw Transactions → EDA & Data Quality Validation → Feature Engineering → Enriched Transactions → Transaction-Monitoring Alerts → Alert Investigation & Risk Analysis**

The data structure supports end-to-end transaction-monitoring analytics by combining customer context, transactional behavior, engineered risk features, and alert outcomes. This enables pattern analysis, customer-risk prioritization, alert investigation, and monitoring-performance analysis.

## EDA & Feature Engineering Context

The raw customer and transaction datasets form the operational layer. `transactions_enriched(1).csv` represents the transaction-level feature-engineering layer, while `customer_risk_features.csv` contains customer-level analytical features. Keeping these layers separate demonstrates the progression from raw data through EDA, cleaning, feature engineering, and AML decision-support analytics.

## Data Quality Conventions

- Validate customer, transaction, and alert identifiers before joining datasets.
- Check transaction amounts for missing, duplicate, negative, or implausible values according to project business rules.
- Standardize date/time fields before temporal, velocity, and trend analysis.
- Standardize transaction types, countries, risk categories, alert statuses, and dispositions before aggregation.
- Evaluate missing values according to business meaning rather than automatically removing them.
- Reconcile engineered transaction and customer-risk features to their underlying source records.
- Validate derived indicators and risk scores before using them for alert prioritization or dashboards.

---

*Prepared for the AML Transaction Monitoring & Alert Investigation Analytics GitHub portfolio project.*