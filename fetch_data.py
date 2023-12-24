from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'host': 'sql12.freesqldatabase.com',
    'user': 'sql12672580',
    'password': 'KetWXbpE2z',
    'database': 'sql12672580'
}

@app.route('/')
def display_sensor_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        sql = "SELECT ID, TIMESTAMP, WATERLEVEL, TEMPERATURE, HUMIDITY FROM ESPDATA"
        cursor.execute(sql)
        data = cursor.fetchall()

        return render_template('display_data.html', data=data)

    except mysql.connector.Error as error:
        return f"Error: {error}"

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
