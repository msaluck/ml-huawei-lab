# Create database my_database. 
import pymysql 
# Connect to the database. 
db = pymysql.connect("localhost", "root", "mysql", "my_database", charset='utf8' ) 
# Use the cursor() method to obtain the operation cursor.
cursor = db.cursor()
# Execute the SQL INSERT statement.
sql = """INSERT INTO my_table(id,
           name)
           Values (1,'Ardi Wibi')"""# You only need to modify the SQL statement to be executed to
# delete or modify the data.
try: 
    # Execute the SQL statement.
    cursor.execute(sql)
    # Submit data to the database for execution.
    db.commit()
except:
    # Rollback upon an error.
    db.rollback()
# Close the database connection.
db.close()    
#   View the result in the database. 
select * from my_table; 