import telegram
import requests

# Secrets
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "-100XXXXXXXXXX"

bot = telegram.Bot(token=BOT_TOKEN)

# Example airdrops (dummy, replace with real scraping later)
airdrops = [
    {"name": "CryptoX Token", "link": "https://t.me/CryptoX_airdrop"},
    {"name": "BlockY Airdrop", "link": "https://t.me/BlockY_airdrop"}
]

for airdrop in airdrops:
    message = f"🚨 NEW AIRDROP ALERT 🚨\n\n🔥 {airdrop['name']}\n🔗 Join Airdrop: {airdrop['link']}"
    bot.send_message(chat_id=CHANNEL_ID, text=message)
