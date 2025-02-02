import mysql.connector as mc

con_obj=mc.connect(
    user='root',
    password='6463',
    host='localhost',
    
)

cus_obj=con_obj.cursor()

cus_obj.execute("create database friend")

print("database created")

