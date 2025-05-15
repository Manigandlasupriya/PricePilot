import time
from tracker.scraper import get_price
from tracker.database import save_to_mysql
from tracker.config import product_urls,PRICE_THRESHOLD
from tracker.email_alert import send_email
from bot.telegram_bot import send_telegram_message
from datetime import datetime
# ChromeDriver path
chromedriver_path = "D:\\python project\\chromedriver-win64\\chromedriver.exe"

for url in product_urls:
    price = get_price(url)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - Price for {url}: ₹{price}")
    
    save_to_mysql(url, price, timestamp)

    if price < PRICE_THRESHOLD:
        message = f"🔔 Price Drop Alert!\n{url}\nCurrent Price: ₹{price}"
        send_email("Price Drop Alert!", message)
        send_telegram_message(message)
