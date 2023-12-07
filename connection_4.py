import MySQLdb
try:
    con=MySQLdb.Connect(host="localhost",user="root",password="root",database="dataflair")
    print("Connection success")
    empid=int(input("Enter employee id for delete: "))

    sql = "select * from employee where eid=%d"
    cur = con.cursor()
    cur.execute(sql % empid)
    result = cur.fetchone()
    if (cur.rowcount == 0):
        print("--------NO RECORD FOUND-----------------")
    else:
        print("ID      NAME   DEPARTMENT   SALARY")
        print("%d      %s       %s      %d" % (result[0], result[1], result[2], result[3]))
        m=input("Are You sure want to delete(yes/no):")
        if(m=='yes'):
            sql="delete from employee where eid=%d"
            cur=con.cursor()
            cur.execute(sql % empid)
            con.commit()
            print("Record Deleted...........")

except Exception as msg:
    print(msg)
finally:
    con.close()
    print("Connection close")