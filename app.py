import streamlit as st
from source.parsers import extract_text
from source.processor import analyze_contract


st.set_page_config(
    page_title="Contract Assistant Agent",
    page_icon="📄",
    layout="wide"
)

st.title("Contract Assistant Agent")
st.caption("Upload PDF or DOCX contracts for analysis.")

uploaded_file = st.file_uploader("Choose a contract", type=["pdf", "docx"])

if uploaded_file is not None:
    st.success(f"Loaded: {uploaded_file.name}")

    if st.button("Analyze Contract"):
        try:
            contract_text = extract_text(uploaded_file)
            result = analyze_contract(contract_text)

            days_until_expiration = result.get("days_until_expiration")
            expiration_status = result.get("expiration_status") or "Unknown"
            test_risk_label = result.get("test_risk_label")

            days_display = (
                str(days_until_expiration)
                if days_until_expiration is not None
                else "Not identified"
            )

            st.subheader("Analysis Result")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Risk Score", result.get("risk_score", 0))

            with col2:
                st.metric("Priority", result.get("priority", "Unknown"))

            with col3:
                st.metric("Expiration Status", expiration_status)

            with col4:
                st.metric("Days Until Expiration", days_display)

            st.divider()

            left_col, right_col = st.columns([1.3, 1])

            with left_col:
                st.markdown("### Contract Overview")
                st.write(f"**Recommendation:** {result.get('recommendation', 'N/A')}")
                st.write(f"**Summary:** {result.get('summary', 'N/A')}")

                if test_risk_label:
                    st.info(f"Double-check from OBSERVACOES PARA TESTE: {test_risk_label}")

            with right_col:
                st.markdown("### Key Details")
                st.write(f"**Contract Value:** R$ {result.get('contract_value', 0.0):.2f}")
                st.write(f"**Start Date:** {result.get('start_date') or 'Not identified'}")
                st.write(f"**End Date:** {result.get('end_date') or 'Not identified'}")

            st.divider()

            if expiration_status == "Critical":
                st.warning("This contract is very close to expiration.")
            elif expiration_status in ["Expiring Soon", "High Attention", "Monitor"]:
                st.warning("This contract requires monitoring based on the expiration timeline.")
            elif expiration_status == "Expired":
                st.error("This contract has already expired.")
            elif days_until_expiration is None:
                st.info("The contract priority was identified, but the expiration date could not be extracted.")
            else:
                st.info("This contract is not close to expiration.")

        except Exception as e:
            st.error(f"Analysis failed: {e}")