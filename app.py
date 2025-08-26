import nltk
nltk.data.path.append("./nltk_data")  # tells Python to use the folder in your project
nltk.download("punkt", download_dir="./nltk_data")
import streamlit as st
import feedparser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# RSS feed URLs
RSS_FEEDS = {
    "India": "https://www.thehindu.com/news/national/feeder/default.rss",
    "Tamil Nadu": "https://www.thehindu.com/news/national/tamil-nadu/feeder/default.rss",
    "Technology": "https://www.thehindu.com/sci-tech/technology/feeder/default.rss"
}

# Function to fetch news from RSS
def fetch_rss_news(feed_url, max_articles=5):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries[:max_articles]:
        articles.append(f"{entry.title} - {entry.summary} (Source: {entry.link})")
    return articles

# Function to summarize text
def summarize_text(text, sentences_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join([str(sentence) for sentence in summary])

# Streamlit App
st.title("📰 Free RSS News Summarizer Bot")
st.write("Ask me about the latest news! (e.g., India, Tamil Nadu, Technology)")

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if query := st.chat_input("Type your news topic (India/Tamil Nadu/Technology)..."):
    st.session_state["messages"].append({"role": "user", "content": query})
    st.chat_message("user").write(query)

    # Select RSS feed
    feed_url = RSS_FEEDS.get(query, RSS_FEEDS["India"])
    news_articles = fetch_rss_news(feed_url)

    if news_articles:
        combined_text = " ".join(news_articles)
        summary = summarize_text(combined_text, sentences_count=3)
    else:
        summary = "Sorry, no recent news found for this topic."

    # Show summary
    st.session_state["messages"].append({"role": "assistant", "content": summary})
    st.chat_message("assistant").write(summary)
