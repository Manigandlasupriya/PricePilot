import requests

# Replace with your values
TELEGRAM_BOT_TOKEN = "7401844627:AAGdvjm3r4SJLgAfbZcJ_ZjP8pBCFqeFWbw"
TELEGRAM_CHAT_ID = "1496299175"  # Example: 1496299175

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("📬 Telegram message sent successfully")
    else:
        print(f"❌ Failed to send Telegram message: {response.status_code}")
        print(response.text)

# Example usage
send_telegram_message("Hello from my Python script!")
