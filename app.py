from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Define your AWS RDS database credentials
DB_HOST = 'http://database-1.c58xtc1jclum.us-east-1.rds.amazonaws.com'    # Replace with your RDS endpoint
DB_NAME = 'database-1'  # Replace with your database name
DB_USER = 'admin'       # Replace with your database username
DB_PASSWORD = 'Praneeth1432'   # Replace with your database password

def insert_data_to_db(user_name, user_email):
    try:
        # Establish a connection to the RDS database
        connection = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to insert data into your table
            insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
            cursor.execute(insert_query, (user_name, user_email))

            # Commit the transaction to the database
            connection.commit()

            print(f"Data inserted successfully for {user_name}!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.form['name']
        #email = request.form['email']

        # Insert data into the database
        insert_data_to_db(name) #email)

        return f"Data submitted successfully for {name}!"

if __name__ == '__main__':
    app.run(debug=True)
