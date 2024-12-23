import mysql.connector as mc
try:
   con_obj=mc.connect(
    user="root",
    password="6463",
    host="localhost"
   )

   cur_obj=con_obj.cursor()
   cur_obj.execute("update employee.emp_info set sal =sal+bfix*4000 where bfix>=3")
   con_obj.commit()
# cur_obj.execute("create database employee")

# cur_obj.execute("show databases")
# cur_obj.execute("create table employee.emp_info(id varchar(20),name varchar(20),sal int(10),bfix int(4) )")

# for db in cur_obj:
    # print(db)
# query="insert into employee.emp_info (id,name,sal,bfix) values(%s,%s,%s,%s)"

# values=[
#     ("A11","LEO",50000,3),
#     ("A12","ROLEX",23000,4),
#     ("A13","VIKRAM",29000,5),
#     ("A14","DELHI",30000,6)
# ]
# cur_obj.executemany(query,values)
        
except Exception as e:
    print(e)