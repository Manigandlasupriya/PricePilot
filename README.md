# PricePilot ✨

Smart Navigation for Product Prices

PricePilot is an intelligent, automated price-tracking system that helps users monitor product prices on Amazon and receive alerts when prices drop below a set threshold. It is designed to be efficient, customizable, and easy to extend.

---

## 🌟 Features

- 🕒 Real-time price scraping using Selenium and BeautifulSoup
- 📧 Email alerts when product prices fall below threshold
- 📢 Telegram notifications for instant updates
- 📊 MySQL database integration for logging historical price data
- 🛠️ Clean, modular architecture

---

## 📁 Project Structure

```bash
smart_grocery_tracker/
├── tracker/
│   ├── main.py             # Entry point
│   ├── scraper.py          # Selenium-based price scraper
│   ├── config.py           # Product URLs and configuration variables
│   ├── database.py         # MySQL connection and storage logic
│   └── alerts.py           # Email and Telegram alert functions
└── requirements.txt         # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/PricePilot.git
cd PricePilot
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Update the values in tracker/config.py:
- Product URLs
- MySQL credentials
- Email and Telegram API keys

### 5. Run the Script
```bash
python -m tracker.main
```

---

## 📊Database Schema
Table: price_history

product_url	price	timestamp
TEXT	FLOAT	DATETIME

product_url: The URL of the Amazon product being tracked.

price: The price of the product at the time of checking.

timestamp: The date and time when the price was recorded.

Example SQL to create the table:
CREATE TABLE price_history (
    product_url TEXT NOT NULL,
    price FLOAT NOT NULL,
    timestamp DATETIME NOT NULL
);


## 🎨 Sample Output
```
2025-05-10 20:34:45 - Price for https://www.amazon.in/dp/B0DXQH1DBS: ₹59900.0
📉 Data saved to MySQL.
📧 Email alert sent
📢 Telegram message sent
```

---

## 🚫 Disclaimer
This tool is for educational purposes only. Web scraping should comply with the terms of service of the target website.

---

## 🌟 Author
Manigandla Supriya
- LinkedIn: https://www.linkedin.com/in/manigandla-supriya-64b7a3250/
- GitHub: https://github.com/Manigandlasupriya

---

## 📈 Contributions
Feel free to fork the repo, create pull requests, or submit issues!

---

## 📁 License
MIT License
