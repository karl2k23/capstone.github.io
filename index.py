import pymysql

# Database connection details
servername = "localhost"
username = "id21695186_esp8266_files_sison"
password = "Database@2k23"
dbname = "id21695186_esp8266_files"

# Connect to the database
conn = pymysql.connect(host=servername, user=username, password=password, database=dbname)
cursor = conn.cursor()

# SQL query
sql = "SELECT id, waterlevel, temperature, humidity, timestamp FROM ESPDATA ORDER BY id DESC"

# Execute the query
cursor.execute(sql)

# Fetch all rows
rows = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()

# Generate HTML table
html_content = """
<!DOCTYPE html>
<html>
<body>
<table cellspacing="5" cellpadding="5">
  <tr>
    <td>ID</td>
    <td>Water Level</td>
    <td>Temperature</td>
    <td>Humidity</td>
    <td>Timestamp</td>
  </tr>
"""

for row in rows:
    html_content += """
  <tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
  </tr>
""".format(row[0], row[1], row[2], row[3], row[4])

html_content += """
</table>
</body>
</html>
"""

# Write the HTML content to a file
with open("output.html", "w") as file:
    file.write(html_content)

print("HTML file generated: output.html")
