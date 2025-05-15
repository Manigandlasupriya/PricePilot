import mysql.connector
from tracker.config import DB_CONFIG

def save_to_mysql(product_url, price, timestamp):
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        query = "INSERT INTO price_history (product_url, price, timestamp) VALUES (%s, %s, %s)"
        cursor.execute(query, (product_url, price, timestamp))
        connection.commit()
        print("✅ Data saved to MySQL.")
    except mysql.connector.Error as err:
        print(f"❌ MySQL Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
