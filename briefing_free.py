import feedparser
import smtplib
from email.mime.text import MIMEText
import os

# ---- Your sections and RSS feeds ----
RSS_FEEDS = {
    "Global Supply Chain": [
        "https://www.supplychaindigital.com/rss.xml",
        "https://www.wsj.com/xml/rss/3_7031.xml"
    ],
    "AI Developments": [
        "https://www.technologyreview.com/feed/",
        "https://www.theverge.com/rss/index.xml"
    ],
    "Longevity & Health": [
        "https://www.medicalnewstoday.com/rss",
        "https://www.healthline.com/rss"
    ],
    "Tech & Startups": [
        "https://techcrunch.com/feed/",
        "https://thenextweb.com/feed/"
    ],
    "Markets & Investing": [
        "https://www.cnbc.com/id/100003114/device/rss/rss.html",
        "https://www.ft.com/?format=rss"
    ]
}

# ---- Function to fetch top 3 headlines per category ----
def fetch_news():
    briefing = ""
    for section, feeds in RSS_FEEDS.items():
        briefing += f"🌟 {section.upper()}\n"
        count = 0
        for feed_url in feeds:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                briefing += f"- {entry.title}\n  {entry.link}\n"
                count += 1
                if count >= 3:  # Only top 3 per section
                    break
            if count >= 3:
                break
        briefing += "\n"
    return briefing

# ---- Function to send email ----
def send_email(body):
    EMAIL = os.environ["EMAIL"]
    PASSWORD = os.environ["EMAIL_PASSWORD"]

    msg = MIMEText(body)
    msg['Subject'] = "Your 06:06 Morning Briefing ☀️"
    msg['From'] = EMAIL
    msg['To'] = EMAIL

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    server.quit()

# ---- Main ----
if __name__ == "__main__":
    briefing = fetch_news()
    print("Briefing generated, sending email...")
    send_email(briefing)
    print("Email sent successfully!")
