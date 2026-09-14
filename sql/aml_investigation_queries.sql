
-- AML Transaction Monitoring & Alert Investigation Analytics
-- 12 focused SQL analyses

-- 1. High-value transactions
SELECT *
FROM transactions
WHERE amount >= 10000
ORDER BY amount DESC;

-- 2. Potential structuring
SELECT customer_id, COUNT(*) AS txn_count, SUM(amount) AS total_amount
FROM transactions
WHERE channel = 'Cash Deposit'
  AND amount BETWEEN 8000 AND 9999.99
GROUP BY customer_id
HAVING COUNT(*) >= 3
ORDER BY total_amount DESC;

-- 3. High-risk jurisdiction wires
SELECT customer_id, transaction_id, transaction_date, amount, counterparty_country
FROM transactions
WHERE channel = 'Wire'
  AND counterparty_country IN ('RU','IR','SY')
  AND amount >= 10000
ORDER BY amount DESC;

-- 4. Monthly transaction volume
SELECT customer_id,
       DATE_TRUNC('month', transaction_date) AS month,
       SUM(amount) AS monthly_volume
FROM transactions
GROUP BY customer_id, DATE_TRUNC('month', transaction_date);

-- 5. Volume compared with expected customer activity
SELECT t.customer_id,
       DATE_TRUNC('month', t.transaction_date) AS month,
       SUM(t.amount) AS monthly_volume,
       c.expected_monthly_volume,
       SUM(t.amount)/NULLIF(c.expected_monthly_volume,0) AS volume_ratio
FROM transactions t
JOIN customers c ON t.customer_id = c.customer_id
GROUP BY t.customer_id, DATE_TRUNC('month', t.transaction_date), c.expected_monthly_volume
HAVING SUM(t.amount) > 3*c.expected_monthly_volume
ORDER BY volume_ratio DESC;

-- 6. Rapid movement / velocity
SELECT customer_id,
       CAST(transaction_date AS DATE) AS txn_day,
       COUNT(*) AS txn_count,
       SUM(amount) AS daily_volume
FROM transactions
GROUP BY customer_id, CAST(transaction_date AS DATE)
HAVING COUNT(*) >= 4 AND SUM(amount) >= 30000
ORDER BY daily_volume DESC;

-- 7. Repeat counterparties
SELECT customer_id, counterparty_id,
       COUNT(*) AS txn_count, SUM(amount) AS total_amount
FROM transactions
GROUP BY customer_id, counterparty_id
HAVING COUNT(*) >= 4
ORDER BY total_amount DESC;

-- 8. Cross-border exposure
SELECT customer_id, counterparty_country,
       COUNT(*) AS txn_count, SUM(amount) AS total_amount
FROM transactions
WHERE counterparty_country <> 'US'
GROUP BY customer_id, counterparty_country
ORDER BY total_amount DESC;

-- 9. PEP customer activity
SELECT c.customer_id, COUNT(t.transaction_id) AS txn_count, SUM(t.amount) AS total_volume
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
WHERE c.pep_flag = 1
GROUP BY c.customer_id
ORDER BY total_volume DESC;

-- 10. Alert volume by scenario
SELECT scenario, COUNT(*) AS alert_count,
       AVG(risk_score) AS avg_risk_score,
       SUM(alert_amount) AS alert_volume
FROM alerts
GROUP BY scenario
ORDER BY alert_count DESC;

-- 11. Escalation rate by scenario
SELECT scenario,
       COUNT(*) AS total_alerts,
       SUM(CASE WHEN disposition IN ('Escalate to Case','SAR Consideration') THEN 1 ELSE 0 END) AS escalated,
       100.0 * SUM(CASE WHEN disposition IN ('Escalate to Case','SAR Consideration') THEN 1 ELSE 0 END) / COUNT(*) AS escalation_rate
FROM alerts
GROUP BY scenario
ORDER BY escalation_rate DESC;

-- 12. Investigator priority queue
SELECT alert_id, customer_id, scenario, risk_score, alert_amount, disposition
FROM alerts
ORDER BY risk_score DESC, alert_amount DESC;
