## 📄 AI Resume Matcher

An AI-powered Streamlit web application that analyzes resumes against job descriptions and provides a **match score, missing skills, and actionable improvement suggestions** using a free Large Language Model (LLM).

---

## 🚀 Features

* Upload resume as **PDF** or paste resume text
* Paste **job description**
* AI-powered analysis with:

  * 🎯 Resume–job **match score**
  * ❌ **Missing skills** identification
  * ✅ Strongly matched skills
  * 🛠 Resume improvement suggestions
* **Real-time streaming** AI responses
* Clean, responsive **Streamlit UI**
* Deployed-ready for **Streamlit Cloud**

---

## 🧠 Tech Stack

* **Python**
* **Streamlit** – Frontend & app framework
* **Groq LLM API** (LLaMA-3.1-8B-Instant)
* **PyPDF** – Resume PDF text extraction
* **Prompt Engineering** – Structured LLM outputs

---

## 🏗 Project Structure

```
ai-resume-matcher/
├── app.py
├── requirements.txt
├── .gitignore
```

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-matcher.git
cd ai-resume-matcher
```

### 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Groq API key

```bash
setx GROQ_API_KEY "your_groq_api_key_here"
```

Restart the terminal after setting the key.

### 5️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🌐 Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to 👉 [https://share.streamlit.io](https://share.streamlit.io)
3. Create a new app and select this repository
4. Add the following secret:


5. Deploy 🚀

---

## 📌 Notes

* Interview rounds and match scores are **AI-estimated** based on typical hiring patterns.
* Designed as a **portfolio project** demonstrating real-world AI application development.
* No API keys are hardcoded for security.

---

## 👤 Author

**Hithesh Kumar H**

* GitHub: [https://github.com/hiteshkumarh](https://github.com/hiteshkumarh)
* LinkedIn: [https://linkedin.com/in/hitheshkumarh](https://linkedin.com/in/hitheshkumarh)

---

* Add screenshots section

Just tell me.
