# 📬 Smart Email Classifier (Prompt Engineering with OpenAI)

This project is a hands-on, real-world demonstration of how to classify and understand text messages using **prompt engineering techniques** and **GPT models**.

---

## ✅ What We've Built

- **Few-Shot Prompt Classifier**  
  A Python script that classifies SMS messages as `Spam` or `Not Spam` using GPT-3.5 with few-shot prompting.

- **Dataset Integration with KaggleHub**  
  SMS Spam Collection dataset is fetched directly using `kagglehub` and cleaned with `pandas`.

- **Secure API Usage**  
  OpenAI API key is safely managed via a `.env` file (excluded from GitHub via `.gitignore`).

- **OpenAI SDK v1.0+ Migration**  
  Code is fully compatible with the latest OpenAI SDK using `OpenAI()` client structure.

---

## 🧠 Skills Demonstrated

- ✅ **Few-Shot Prompt Engineering**
- ✅ **Zero-Shot Prompting** *(coming next)*
- ✅ **OpenAI API integration**
- ✅ **Dataset handling and real message evaluation**
- ✅ **VS Code + GitHub Workflow**

---

## 📂 Project Structure

smart-email-classifier/
├── classify_with_prompt.py # Few-shot classification script
├── load_dataset.py # KaggleHub dataset fetch & display
├── .env # API key (not included in repo)
├── .gitignore
└── README.md


---

## 🚀 How to Run

1. Clone the repo  
2. Create your `.env` file with your OpenAI API key:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx

3. Install dependencies:
```bash
pip install -r requirements.txt
Run the classifier:

bash
Copy
Edit
python classify_with_prompt.py


👤 Author
Shubham Yedekar
Built with ❤️ and a lot of learning!

yaml
Copy
Edit

---

Would you like me to create a `requirements.txt` file for you as well?

```
