import os
import uuid 
import json 
import streamlit as st
from utils.config import get_backend_url
from utils.types import AnalyzeRequest, AnalyzeResponse


# Page Config
st.set_page_config(
    page_title= "Jobbie AI",
    page_icon="🤖",
    layout="wide"
)

# Title and Intro 
st.title("🤖 AI Research Assistant for JobSeekers")
st.markdown("Upload your resume, choose your target role, and get personalized insights!")

# Sidebar
st.sidebar.header("⚙️ Settings")
role = st.sidebar.text_input("Target Role", placeholder="e.g., Data Scientist")
tone = st.sidebar.selectbox("Report Tone", ["Professional", "Friendly", "Concise"])
experience_level = st.sidebar.selectbox("Experience Level", ["Entry", "Mid", "Senior"])

# File Upload
uploaded_file = st.file_uploader("📄 Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
backend_url = get_backend_url()

# Session Handling
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Run Analysis Button
if st.button("🚀 Run Analysis") and uploaded_file and role:
    with st.spinner("Analyzing your resume..."):
        resume_text = uploaded_file.read().decode("latin-1", errors="ignore")

        # Build Request
        req = AnalyzeRequest(
            resume_text=resume_text,
            target_role=role,
            tone=tone,
            experience_level=experience_level,
            session_id=st.session_state.session_id
        )

        # Mock Response (until wired backend)
        res = AnalyzeResponse(
            match_score=82,
            matched_skills=["Python", "SQL", "Data Analysis"],
            missing_skills=["Deep Learning", "MLOps"],
            recommendations=[
                "Consider adding hands-on projects with TensorFlow/PyTorch.",
                "Highlight experience with cloud platforms like AWS/GCP."
            ],
            hashtags=["#DataScience", "#CareerGrowth", "AIJobs"]
        )

        # Output Display
        st.subheader("📊 Resume Analysis Results")
        st.metric("Target Role", role)
        st.metric("Match Score", f"{res.match_score}%") 
        st.metric("Session ID", st.session_state.session_id)

        st.write("✅ **Matched Skills:**", ", ".join(res.matched_skills))
        st.write("⚠️ **Missing Skills:**", ", ".join(res.missing_skills))

        st.write("💡 **Recommendations:**")
        for rec in res.recommendations:
            st.write(f"- {rec}")

        st.write("📌 Suggested Hashtags:", " ".join(res.hashtags))

        with st.expander("👨‍💻 Agent Logs"):
            st.json({
                "TrendHunter": "Analyzed job market data.",
                "ResumeAnalyzer": "Extracted skills and experience.",
                "GapFinder": "Detected missing skills.",
                "Advisor": "Generated personalized recommendations."
            })

elif not uploaded_file:
    st.info("Please upload your resume to begin analysis.")