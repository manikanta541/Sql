import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="mulesoft")
mycu = mydb.cursor()

s1="insert into student(RegNo,Name) values(%s,%s)"
d1=("17k61a05f","rushendra")
s2="insert into student(RegNo,Name) values(%s,%s)"
d2=("17k61a0522","babu")
mycu.execute(s1,d1)
mycu.execute(s2,d2)
mydb.commit()
mycu.execute("select * from student")
for i in mycu:
    print(i)
