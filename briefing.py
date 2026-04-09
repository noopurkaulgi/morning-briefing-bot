import requests
import datetime
import os

CLAUDE_API_KEY = os.environ["CLAUDE_API_KEY"]

def get_rss_articles(url):
    import feedparser
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries[:5]:
        articles.append(entry.title + " - " + entry.link)
    return articles

def collect_news():
    sources = {
        "supply_chain": "https://www.ft.com/supply-chain?format=rss",
        "ai": "https://www.technologyreview.com/feed/",
        "tech": "https://techcrunch.com/feed/",
        "markets": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
        "health": "https://longevity.technology/feed/"
    }

    all_news = []
    for src in sources.values():
        all_news += get_rss_articles(src)

    return "\n".join(all_news)

def ask_claude(news_text):
    url = "https://api.anthropic.com/v1/messages"
    
    prompt = f"""
You are my personal morning briefing assistant.

Create my daily briefing in this format:

🌍 GLOBAL SUPPLY CHAIN
🤖 AI DEVELOPMENTS
🧬 LONGEVITY & HEALTH
🚀 TECH & STARTUPS
📈 MARKETS & INVESTING
🎯 BIG PICTURE

Here is the news:
{news_text}
"""

    headers = {
        "x-api-key": CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    json_data = {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 2000,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=json_data)
    return response.json()["content"][0]["text"]

def send_email(text):
    import smtplib
    from email.mime.text import MIMEText

    EMAIL = os.environ["EMAIL"]
    PASSWORD = os.environ["EMAIL_PASSWORD"]

    msg = MIMEText(text)
    msg["Subject"] = "Your 06:06 Morning Briefing ☀️"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    server.quit()

news = collect_news()
briefing = ask_claude(news)
send_email(briefing)
