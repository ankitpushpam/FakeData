# data_extraction.py
import sqlite3
import json

def extract_data_from_tables(database_url, user_table_name, order_table_name):
    conn = None
    user_records = []
    order_records = []

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_url)
        cursor = conn.cursor()

        # Extract records from the User table
        cursor.execute(f"SELECT * FROM {user_table_name}")
        user_records = cursor.fetchall()

        # Extract records from the Order table
        cursor.execute(f"SELECT * FROM {order_table_name}")
        order_records = cursor.fetchall()

    except Exception as e:
        print(f"Error extracting data: {e}")

    finally:
        if conn:
            conn.close()

    return user_records, order_records

def save_data_as_json(user_records, order_records):
    user_data = [{"user_uuid": row[0], "firstName": row[1], "lastName": row[2], "age": row[3], "order_uuid": row[4],
                  "address": row[5]} for row in user_records]
    order_data = [{"order_uuid": row[0], "user_uuid": row[1], "order_time": row[2], "shipping_address": row[3],
                   "billing_address": row[4], "product_id": row[5]} for row in order_records]

    with open("user_records.json", "w") as user_file:
        json.dump(user_data, user_file, indent=4)

    with open("order_records.json", "w") as order_file:
        json.dump(order_data, order_file, indent=4)

    print("Records saved as JSON files.")

def main():
    database_url = 'fake_data.db'
    user_table_name = 'user_table'
    order_table_name = 'order_table'

    user_records, order_records = extract_data_from_tables(database_url, user_table_name, order_table_name)
    save_data_as_json(user_records, order_records)

if __name__ == "__main__":
    main()
