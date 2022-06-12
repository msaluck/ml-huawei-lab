# Define the method of connecting to the database. The SQL statement is the database operation 
# statement to be executed each time. 
def con_mysql(sql):
try:
    db = pymysql.connect("localhost", "root", "mysql", "money", charset='utf8' )
    # Use the cursor() method to obtain the operation cursor. 
    cursor = db.cursor()
    # Execute the SQL statement using the execute method.
    cursor.execute(sql)
    results = cursor.fetchone()# Query a data record.
    db.commit() # Submit the data to the database.
except Exception as e:
    db.rollback()
    print("System error")
    sys.exit()
db.close() # Close the database. 
return results
# Test method:
sql = "select * from user" 
sql = "select * from user" 
