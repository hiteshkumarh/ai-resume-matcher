import streamlit as st
from pypdf import PdfReader
import os
import re
from groq import Groq


# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Resume Matcher",
    page_icon="📄",
    layout="wide"
)

# ---------------- Groq Client ----------------
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------- Helper Functions ----------------
def extract_text_from_pdf(uploaded_file):
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
    except Exception:
        return None


def build_prompt(resume_text, job_description):
    return f"""
You are an experienced technical recruiter.

Analyze the resume against the job description and hiring process.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

INSTRUCTIONS (FOLLOW STRICTLY):
1. Give a MATCH SCORE from 0 to 100 (integer only).
2. List MISSING SKILLS as bullet points.
3. List STRONG MATCHES.
4. Suggest 3–5 RESUME IMPROVEMENTS.
5. Based on the role and company mentioned in the job description,
   ESTIMATE the typical INTERVIEW ROUNDS.

OUTPUT FORMAT (STRICT):
MATCH_SCORE: <number>

MISSING_SKILLS:
- skill 1
- skill 2

STRONG_MATCHES:
- skill 1
- skill 2

IMPROVEMENT_SUGGESTIONS:
- suggestion 1
- suggestion 2

INTERVIEW_ROUNDS:
- Round 1: <name>
- Round 2: <name>
- Round 3: <name>
Total Rounds: <number>
"""

def parse_llm_output(text):
    score = None
    missing_skills = []

    score_match = re.search(r"MATCH_SCORE:\s*(\d+)", text)
    if score_match:
        score = int(score_match.group(1))

    missing_section = re.search(
        r"MISSING_SKILLS:(.*?)(STRONG_MATCHES:|IMPROVEMENT_SUGGESTIONS:)",
        text,
        re.S
    )
    if missing_section:
        lines = missing_section.group(1).splitlines()
        missing_skills = [
            line.replace("-", "").strip()
            for line in lines if line.strip().startswith("-")
        ]

    return score, missing_skills
# ---------------- UI ----------------
st.title("📄 Resume Matcher")
st.write(
    "Upload your resume or paste the text, then add a job description. "
    "This app will analyze how well your resume matches the job."
)

st.markdown("---")

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("📄 Resume Input")
    resume_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
    resume_text = st.text_area("Or paste your resume text here", height=300)

with right_col:
    st.subheader("💼 Job Description")
    job_description = st.text_area("Paste the job description here", height=430)

st.markdown("---")

analyze_clicked = st.button("🔍 Analyze Resume", use_container_width=True)

# ---------------- Backend Logic ----------------
if analyze_clicked:
    # Resume normalization
    if resume_file:
        resume_content = extract_text_from_pdf(resume_file)
        if not resume_content:
            st.error("Failed to extract text from PDF.")
            st.stop()
    elif resume_text.strip():
        resume_content = resume_text.strip()
    else:
        st.error("Please upload or paste a resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please paste the job description.")
        st.stop()

    # LLM Call
    st.subheader("📊 Analysis Result")

    output_placeholder = st.empty()
    streamed_text = ""

    with st.spinner("Analyzing with LLaMA-3..."):
        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": build_prompt(resume_content, job_description)}
            ],
            temperature=0.3,
            stream=True,
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                streamed_text += chunk.choices[0].delta.content
                output_placeholder.markdown(streamed_text)

    # ---------------- Parse LLM Output ----------------
    score, missing_skills = parse_llm_output(streamed_text)

    # ---------------- Score Bar ----------------
    if score is not None:
        st.markdown("## 🎯 Match Score")
        st.progress(score / 100)
        st.write(f"**{score}% match**")

    # ---------------- Missing Skills ----------------
    if missing_skills:
        st.markdown("## ❌ Missing Skills")
        for skill in missing_skills:
            st.write(f"- {skill}")

        # ---------------- Parse LLM Output ----------------
        score, missing_skills = parse_llm_output(streamed_text)

        # ---------------- Score Bar ----------------
        if score is not None:
            st.markdown("## 🎯 Match Score")
            st.progress(score / 100)
            st.write(f"**{score}% match**")

        # ---------------- Missing Skills ----------------
        if missing_skills:
            st.markdown("## ❌ Missing Skills")
            for skill in missing_skills:
                st.write(f"- {skill}")



