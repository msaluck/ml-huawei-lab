# Create database my_database. 
import pymysql 
# Connect to the database. 
db = pymysql.connect("localhost", "root", "mysql", "my_database", charset='utf8' ) 
# localhost: local connection. You can also change it to the IP address of the database
# root: MySQL database account; mysql: database password.
# my_database: name of the database to be connected.
# Use the cursor() method to obtain the operation cursor.
cursor = db.cursor()
# Execute the SQL statement using the execute method.
cursor.execute("SELECT VERSION()")
# Use the fetchone() method to obtain a data record.
data = cursor.fetchone() 
print("Database version : %s " % data)
















