# 🔤 Language Tutor AI (English & Thai)

An interactive AI-powered language tutor that supports both **English** and **Thai**. This app corrects grammar, explains mistakes, and offers useful vocabulary — all in real-time.

Built using **LangChain**, **Chainlit**, and **OpenAI**, this tool is perfect for language learners looking to improve their sentence construction and understanding.

---

## ✨ Features

- 🌐 **Automatic Language Detection** (English or Thai)
- ✅ **Grammar Correction**
- 🧠 **Explanations** for grammatical fixes
- 📘 **Vocabulary Suggestions**
- ⚡ **Real-time streaming chat** powered by Chainlit and LangChain's `Runnable`

---

## 📸 Demo

**Input (English):**  
`She don't like go to school.`  
**Output:**  
- ✅ Corrected: *She doesn’t like going to school.*  
- 💡 Explanation: “Don’t” should be “doesn’t” for third person. “Go” becomes “going” after “like.”

**Input (Thai):**  
`เขาไปตลาดเมื่อวานนี้แล้วจะไปอีกพรุ่งนี้`  
**Output:**  
- ✅ Corrected: *เขาไปตลาดเมื่อวานนี้ และจะไปอีกพรุ่งนี้*  
- 💡 Explanation: Added "และ" for clarity and flow.

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/language-tutor-ai.git
   cd language-tutor-ai
Set up a virtual environment

2. **Set up the environment and run the app**
# Create and activate a virtual environment
python -m venv venv
# For macOS/Linux:
source venv/bin/activate
# For Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your OpenAI API key
echo OPENAI_API_KEY=your_openai_key_here > .env

# Run the Chainlit app
chainlit run app.py
