# 🔤 Language Tutor AI (English & Thai)

An interactive AI-powered language tutor that supports both **English** and **Thai**. This application corrects grammar, explains mistakes, and offers useful vocabulary suggestions — all in real time.

Built using **LangChain**, **Chainlit**, and **OpenAI**, this tool is ideal for language learners looking to improve sentence construction and understanding in either language.

---

## ✨ Features

- 🌐 **Automatic Language Detection** (English or Thai)
- ✅ **Grammar Correction**
- 🧠 **Explanation of Corrections**
- 📘 **Vocabulary Suggestions**
- ⚡ **Real-time streaming responses** powered by Chainlit and LangChain’s `Runnable` interface

---

## 📸 Demo

**Input (English):**  
`She don't like go to school.`  
**Output:**  
- ✅ Corrected: *She doesn’t like going to school.*  
- 💡 Explanation: “Don’t” → “Doesn’t” for third person. “Go” → “Going” after "like."

**Input (Thai):**  
`เขาไปตลาดเมื่อวานนี้แล้วจะไปอีกพรุ่งนี้`  
**Output:**  
- ✅ Corrected: *เขาไปตลาดเมื่อวานนี้ และจะไปอีกพรุ่งนี้*  
- 💡 Explanation: Added "และ" to improve sentence clarity and flow.

---

## 🚀 Getting Started

1. **Clone the repository**

   bash  
   `git clone https://github.com/yourusername/language-tutor-ai.git`  
   `cd language-tutor-ai`

2. **Set up the environment and run the app**

   bash  
   `python -m venv venv`  

   _Activate the virtual environment:_  
   macOS/Linux → `source venv/bin/activate`  
   Windows → `venv\Scripts\activate`

   _Install dependencies:_  
   `pip install -r requirements.txt`

   _Create a .env file and add your OpenAI API key:_  
   `echo OPENAI_API_KEY=your_openai_key_here > .env`

   _Run the Chainlit app:_  
   `chainlit run app.py`

---

## 📚 Learning Outcomes

- Real-world usage of **LangChain** and **Chainlit** for interactive LLM applications  
- Prompt engineering for **multilingual grammar correction**  
- Creating clean, maintainable AI app workflows with **LangChain Runnables**

---

## 🙌 Acknowledgements

- [Chainlit](https://www.chainlit.io/)  
- [LangChain](https://www.langchain.com/)  
- [OpenAI](https://platform.openai.com/)
