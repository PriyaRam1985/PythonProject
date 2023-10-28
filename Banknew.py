import mysql.connector as  mc
con=mc.connect(host="localhost",username="root",database="mysql",password="admin")
def openAcc():
    ac=input("Enter the Account NO:")
    n=input("Enter Name:")
    dob=input("Enter the DOB:")    
    address=input("Enter the Address:")
    ph=input("Enter the Phone NO:")
    OpeningBalance=int(input("Enter Opening Balance"))
    data1=(ac,n,dob,address,ph,OpeningBalance)
    data2=(ac,n,OpeningBalance)
    sql1='insert into accountnew values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amountnew values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print("Data Entered Successfuuly")
    main()
def depositAcc():
    ac=input("Enter the Account NO:")
    amount=int(input("Enter the amount"))
    a="select balance from amountnew where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]+amount
    query="update amountnew set balance=%s where acno=%s"
    d=(tam,ac)
    c.execute(query,d)
    con.commit()
    print("Data updated Successfuuly")
    main()
   
def withdrawlamount():
    ac=input("Enter the Account NO:")
    amount=int(input("Enter the amount"))
    a="select balance from amountnew where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-amount
    query="update amountnew set balance=%s where acno=%s"
    d=(tam,ac)
    c.execute(query,d)
    con.commit()
    print("Amount withdrawl successfully")
    main()
    
def balance():
    ac=input("Enter the Account NO:")
    a="select balance from amountnew where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("Balance for account",ac,"is",myresult[0])
    main()
   
def display():
   ac=input("Enter the Account NO:")
   a="select * from accountnew where acno=%s"
   data=(ac,)
   c=con.cursor()
   c.execute(a,data)
   myresult=c.fetchone()
   for i in myresult:
    print(i,end=" ")
    main()

def closeac():
   ac=input("Enter the Account NO:")
   sql1="delete from accountnew where ac=%s"
   sql2="delete from amountnew where ac=%s"
   data=(ac,)
   c=con.cursor()
   c.execute(sql1,data)
   c.execute(sql2,data)
   con.commit()
   main()

def main():
            print("""
            1.OPEN A NEW ACCOUNT
            2.DEPOSIT AMOUNT
            3.WITHDRAW AMOUNT
            4.BALANCE ENQUIRY
            5.DISPLAY CUSTOMERDETAILS
            6.CLOSE AN ACCOUNT
            """)
            choice=input("Enter Task No")
            while True:
                if(choice=='1'):
                  openAcc()
                
                if(choice=='2'):
                  depositAcc()
                
                if(choice=='3'):
                  withdrawlamount()
                
                if(choice=='4'):
                  balance()
                
                if(choice=='5'):
                  display()
                
                if(choice=='6'):
                  closeac()
                
                else:
                   print("Wrong Choice")
                   main()
                   

main()

    

