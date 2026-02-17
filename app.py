import streamlit as st

st.set_page_config(
    page_title="Autonomous Tech Research Agent",
    page_icon="🤖",
    layout="wide"
)

# ===== Custom Header =====
st.markdown("""
<h1 style='text-align: center; color: #4CAF50;'>
🤖 Autonomous Technology Research Agent
</h1>
<p style='text-align: center; font-size:18px;'>
Multi-Agent LLM Research System using CrewAI + Groq + Tavily
</p>
""", unsafe_allow_html=True)

st.divider()

# ===== Input Section =====
col1, col2 = st.columns([2,1])

with col1:
    topic = st.text_input("🔎 Enter Technology Topic")

with col2:
    run_btn = st.button("🚀 Run Research")

# ===== Run Pipeline =====
if run_btn:

    if topic.strip() == "":
        st.warning("Please enter a topic first")
    else:
        with st.spinner("Agents are researching the web and generating report..."):

            try:
                from main import run_research_pipeline
                result = run_research_pipeline(topic)

                st.success("✅ Research Completed")

                st.subheader("📄 Final Research Report")
                st.markdown(result)

                # download button
                st.download_button(
                    "⬇️ Download Report",
                    result,
                    file_name="tech_research_report.txt"
                )

            except Exception as e:
                st.error("❌ Error occurred")
                st.exception(e)

st.divider()

# ===== Footer =====
st.markdown("""
<center>
Built with CrewAI • LangChain • Tavily • Groq • Streamlit
</center>
""", unsafe_allow_html=True)
