from MySQLdb import *

try:
    conn = MySQLdb.connect(host = 'localhost',user="root",password="root",database="student")
    print("connection successful")
    
    data= "insert into student values(101,'sanket','cs',80000)"
    cur = conn.cursor()
    cur.execute(data)
    conn.commit()
    print("record inserted successfully",cur.rowcount)
    
    
except Exception as e:
    print(e)
    
    
finally:
    conn.close()
    print("connnection closed successfully")