from tkinter import *
import MySQLdb

def saveData(event):
    con=MySQLdb.Connect(host="localhost",user="root",password="root",database="dataflair")
    sql="insert into employee values('%d','%s','%s','%d')"
    cur=con.cursor()
    value=(int(txtid.get()),txtname.get(),txtdept.get(),int(txtsal.get()))
    cur.execute(sql % value)
    con.commit()
    print("record inserted: ",cur.rowcount)
    con.close()
    print("Connection close")
    txtname.insert(0,"Hi Friend")

myroot=Tk()
myroot.geometry('600x600')
myroot.maxsize(600,600)
myroot.minsize(600,600)
myroot.title("Employee Registration Form")
myroot.wm_iconbitmap('2.ico')
lb1=Label(text="Enter Employee Id:",font=('Arial,10.bold'),fg="red")
lb1.grid(row=0,column=0)
empid=IntVar()
txtid=Entry(textvariable=empid,font=('Arial,10.bold'),fg="blue")
txtid.grid(row=0,column=1)
lb1=Label(text="Enter Name:",font=('Arial,10.bold'),fg="red")
lb1.grid(row=1,column=0)
empname=StringVar()
txtname=Entry(textvariable=empname,font=('Arial,10.bold'),fg="blue")
txtname.grid(row=1,column=1)
lb3=Label(text="Enter Department:",font=('Arial,10.bold'),fg="red")
lb3.grid(row=3,column=0)
empdept=StringVar()
txtdept=Entry(textvariable=empdept,font=('Arial,10.bold'),fg="blue")
txtdept.grid(row=3,column=1)
lb4=Label(text="Enter Salary:",font=('Arial,10.bold'),fg="red")
lb4.grid(row=4,column=0)
empsal=IntVar()
txtsal=Entry(textvariable=empsal,font=('Arial,10.bold'),fg="blue")
txtsal.grid(row=4,column=1)
txtsal.bind('<Return>',saveData)
btnsave=Button(text='Save',font=('Verdana,10.bold'),fg="black",command=lambda :saveData(0))
btnsave.grid(row=5,column=1)

myroot.mainloop()