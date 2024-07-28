import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection
    conn = mysql.connector.connect(
        host='***.*.*.*',
        port=3306,
        database='NAME',
        user='NAME',
        password='BLANK'
    )

    if conn.is_connected():
        print('Connected to MySQL database')
        
        # Create a cursor object
        cursor = conn.cursor()
        
        # Execute a query
        cursor.execute('SELECT * FROM *TABLE*')
        
        # Fetch all rows from the last executed statement
        rows = cursor.fetchall()
        
        # Print the rows
        for row in rows:
            print(row)

except Error as e:
    print(f"Error: {e}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print('MySQL connection is closed')
