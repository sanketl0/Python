import MySQLdb
class MyDataBase:
    def __init__(self):
        self.con=MySQLdb.Connect(host="localhost",user="root",password="root",database="dataflair")
        print("Connection success")

    def autoId(self):
        self.maxid=100
        sql="select max(eid) from employee"
        self.cur=self.con.cursor()
        self.cur.execute(sql)
        result=self.cur.fetchone()
        self.maxid=result[0]
        self.maxid=id=self.maxid+1


    def insertData(self,empname,empdept,empsal):
        self.autoId()
        sql="insert into employee values('%d','%s','%s','%d')"
        value=(self.maxid,empname,empdept,empsal)
        self.cur=self.con.cursor()
        self.cur.execute(sql % value)
        print("record inserted: ",self.cur.rowcount)
        self.con.commit()

    def searchAll(self):
        sql="select * from employee"
        self.cur=self.con.cursor()
        self.cur.execute(sql)
        result=self.cur.fetchall()
        print("---------------------------------------------")
        print("ID     NAME      DEPARTMENT            SALARY")
        for row in result:
            print("---------------------------------------------")
            print("%d        %s       %s        %d"%(row[0],row[1],row[2],row[3]))

    def searchById(self,empid):
        sql="select * from employee where eid=%d"
        self.cur=self.con.cursor()
        self.cur.execute(sql % empid)
        result=self.cur.fetchone()
        if(self.cur.rowcount==0):
            print("----------No Record Found----------")
        else:
            print("ID     NAME      DEPARTMENT            SALARY")
            print("---------------------------------------------")
            print("%d        %s       %s        %d" % (result[0], result[1], result[2], result[3]))

    def deleteById(self,empid):
        sql = "select * from employee where eid=%d"
        self.cur = self.con.cursor()
        self.cur.execute(sql % empid)
        result = self.cur.fetchone()
        if (self.cur.rowcount == 0):
            print("----------No Record Found----------")
        else:
            print("ID     NAME      DEPARTMENT            SALARY")
            print("---------------------------------------------")
            print("%d        %s       %s        %d" % (result[0], result[1], result[2], result[3]))
            choice=input("Are You sure want to delete(yes/no) :")
            if(choice=='yes'):
                sql="delete from employee where eid=%d"
                self.cur=self.con.cursor()
                self.cur.execute(sql % empid)
                self.con.commit()
                print("Record deleted.........")

    def __del__(self):
        print("Connection close")
        self.con.close()

#Calling Place
ch=0
M1=MyDataBase()
while(ch!=5):
    print("---------------Database Menu----------------")
    print("1.Insert Record")
    print("2.Search Record By Id")
    print("3.Search All Record")
    print("4.Delete Record By Id")
    print("5.Exit")
    print("---------------------------------------------")
    ch=int(input("Enter your Choice"))
    if(ch==1):
        ename = input("Enter Employee Name:")
        edept=input("Enter Employee Department:")
        esal = int(input("Enter Employee Salary:"))
        M1.insertData(ename,edept,esal)
    elif(ch==2):
        eid = int(input("Enter Employee Id for Search:"))
        M1.searchById(eid)
    elif(ch==3):
        M1.searchAll()
    elif(ch==4):
        eid = int(input("Enter Employee Id for Delete:"))
        M1.deleteById()

#M1=MyDataBase()
# eid = int(input("Enter Employee Id for Delete:"))
# M1.deleteById(eid)
#M1.searchById(eid)

#M1.searchAll()
# M1.autoId()
# print(" Employee ID:",M1.maxid)
# ename=input("Enter Employee Name:")
# edept=input("Enter Employee Department:")
# esal = int(input("Enter Employee Salary:"))
# M1.insertData(ename,edept,esal)