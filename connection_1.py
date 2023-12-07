import MySQLdb

try:
    conn = MySQLdb.connect(host="localhost", user='root',password='root',database='student')
    print("successfully connected to MySQL")
    
    eid = int(input('Enter emp id:'))
    ename = input("enter a emp name:")
    edpt = input("Enter department")
    esalary = int(input("enter emp salary:"))
    
    data = "insert into employee values('%d,'%s','%s'.'%d')"
    value =(eid,ename,edpt,esalary)
    cur = conn.cursor()
    cur.execute(data % value)
    conn.commit()
    print("record inserted ",cur.rowcount)


except Exception as e:
    print(e)
    
    
finally:
    conn.close()
    print("connection closed")