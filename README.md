# NewsChatBot

**NewsChatBot** is a web application that aggregates RSS news feeds and generates concise summaries using Natural Language Processing (NLP) techniques.  
The application is built with **Python** and **Streamlit**, making it lightweight, interactive, and easy to deploy.

---

## Features
- Aggregates news articles from multiple RSS feeds  
- Generates concise summaries using NLP  
- Provides an interactive and user-friendly interface with Streamlit  
- Lightweight and easy to run locally or deploy online  
- Option to add or modify RSS feed sources  

---

## Installation and Setup

To run the project locally, follow the steps below:

1. **Clone the repository**
   git clone https://github.com/Nagamrithula15/NewsChatBot.git
   cd NewsChatBot
2. **Create a virtual environment (optional but recommended)**
  python -m venv venv
  source venv/bin/activate   # On Linux/Mac
  venv\Scripts\activate      # On Windows
3. **Install dependencies** 
  pip install -r requirements.txt
4. **Run the Streamlit application**
  streamlit run app.py

---

## Technology Stack
1.Python – Core programming language
2. Streamlit – Framework for building the web interface
3. NLP Libraries – NLTK, SpaCy, or Hugging Face Transformers (for text summarization)
4.Feedparser – For handling RSS feeds

---

## Project Structure
NewsChatBot/
│── app.py              # Main Streamlit application
│── requirements.txt    # List of dependencies
│── utils/              # Helper functions (NLP, RSS parsing, etc.)
│── README.md           # Project documentation

---

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code with attribution.

---

## Acknowledgements
1. Streamlit
2. NLTK
3. SpaCy
4. Feedparser
5. Open-source NLP and RSS feed providers
