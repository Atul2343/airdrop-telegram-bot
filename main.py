import feedparser
import requests

BOT_TOKEN = "PASTE_BOT_TOKEN"
CHANNEL = "@PASTE_CHANNEL"

feed = feedparser.parse("https://airdrops.io/feed/")

entry = feed.entries[0]

msg = f"""
🚨 NEW AIRDROP ALERT 🚨

🔥 {entry.title}

🔗 Join:
{entry.link}

#Airdrop #Crypto
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHANNEL,
    "text": msg
})
