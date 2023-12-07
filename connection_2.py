# to fetch  single records from database 

import MySQLdb


try:
    conn = MySQLdb.connect(host="localhost", user='root',password='root',database='student')
    print("successfully connected to MySQL")
    
    eid = int(input('Enter emp id:'))
    data = "select  * frim employee where eid = %d"
    cur = conn.cursor()
    cur.execute(data % eid)
    result = cur.fetchone()
    if cur.rowcount == 0:
        print("________no records found_____")
    else:
        print("ID     NAME    DEPARTMENT  SALARY")
        print("%d       %s              %s                 %d"%(result[0], result[1], result[2],result[3]))
    

except Exception as e:
    print(e)
    
finally:
    conn.close()
    print("connection closed")
    
    
    
    
    #  for feching all data
    # data = "select * from employee"
    # cur = conn.cursor()
    # cur.execute(data)
    # result = cur.fetchall()
    # for row in result:
    #     print("ID     NAME    DEPARTMENT  SALARY")
    #     print("%d       %s              %s                 %d"%(result[0], result[1], result[2],result[3]))