import mysql.connector as mc

can_obj = mc.connect(
    user="root",
    password="6463",
    host="localhost"
)

print(can_obj)
cur_obj=can_obj.cursor()
# cur_obj.execute("show databases")
# cur_obj.execute("create table students.std_info(usn varchar(30),name varchar(30),degree varchar(30),stream varchar(30),marks int(10),grade varchar(10))")

query="insert into students.std_info(usn,name,degree,stream,marks,grade) values(%s,%s,%s,%s,%s,%s)"

# values=[
#     ('A01', 'LEO', 'B.TECH', 'IT', 85,'A'),
#     ('A02', 'VERRA', 'B.TECH', 'IT', 67,'A'),
#     ('A01', 'DEVA', 'B.TECH', 'CSE', 55,'B'),
#     ('A01', 'ROLEX', 'B.E', 'ECE', 75,'C')
    
# ]
usn=input("enter a userno")
name=input("enter a name")
degree=input("enter a degree")
stream=input("enter a stream")
marks=int(input("enter a marks"))
grade=input("enter a grade")
values=[
    (usn,name,degree,stream,marks,grade)
]
cur_obj.executemany(query,values)
can_obj.commit()

# for i in cur_obj:
#     print(i)