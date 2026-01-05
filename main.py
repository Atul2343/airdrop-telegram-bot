import feedparser
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL")

feed = feedparser.parse("https://airdrops.io/feed/")
entry = feed.entries[0]

msg = (
    "🚨 NEW AIRDROP ALERT 🚨\n\n"
    f"🔥 {entry.title}\n\n"
    f"🔗 Join Airdrop:\n{entry.link}\n\n"
    "#Airdrop #Crypto"
)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(url, data={
    "chat_id": CHANNEL,
    "text": msg
})

print(response.text)
