import mysql.connector

# pip install mysql-connector-python

"""
Connects to a MySQL database with the specified host, user, password, and database name.

Args:
    host (str): The hostname or IP address of the MySQL server.
    user (str): The username to use for the database connection.
    passwd (str): The password to use for the database connection.
    database (str): The name of the database to connect to.

Returns:
    mysql.connector.connection.MySQLConnection: A connection to the MySQL database.
"""
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "Walden0042$$",
  database = "suresh_batch"
)

cursor = db.cursor()

create_table_query = "create table if not exists student(id int,name varchar(20),marks int)"
cursor.execute(create_table_query)
print("Table Created")

id = int(input("Enter id: "))
name = input("Enter name: ")
marks = int(input("Enter marks: "))

insert_data_query = "insert into student(id,name,marks) values(%s,%s,%s)"
cursor.execute(insert_data_query,(id,name,marks))
print("Data Added")
db.commit()

display_data_query = "select * from student"
cursor.execute(display_data_query)
students =  cursor.fetchall()
print(students)

# alter_data_query = "alter table student add city varchar(20)"
# cursor.execute(alter_data_query)

for s in students:
  print(list(s))


cursor.close()
db.close()
