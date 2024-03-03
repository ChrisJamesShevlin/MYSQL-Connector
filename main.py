Python import csv

import pandas as pd

df = pd.read_csv('source_path')

print(df.head())



import mysql.connector

mydb = {
    'host': 'localhost',
    'user': '****',
    'password': '*********',
    'database': 'database_name',
}

# Establish a connection to the MySQL database
connection = mysql.connector.connect(**mydb)

try:
    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Execute a simple SELECT query to retrieve all data from the fibonacci_table
    query = "SELECT * FROM database_name"
    cursor.execute(query)

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Print the header
    print("ID\tValue")

    # Print each row
    for row in rows:
        print(f"{row[0]}\t{row[1]}")

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
