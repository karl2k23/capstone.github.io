from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# Database connection details
servername = "localhost"
username = "your_username"
password = "your_password"
dbname = "your_database_name"

@app.route('/data')
def get_data():
    try:
        # Connect to the database
        conn = pymysql.connect(host=servername, user=username, password=password, database=dbname)
        cursor = conn.cursor()

        # SQL query to retrieve data
        sql = "SELECT id, waterlevel, temperature, humidity, timestamp FROM ESPDATA ORDER BY id DESC"

        # Execute the query
        cursor.execute(sql)

        # Fetch all rows
        rows = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Format fetched data into a list of dictionaries
        data = []
        for row in rows:
            data.append({
                "id": row[0],
                "waterlevel": row[1],
                "temperature": row[2],
                "humidity": row[3],
                "timestamp": row[4].strftime("%Y-%m-%d %H:%M:%S") if row[4] else ""
            })

        return jsonify({"data": data})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
