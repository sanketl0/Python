import MySQLdb


class Database:
    
    def __init__(self):
        self.conn=MySQLdb.connect(host='localhost',user='root',password='root',database='student')
        print("connection successful")
        
    def insertdata(self,eid,ename,edept,esalary):
        data="insert into student values('%d' , '%s', '%s' , '%d')"
        value = (eid,ename,edept,esalary)
        self.cur=self.conn.cursor()
        self.cur.execute(data % value)
        print("Recorded successfully inserted",self.cur.rowcount)
        self.conn.commit()
        
    def closeconn(self):
        self.conn.close()
        

M = Database()
eid =int(input("Enter a emp id:"))
ename =input("enter emp name:")
edept= input("enter a department:")
esalary=int(input("Enter a salary:"))

M.insertdata(eid,ename,edpt,esalay)
M.closeconn()

