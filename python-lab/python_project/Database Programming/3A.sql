# Create database my_database. 
import pymysql 
# Connect to the database. 
db = pymysql.connect("localhost", "root", "mysql", "my_database", charset='utf8' ) 
# Use the cursor() method to obtain the operation cursor
cursor = db.cursor()
# SQL statement for creating a data table.
sql = """CREATE TABLE my_table (
    id int,
     name varchar(50))"""
# Run the following commands:
cursor.execute(sql) 
# Close the database connection.
db.close()








