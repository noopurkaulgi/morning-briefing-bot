**Morning Intelligence Briefing Bot**
An automated morning briefing system that collects and delivers curated industry news directly to email every day.

**TL;DR**

Built a cloud-based automated intelligence agent that reduces a 1–2 hour manual morning research workflow into a fully automated daily briefing delivered before the workday begins.
The system aggregates and filters live information from 15+ sources across supply chain, markets, AI, technology, and operational intelligence, automatically extracting the most relevant updates and delivering them in a structured executive-style email. The project was designed to explore how lightweight automation and LLM-integrated workflows can reduce repetitive operational tasks, improve information flow, and increase decision readiness in fast-moving environments such as transport, aviation, logistics, and infrastructure operations.

Although currently used as a market intelligence and news automation system, the same architecture can be extended into real operational environments to automate:
1. daily and weekly performance reporting
2. fleet and asset condition monitoring
3. operational exception reporting
4. engineering defect summaries
5. delay and disruption intelligence
6. maintenance trend analysis
7. commercial and financial risk briefings
8. executive KPI reporting

**Project Aim:** The project was built to reduce the time spent manually scanning multiple websites, newsletters, and news platforms each morning. Instead of checking different sources individually, the bot automatically gathers relevant updates, filters them into categories, and sends a structured briefing email before the workday begins.

**Project Overview**

The system automatically:
1. Collects news from multiple RSS feeds
2. Organises updates into topic-based categories
3. Filters relevant articles using keyword matching
4. Removes duplicate headlines
5. Delivers a concise morning briefing via email
6. Runs automatically every day using GitHub Actions

**Categories Covered**
The bot currently tracks:

1. Global Supply Chain
2. AI & Technology
3. Longevity & Health
4. Markets & Investing
5. Startups & Innovation
6. Selected Industry Twitter/X feeds

**How It Works**
1. RSS feeds are pulled from selected news sources
2. Headlines are filtered using category-specific keywords
3. Duplicate or irrelevant articles are removed
4. A formatted briefing email is generated
5. GitHub Actions triggers the workflow automatically each morning
6. The email is sent directly to the inbox using SMTP

**Technology Stack**
Python
GitHub Actions
RSS Feeds
SMTP Email Automation
Environment Variables / GitHub Secrets

**Automation Workflow**

The project is fully cloud-based. A scheduled GitHub Actions workflow runs the Python script every morning without requiring the laptop to remain switched on.
This allows the briefing to be generated and delivered automatically at a fixed time each day.

**🤖 AI Integration Note**

An earlier version of this project incorporated the Claude API to generate AI-written executive summaries for the top news stories each morning. Instead of simply forwarding headlines, the system was able to interpret articles and produce concise briefing-style summaries designed for faster decision-making and information consumption.

The current public repository uses a fully free workflow built around RSS parsing, filtering, and automation logic to keep the project lightweight and cost-efficient for continuous daily operation.

However, the architecture was intentionally designed to support LLM integration, and the summarisation layer can be re-enabled using models such as Claude or OpenAI when required.

This project was particularly valuable in understanding how AI can be applied practically within operational environments.


**Potential Use Cases**

The same concept can be adapted for:

1. Transport operations monitoring
2. Aviation and logistics intelligence
3. Commercial market tracking
4. Competitor monitoring
5. Executive morning briefings
6. Operational reporting automation

**Author**

Built as a personal automation and productivity project focused on improving information flow, reducing manual effort, and exploring practical workflow automation.
