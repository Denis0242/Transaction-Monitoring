import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="AML Investigator Workbench", layout="wide")

ROOT = Path(__file__).resolve().parents[1]
alerts = pd.read_csv(ROOT/"data"/"processed"/"alerts.csv")
tx = pd.read_csv(ROOT/"data"/"processed"/"transactions_enriched.csv", parse_dates=["transaction_date"])
customers = pd.read_csv(ROOT/"data"/"raw"/"customers.csv")
risk = pd.read_csv(ROOT/"data"/"processed"/"customer_risk_features.csv")

st.title("AML Transaction Monitoring & Alert Investigation Analytics")
st.caption(
    "Synthetic portfolio project | SQL + Python + Tableau + Streamlit | "
    "Transaction monitoring, customer risk assessment, alert investigation, and escalation decision support."
)

with st.sidebar:
    st.header("Alert Filters")
    st.caption("Use the dropdowns below to filter the dashboard.")

    scenario_options = ["All"] + sorted(
        alerts["scenario"].dropna().astype(str).unique().tolist()
    )
    selected_scenario = st.selectbox(
        "Scenario",
        scenario_options,
        index=0,
        key="sidebar_scenario_filter"
    )

    disposition_options = ["All"] + sorted(
        alerts["disposition"].dropna().astype(str).unique().tolist()
    )
    selected_disposition = st.selectbox(
        "Disposition",
        disposition_options,
        index=0,
        key="sidebar_disposition_filter"
    )

    risk_score_options = ["All", "40+", "50+", "60+", "70+", "80+", "90+"]
    selected_min_risk = st.selectbox(
        "Minimum Alert Risk Score",
        risk_score_options,
        index=0,
        key="sidebar_min_risk_filter"
    )

filtered = alerts.copy()

if selected_scenario != "All":
    filtered = filtered[
        filtered["scenario"].astype(str).eq(selected_scenario)
    ]

if selected_disposition != "All":
    filtered = filtered[
        filtered["disposition"].astype(str).eq(selected_disposition)
    ]

if selected_min_risk != "All":
    min_risk = int(selected_min_risk.replace("+", ""))
    filtered = filtered[
        pd.to_numeric(filtered["risk_score"], errors="coerce").fillna(0) >= min_risk
    ]

total_alerts = len(filtered)
high_risk_alerts = (filtered["risk_score"] >= 80).sum() if total_alerts else 0
escalations = (
    filtered["disposition"].isin(["Escalate to Case", "SAR Consideration"]).sum()
    if total_alerts else 0
)
alert_volume = filtered["alert_amount"].sum() if total_alerts else 0
high_risk_pct = high_risk_alerts / total_alerts * 100 if total_alerts else 0
escalation_pct = escalations / total_alerts * 100 if total_alerts else 0

st.subheader("Executive Summary")

if filtered.empty:
    st.warning("No AML alerts match the selected filters. Try lowering the minimum risk score or selecting additional scenarios.")
else:
    if high_risk_pct >= 40 or escalation_pct >= 30:
        portfolio_status = "Heightened AML Risk"
        portfolio_message = "The selected alert population contains a significant concentration of high-risk or escalated activity."
    elif high_risk_alerts > 0 or escalations > 0:
        portfolio_status = "Targeted Investigation Required"
        portfolio_message = "Some alerts require deeper investigation, although elevated risk is not concentrated across the entire portfolio."
    else:
        portfolio_status = "Routine Monitoring"
        portfolio_message = "The selected alert population does not currently show a strong concentration of elevated AML risk."

    s1, s2, s3 = st.columns([1.3, 1, 2.7])
    s1.metric("Portfolio Status", portfolio_status)
    s2.metric("Escalations", f"{escalations:,}")
    s3.info(portfolio_message)

    st.markdown(
        f"""**Plain-English summary:** The selected view contains **{total_alerts:,} AML alerts**
        representing approximately **${alert_volume:,.0f} in alerted transaction activity**.
        **{high_risk_alerts:,} alerts ({high_risk_pct:.1f}%)** have risk scores of 80 or above,
        while **{escalations:,} alerts ({escalation_pct:.1f}%)** are marked for case escalation
        or SAR consideration."""
    )

    st.markdown("#### What This Means")
    if high_risk_alerts:
        st.write(f"• **{high_risk_alerts:,} high-risk alerts** should receive priority investigator attention.")
    if escalations:
        st.write(f"• **{escalations:,} alerts** have reached an escalation or SAR-consideration stage.")
    top_scenario = filtered["scenario"].value_counts().index[0]
    st.write(f"• The most common alert scenario is **{top_scenario}**.")
    st.write(f"• Approximately **${alert_volume:,.0f}** in activity is associated with the selected alerts.")

    st.markdown("#### Final Portfolio Decision")
    if portfolio_status == "Heightened AML Risk":
        st.error("Prioritize high-risk alerts and cases marked for escalation or SAR consideration. Review customer profiles, transaction behavior, counterparties, geographic exposure, and prior alerts before disposition.")
    elif portfolio_status == "Targeted Investigation Required":
        st.warning("Continue standard monitoring across the broader portfolio while prioritizing the highest-risk alerts and customers for deeper investigation.")
    else:
        st.success("Maintain routine transaction monitoring. The selected alert population does not currently indicate broad AML escalation.")

st.divider()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Alerts", f"{total_alerts:,}")
c2.metric("High-Risk Alerts", f"{high_risk_alerts:,}")
c3.metric("Escalations", f"{escalations:,}")
c4.metric("Alert Volume", f"${alert_volume:,.0f}")

customer_ids = sorted(set(customers["customer_id"].dropna()) & set(risk["customer_id"].dropna()))

st.subheader("Customer Investigation Summary")

if not customer_ids:
    st.warning("No customers have both a customer profile and AML risk record.")
    selected_customer = None
    customer_alerts = pd.DataFrame()
    customer_tx = pd.DataFrame()
else:
    selected_customer = st.selectbox("Select a customer to understand the investigation", customer_ids)
    profile = customers[customers["customer_id"] == selected_customer]
    rf = risk[risk["customer_id"] == selected_customer]
    customer_tx = tx[tx["customer_id"] == selected_customer].sort_values("transaction_date", ascending=False)
    customer_alerts = alerts[alerts["customer_id"] == selected_customer].sort_values("risk_score", ascending=False)

    if profile.empty or rf.empty:
        st.warning("Customer profile or AML risk information is unavailable.")
    else:
        p = profile.iloc[0]
        r = rf.iloc[0]

        pep_value = p.get("pep_flag", 0)
        is_pep = pd.notna(pep_value) and str(pep_value).strip().lower() in ["1", "1.0", "yes", "true"]

        risk_score = r.get("risk_score", 0)
        risk_level = r.get("risk_level", "Unknown")
        expected_volume = p.get("expected_monthly_volume", 0)
        total_volume = r.get("total_volume", 0)
        cross_border_ratio = r.get("cross_border_ratio", 0)
        unique_counterparties = r.get("unique_counterparties", 0)
        kyc_risk = p.get("kyc_risk", "Unknown")

        a, b, c, d = st.columns(4)
        a.metric("KYC Risk", str(kyc_risk))
        b.metric("AML Risk Score", int(risk_score) if pd.notna(risk_score) else 0)
        c.metric("Risk Level", str(risk_level))
        d.metric("PEP", "Yes" if is_pep else "No")

        e, f, g, h = st.columns(4)
        e.metric("Expected Monthly Volume", f"${expected_volume:,.0f}" if pd.notna(expected_volume) else "$0")
        f.metric("Total Volume", f"${total_volume:,.0f}" if pd.notna(total_volume) else "$0")
        g.metric("Cross-Border Ratio", f"{cross_border_ratio:.1%}" if pd.notna(cross_border_ratio) else "0%")
        h.metric("Unique Counterparties", int(unique_counterparties) if pd.notna(unique_counterparties) else 0)

        st.markdown("#### Investigation Summary")
        alert_count = len(customer_alerts)
        high_customer_alerts = (customer_alerts["risk_score"] >= 80).sum() if not customer_alerts.empty else 0
        customer_escalations = (
            customer_alerts["disposition"].isin(["Escalate to Case", "SAR Consideration"]).sum()
            if not customer_alerts.empty else 0
        )

        volume_ratio = None
        if pd.notna(expected_volume) and expected_volume > 0 and pd.notna(total_volume):
            volume_ratio = total_volume / expected_volume

        st.write(
            f"Customer **{selected_customer}** is rated **{risk_level} AML risk** with a risk score of "
            f"**{int(risk_score) if pd.notna(risk_score) else 0}** and has **{alert_count:,} AML alert(s)**, "
            f"including **{high_customer_alerts:,} high-risk alert(s)**."
        )

        if pd.notna(cross_border_ratio):
            st.write(f"Cross-border activity represents approximately **{cross_border_ratio:.1%}** of observed transaction activity.")

        if volume_ratio is not None:
            if volume_ratio >= 2:
                st.write(f"Observed transaction volume is approximately **{volume_ratio:.1f}× the expected monthly volume**, which may require further explanation.")
            else:
                st.write("Observed transaction volume is relatively consistent with the customer's expected activity profile.")

        if is_pep:
            st.write("The customer is identified as a **PEP**, increasing the level of due diligence and monitoring expected.")

        if customer_escalations:
            st.write(f"**{customer_escalations} alert(s)** have already reached an escalation or SAR-consideration stage.")

        st.markdown("#### Recommended Decision")
        elevated_volume = volume_ratio is not None and volume_ratio >= 2
        high_cross_border = pd.notna(cross_border_ratio) and cross_border_ratio >= 0.40

        if str(risk_level) in ["High", "Critical"] and (
            high_customer_alerts > 0 or customer_escalations > 0 or elevated_volume or high_cross_border
        ):
            st.error("🔴 **ESCALATE FOR FURTHER INVESTIGATION**\n\nThe customer combines elevated AML risk with additional concerns such as high-risk alerts, unusual transaction volume, significant cross-border activity, or previous escalation activity. Further investigation is recommended before closure.")
        elif customer_escalations > 0:
            st.warning("🟠 **ENHANCED REVIEW REQUIRED**\n\nThe customer has alert activity already identified for case escalation or SAR consideration. Additional review should be completed before final disposition.")
        elif str(risk_level) in ["High", "Critical"] or elevated_volume or high_cross_border or is_pep:
            st.warning("🟠 **TARGETED AML REVIEW**\n\nThe customer has elevated risk characteristics that justify additional transaction and customer-profile review.")
        else:
            st.success("🟢 **CLOSE / CONTINUE ROUTINE MONITORING**\n\nThe available evidence does not currently show a strong combination of elevated AML risk indicators requiring immediate escalation.")

st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["Alert Queue", "Customer 360", "Portfolio Analytics", "Tableau Gallery"])

with tab1:
    st.subheader("Risk-Ranked Alert Queue")
    st.caption("Alerts are ranked by risk score and transaction amount so investigators can quickly identify the highest-priority alerts.")
    if filtered.empty:
        st.info("No alerts match the selected filters.")
    else:
        st.dataframe(filtered.sort_values(["risk_score", "alert_amount"], ascending=[False, False]), use_container_width=True, hide_index=True)

with tab2:
    st.subheader("Customer 360")
    if selected_customer is None:
        st.warning("No valid customer records are available.")
    else:
        st.markdown(f"### Customer {selected_customer}")
        st.markdown("#### Customer Alerts")
        if customer_alerts.empty:
            st.info("No AML alerts are available for this customer.")
        else:
            st.dataframe(customer_alerts, use_container_width=True, hide_index=True)

        st.markdown("#### Recent Transactions")
        preferred_cols = ["transaction_id", "transaction_date", "channel", "direction", "amount", "counterparty_country", "counterparty_id"]
        available_cols = [col for col in preferred_cols if col in customer_tx.columns]

        if customer_tx.empty:
            st.info("No transactions are available for this customer.")
        elif available_cols:
            st.dataframe(customer_tx[available_cols].head(75), use_container_width=True, hide_index=True)
        else:
            st.warning("Transaction data is available, but the expected display columns could not be found.")

        st.markdown("#### Weekly Transaction Trend")
        if not customer_tx.empty and "transaction_date" in customer_tx.columns and "amount" in customer_tx.columns:
            trend = customer_tx.set_index("transaction_date")["amount"].resample("W").sum()
            st.line_chart(trend)
        else:
            st.info("Insufficient transaction information to create the trend.")

        st.markdown("#### Investigator Notes")
        st.text_area(
            "Document review rationale",
            "Reviewed customer profile, expected activity, KYC risk, alert scenario, transaction behavior, counterparties, "
            "geographic exposure, prior alerts, and relevant red flags. Document closure or escalation rationale here.",
            height=140
        )

with tab3:
    st.subheader("Alert Distribution")
    if not filtered.empty:
        chart = filtered.groupby("scenario", as_index=False).size().rename(columns={"size": "alerts"})
        if not chart.empty:
            st.bar_chart(chart.set_index("scenario"))
    else:
        st.info("No alert data available for the selected filters.")

    st.subheader("Customer Risk Distribution")
    if "risk_level" in risk.columns:
        rd = risk["risk_level"].dropna().value_counts()
        if not rd.empty:
            st.bar_chart(rd)

with tab4:
    st.subheader("Tableau Gallery")
    st.caption(
        "Executive Tableau dashboard for quick recruiter and hiring-manager review."
    )

    dashboard_candidates = [
        ROOT / "images" / "02_executive_dashboard.png",
        ROOT / "images" / "01_executive_dashboard.png",
    ]
    dashboard = next((p for p in dashboard_candidates if p.exists()), None)

    if dashboard:
        st.image(
            str(dashboard),
            caption="AML Transaction Monitoring & Alert Investigation — Executive Dashboard",
            use_container_width=True
        )
    else:
        st.warning(
            "Executive dashboard image not found. Add `02_executive_dashboard.png` to the images folder."
        )

st.info("Educational portfolio demonstration only. No real bank or customer data is used.")

st.caption(
    "Synthetic educational portfolio project. No real customer, transaction, bank, alert, or SAR data is used. "
    "Automated recommendations support analyst review and are not regulatory filing decisions."
)
