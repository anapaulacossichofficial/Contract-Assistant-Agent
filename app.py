import streamlit as st

from source.processor import analyze_file


st.set_page_config(page_title="Contract Assistant Agent", page_icon="📄", layout="centered")

st.title("Contract Assistant Agent")
st.caption("Upload PDF or DOCX contracts for analysis.")

uploaded_file = st.file_uploader("Choose a contract", type=["pdf", "docx"])

if uploaded_file is not None:
    st.success(f"Loaded: {uploaded_file.name}")

    if st.button("Analyze Contract"):
        with st.spinner("Analyzing contract..."):
            try:
                result = analyze_file(uploaded_file)

                if not result:
                    st.error("The analysis did not return any result.")
                    st.stop()

                st.subheader("Analysis Result")

                st.metric("Risk Score", result.risk_score)
                st.write(f"**Priority:** {result.priority}")
                st.write(f"**Recommendation:** {result.recommendation}")
                st.write(f"**Value:** R$ {result.value:,.2f}")
                st.write(f"**Period:** {result.start_date} to {result.end_date}")
                st.write(f"**Days to Expiry:** {result.days_to_expiry}")
                
                if result.rationale:
                    st.write("**Rationale:**")
                    for item in result.rationale:
                        st.write(f"- {item}")
                
                with st.expander("Contract Preview"):
                    st.text(result.text_preview)

            except Exception as e:
                st.error(f"Analysis failed: {e}")