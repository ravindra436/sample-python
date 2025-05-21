from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return "App is running!", 200

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cursor = conn.cursor()
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        return f"Connected to MySQL! Current time: {result[0]}"
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
