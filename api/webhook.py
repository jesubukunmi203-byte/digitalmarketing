import os
import json
import requests
from http.server import BaseHTTPRequestHandler

# Environment Variable for your Bot Token (Set in Vercel Dashboard)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{TOKEN}/"

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        update = json.loads(post_data.decode('utf-8'))

        if "message" in update:
            chat_id = update["message"]["chat"]["id"]
            text = update["message"].get("text", "")

            # Simple Functional Logic
            if text == "/start":
                send_message(chat_id, 
                    "Welcome to the Digital Marketing Helper.\n\n"
                    "Use these commands:\n"
                    "/checklist - Ad compliance tips\n"
                    "/tips - Quick marketing advice\n"
                    "/help - Show this menu"
                )
            elif text == "/checklist":
                send_message(chat_id, 
                    "✅ Telegram Ads Checklist:\n"
                    "1. Profile image & description complete.\n"
                    "2. No third-party redirects.\n"
                    "3. Clear match between ad text and bot content.\n"
                    "4. No gambling or prohibited content.\n"
                    "5. Bot responds to commands on mobile."
                )
            elif text == "/tips":
                send_message(chat_id, 
                    "💡 Quick Tip:\n"
                    "Focus on one clear benefit. Avoid vague claims. "
                    "Ensure your bot is interactive and not just a redirect."
                )
            else:
                send_message(chat_id, "Command not recognized. Tap /start.")

        self.send_response(200)
        self.end_headers()

def send_message(chat_id, text):
    url = API_URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)
