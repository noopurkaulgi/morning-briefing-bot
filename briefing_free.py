import feedparser
import smtplib
from email.mime.text import MIMEText
import os
from datetime import datetime, timedelta
import time

# ---------------- RSS FEEDS ----------------
RSS_FEEDS = {
    "Global Supply Chain": [
        "https://www.supplychaindigital.com/rss.xml",
        "https://www.freightwaves.com/news/feed",
        "https://www.theloadstar.com/feed/",
        "https://www.joc.com/rss.xml"
    ],
    "AI Developments": [
        "https://www.technologyreview.com/feed/",
        "https://venturebeat.com/category/ai/feed/",
        "https://www.theverge.com/rss/index.xml"
    ],
    "Longevity & Health": [
        "https://www.longevity.technology/feed/",
        "https://www.medicalnewstoday.com/rss",
        "https://www.health.harvard.edu/blog/feed"
    ],
    "Tech & Startups": [
        "https://techcrunch.com/feed/",
        "https://thenextweb.com/feed/",
        "https://feeds.feedburner.com/entrepreneur/latest"
    ],
    "Markets & Investing": [
        "https://www.cnbc.com/id/100003114/device/rss/rss.html",
        "https://www.ft.com/markets?format=rss",
        "https://www.marketwatch.com/rss/topstories"
    ],
    "Top Tweets": [
        "https://nitter.net/OpenAI/rss",
        "https://nitter.net/sama/rss",
        "https://nitter.net/FT/rss"
    ]
}

# ---------------- KEYWORDS FILTER ----------------
KEYWORDS = {
    "Global Supply Chain": [
        "supply chain","logistics","shipping","freight","inventory",
        "warehouse","manufacturing","procurement","port","cargo",
        "semiconductor","factory","transport","rail","automotive"
    ],

    "AI Developments": [
        "ai","artificial intelligence","llm","chatgpt","openai",
        "automation","machine learning","robot","nvidia","copilot"
    ],

    "Longevity & Health": [
        "longevity","diet","exercise","sleep","health","nutrition",
        "aging","fitness","protein","mental health","wellness"
    ],

    "Tech & Startups": [
        "startup","funding","venture","ipo","saas",
        "innovation","product","platform","technology"
    ],

    "Markets & Investing": [
        "stock","market","inflation","interest rates","fed",
        "earnings","shares","investment","economy","oil","crypto"
    ],

    "Top Tweets": [
        "ai","startup","supply chain","market","economy",
        "future","technology","automation","innovation"
    ]
}

# ---------------- FETCH NEWS ----------------
def fetch_news():
    briefing = ""
    cutoff_time = datetime.utcnow() - timedelta(hours=24)

    for section, feeds in RSS_FEEDS.items():
        briefing += f"🌟 {section.upper()}\n"
        collected = []

        for feed_url in feeds:
            feed = feedparser.parse(feed_url)

            for entry in feed.entries:

                # ---------------- DATE FILTER ----------------
                if hasattr(entry, "published_parsed") and entry.published_parsed:
                    published_time = datetime.fromtimestamp(
                        time.mktime(entry.published_parsed)
                    )

                    if published_time < cutoff_time:
                        continue
                else:
                    continue

                title = entry.title.lower()

                # ---------------- KEYWORD FILTER ----------------
                if any(word in title for word in KEYWORDS[section]):
                    collected.append(f"- {entry.title}\n  {entry.link}")

        # remove duplicates and keep top 3
        unique_news = list(dict.fromkeys(collected))[:3]

        if unique_news:
            briefing += "\n".join(unique_news)
        else:
            briefing += "- No major updates in last 24h"

        briefing += "\n\n"

    return briefing

# ---------------- EMAIL ----------------
def send_email(body):
    EMAIL = os.environ["EMAIL"]
    PASSWORD = os.environ["EMAIL_PASSWORD"]

    msg = MIMEText(body)
    msg['Subject'] = "Your Morning Briefing ☀️"
    msg['From'] = EMAIL
    msg['To'] = EMAIL

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    server.quit()

# ---------------- MAIN ----------------
if __name__ == "__main__":
    briefing = fetch_news()
    print("Briefing generated, sending email...")
    send_email(briefing)
    print("Email sent successfully!")
