# 📬 Smart Email Classifier (Prompt Engineering with OpenAI)

This project is a hands-on, real-world demonstration of how to classify and understand SMS messages using **OpenAI's GPT** models and **prompt engineering techniques**. It includes a full Streamlit UI for live interaction.

---

## ✅ What We've Built

- **Few-Shot Prompt Classifier**  
  Classify messages as `Spam` or `Not Spam` using few-shot examples.

- **Zero-Shot Summarization**  
  Generate one-line summaries of messages using direct instruction.

- **Chain-of-Thought Reasoning**  
  Ask GPT to explain its logic before making a classification.

- **Streamlit UI**  
  A live web interface to run all tasks—no code required.

- **Secure API Usage**  
  OpenAI API key is stored securely in a `.env` file.

- **OpenAI SDK v1.0+ Compatible**  
  Clean code using the modern `OpenAI()` client structure.

---

## 🧠 Skills Demonstrated

- Prompt Engineering (Few-Shot, Zero-Shot, CoT)
- GPT-3.5 API Integration
- Streamlit App Development
- Secure API handling with `dotenv`
- Dataset processing via `KaggleHub` and `pandas`
- GitHub-based version control and collaboration

---

## 📂 Project Structure

smart-email-classifier/
├── app.py # Streamlit UI
├── classify_with_prompt.py # Few-shot prompt classification
├── classify_with_cot.py # Chain-of-Thought classifier
├── summarize_message.py # Zero-shot summarization
├── load_dataset.py # Dataset fetch and preview
├── .env # API Key (not included in repo)
├── .gitignore
└── README.md



---

## 🚀 How to Run

### 🔧 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShubhamRSY/smart-email-classifier.git
   cd smart-email-classifier


```

Create a .env file with your OpenAI key:

ini
Copy
Edit
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
```

▶️ Running Tasks
1. Few-Shot Classification
bash
Copy
Edit
python classify_with_prompt.py
2. Zero-Shot Summarization
bash
Copy
Edit
python summarize_message.py
3. Chain-of-Thought Reasoning
bash
Copy
Edit
python classify_with_cot.py
4. Run Streamlit App
bash
Copy
Edit
streamlit run app.py
📌 Next Steps
 Zero-Shot Summarization

 Chain-of-Thought Reasoning

 Streamlit Deployment

 Add RAG-based Answering

 LLMOps + Deployment (FastAPI, Docker)

 HuggingFace/Streamlit Cloud Deployment

👤 Author
Shubham Yedekar
Built with ❤️ and GPT.

