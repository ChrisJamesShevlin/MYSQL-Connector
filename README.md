# MySQL Database Connection Script in Python

This repository contains a Python script that demonstrates how to establish a connection to a MySQL database, execute a SQL query, and fetch results using the `mysql-connector-python` library.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Error Handling](#error-handling)
- [License](#license)

## Overview

This script connects to a MySQL database, runs a SQL query to fetch all rows from a specific table, and prints the results to the console. The script includes connection setup, querying, and proper closing of the database connection.

## Prerequisites

Before running this script, ensure the following:

- **MySQL Server**: A running instance of MySQL server.
- **Database Access**: Credentials (host, database name, username, and password) to access the MySQL database.
- **Python**: Python 3 installed on your machine.
- **MySQL Connector**: The `mysql-connector-python` package installed.

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/mysql-connection-example.git
   cd mysql-connection-example
   ```

2. **Install the MySQL connector**:
   Install the MySQL connector for Python using `pip`:
   ```bash
   pip install mysql-connector-python
   ```

3. **Set up the MySQL Database**:
   Ensure you have access to the MySQL server, with a database and table to query.

## Usage

To use this script, follow these steps:

1. **Update the Connection Details**:
   In the script, update the following placeholders with your actual MySQL server details:

   ```python
   conn = mysql.connector.connect(
       host='***.*.*.*',       # Replace with your MySQL server IP or hostname
       port=3306,              # MySQL server port
       database='NAME',         # Name of your database
       user='NAME',             # MySQL username
       password='BLANK'         # MySQL password
   )
   ```

   Similarly, update the placeholder for the table you want to query:
   ```python
   cursor.execute('SELECT * FROM *TABLE*')  # Replace *TABLE* with your table name
   ```

2. **Run the Script**:
   Execute the script to connect to your MySQL database and fetch the rows from the specified table:
   ```bash
   python mysql_connection.py
   ```

### Example Output:
If the connection is successful and there are rows in the table, the output will look something like this:

```bash
Connected to MySQL database
(1, 'John', 'Doe', '2024-01-01')
(2, 'Jane', 'Smith', '2024-01-02')
MySQL connection is closed
```

## Customization

1. **Change the SQL Query**:
   You can modify the SQL query to fetch specific data or use more complex queries. For example:
   ```python
   cursor.execute('SELECT column1, column2 FROM *TABLE* WHERE condition')
   ```

2. **Adjust Fetching Behavior**:
   By default, `fetchall()` retrieves all the rows. If you only need a few rows or want to process data in chunks, consider using `fetchone()` or `fetchmany()`:
   ```python
   rows = cursor.fetchmany(10)  # Fetch 10 rows at a time
   ```

3. **Logging**:
   You can add logging to track script execution, query times, or database connections instead of printing directly to the console.

## Error Handling

The script includes basic error handling to catch issues like connection failures, query errors, or missing tables. If an error occurs, the exception message will be printed, and the connection will be closed gracefully.

Example of error handling:
```python
except Error as e:
    print(f"Error: {e}")
```

This ensures that the MySQL connection is properly closed in the `finally` block:
```python
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print('MySQL connection is closed')
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

---

Feel free to contribute to this repository by opening an issue or submitting a pull request if you have suggestions or improvements.
