import pymysql as m

db=m.connect(host="localhost",user="root",password="Root@1234")
cur=db.cursor()
cur.execute("create database if not exists tat")
cur.execute("use tat")
cur.execute("create table if not exists cust(id int primary key auto_increment,first_name varchar(20),last_name varchar(20),mobline_no varchar(10),age varchar(5),person int,total int)")


def add_booking(mob,fname,lname):
    
    age=input("Enter your age: ")
    per=int(input("Enter number of persons travelling: "))
    kids=int(input("Enter number of kids travelling: "))
    jain=int(input("Enter people for jain food: "))
    regular=int(input("ENter people for regular food: "))
    
    print("**********TRAVEL PLACES OPTIONS**********")
    print("1.MANALI")
    print("2.RISHIKESH")
    print("3.GOA")
    
    pc=int(input("Enter Your Choice: "))
    place=""
    package_no=0
    if pc == 1:
        place = "MANALI"
    elif pc == 2:
        place = "RISHIKESH"
    elif pc == 3:
        place = "GOA"
    else:
        print("Invalid choice")
        return
    
    if pc==1:
        print("-----PACKAGE OPTIONS------")
        print("1.October to February - 10 days and 9 nights---- 15,000 per person")
        print("2.July to August - 10 days and 9 nights---- 11,000 per person")
    
        pk=int(input("Enter Your Choice: "))
        if pk==1:
            package_no=1
        elif pk==2:
            package_no=2
        else:
            print("Invalid choice")
            return
        if pk==1:
            op=input("Do you want to include activities(yes/no): ")
            op=op.lower()
            if op=="yes":
                cost=0
                while True:
                    
                    print("**********TRAVEL PLACES OPTIONS**********")
                    print("1.River Crossing--- 500/-")
                    print("2.Camping--- 1,2000/-")
                    print("3.skiing--- 2,000/-")
                    print("PRESS 0 FOR FINISHING")
                    
                    ch=int(input("Enter Your Choice: "))
                
                    
                    if ch==1:
                        p=int(input("Enter how many people will do activities: "))
                        cost=cost+(500*p)
                    elif ch==2:
                        p=int(input("Enter how many people will do activities: "))
                        cost=cost+(1200*p)
                    elif ch==3:
                        p=int(input("Enter how many people will do activities: "))
                        cost=cost+(2000*p)
                    elif ch==0:
                        break
                    else:
                        print("Invalid choice")
                    
                print("The activities charge is: ",cost)
                
                print("********BILLING DETAILS********")
                
                fcost=(jain*400)+(regular*450)
                pcost=(15000*per)
                t=fcost+pcost+cost
                print("FOOD COST: ",fcost)
                print("ACTIVITY COST: ",cost)
                print("PACKAGE COST: ",pcost)
                print("TOTAL AMOUNT IS ",t)
            
            elif op=="no":
                print("********BILLING DETAILS********")
                
                fcost=(jain*400)+(regular*450)
                pcost=(15000*per)
                t=fcost+pcost
                print("FOOD COST: ",fcost)
                print("PACKAGE COST: ",pcost)
                print("TOTAL AMOUNT IS ",t)
            else:
                print("Invalid choice")
            
        elif pk==2:
            op=input("Do you want to include activities (yes/no): ")
            op=op.lower()
            if op=="yes":
                cost=0
                while True:
                    print("**********TRAVEL PLACES OPTIONS**********")
                    print("1.River Crossing--- 500/-")
                    print("2.Camping--- 1,2000/-")
                    print("3.skiing--- 2,000/-")
                    print("PRESS 0 FOR FINISHING")
                
                    ch=int(input("Enter Your Choice: "))
                    
                    

                    
                
                    if ch==1:
                        p=int(input("Enter how many people will do activities: "))
                        cost=cost+(500*p)
                        
                    elif ch==2:
                        p=int(input("Enter how many people will do activities: "))
                        cost=cost+(1200*p)
                    elif ch==3:
                        p=int(input("Enter how many people will do activities: "))
                        cost=cost+(2000*p)
                    elif ch==0:
                        break
                    else:
                        print("Invalid choice")
                
                print("The activities charge is: ",cost)
            
                print("********BILLING DETAILS********")
            
                fcost=(jain*400)+(regular*450)
                pcost=(11000*per)
                t=fcost+pcost+cost
                print("FOOD COST: ",fcost)
                print("ACTIVITY COST: ",cost)
                print("PACKAGE COST: ",pcost)
                print("TOTAL AMOUNT IS ",t)
                
            elif op=="no":
                print("********BILLING DETAILS********")
                
                fcost=(jain*400)+(regular*450)
                pcost=(15000*per)
                t=fcost+pcost
                print("FOOD COST: ",fcost)
                print("PACKAGE COST: ",pcost)
                print("TOTAL AMOUNT IS ",t)
            else:
                print("Invalid choice")
                
        else:
            print("Invalid Choice")

    elif pc==2:
            print("-----PACKAGE OPTIONS------")
            print("1.October to February - 10 days and 9 nights---- 15,000 per person")
            print("2.July to August - 10 days and 9 nights---- 11,000 per person")
    
            pk=int(input("Enter Your Choice: "))
            if pk==1:
                package_no=1
            elif pk==2:
                package_no=2
            else:
                print("Invalid choice")
                return
            if pk==1:
                
                op=input("Do you want to include activities (yes/no): ")
                op=op.lower()
                if op=="yes":
                    cost=0
                    while True:
                        print("**********TRAVEL PLACES OPTIONS**********")
                        print("1.River Crossing--- 500/-")
                        print("2.Camping--- 1,2000/-")
                        print("PRESS 0 FOR FINISHING")
                
                    
                        ch=int(input("Enter Your Choice: "))
                      
                        if ch==1:
                            p=int(input("Enter how many people will do activities: "))
                            cost=cost+(500*p)
                        elif ch==2:
                            p=int(input("Enter how many people will do activities: "))
                            cost=cost+(1200*p)
                        elif ch==0:
                            break
                    
                        else:
                            print("Invalid choice")
                    
                    print("The activities charge is: ",cost)
                
                    print("********BILLING DETAILS********")
                    
                    fcost=(jain*400)+(regular*450)
                    pcost=(15000*per)
                    t=fcost+pcost+cost
                    print("FOOD COST: ",fcost)
                    print("ACTIVITY COST: ",cost)
                    print("PACKAGE COST: ",pcost)
                    print("TOTAL AMOUNT IS ",t)
                
                elif op=="no":
                    print("********BILLING DETAILS********")
                    
                    fcost=(jain*400)+(regular*450)
                    pcost=(15000*per)
                    t=fcost+pcost
                    print("FOOD COST: ",fcost)
                    print("PACKAGE COST: ",pcost)
                    print("TOTAL AMOUNT IS ",t)
                else:
                    print("Invalid choice")
                
            elif pk==2:
                op=input("Do you want to include activities (yes/no): ")
                op=op.lower()
                if op=="yes":
                    cost=0
                    while True: 
                        print("**********TRAVEL PLACES OPTIONS**********")
                        print("1.River Crossing--- 500/-")
                        print("2.Camping--- 1,2000/-")
                        print("PRESS 0 FOR FINISHING")
                        
                
                        ch=int(input("Enter Your Choice: "))
                       
                
                        if ch==1:
                            p=int(input("Enter how many people will do activities: "))
                            cost=cost+(500*p)
                        elif ch==2:
                            p=int(input("Enter how many people will do activities: "))
                            cost=cost+(1200*p)
                        elif ch==0:
                            break
                        else:
                            print("Invalid choice")
                    
                    print("The activities charge is: ",cost)
                
                    print("********BILLING DETAILS********")
                
                    fcost=(jain*400)+(regular*450)
                    pcost=(11000*per)
                    t=fcost+pcost+cost
                    print("FOOD COST: ",fcost)
                    print("ACTIVITY COST: ",cost)
                    print("PACKAGE COST: ",pcost)
                    print("TOTAL AMOUNT IS ",t)
                    
                elif op=="no":
                    print("********BILLING DETAILS********")
                    
                    fcost=(jain*400)+(regular*450)
                    pcost=(15000*per)
                    t=fcost+pcost
                    print("FOOD COST: ",fcost)
                    print("PACKAGE COST: ",pcost)
                    print("TOTAL AMOUNT IS ",t)
                
                else:
                    print("Invalid choice")
                    
            else:
                print("Invalid Choice")
                
    elif pc==3:
            print("-----PACKAGE OPTIONS------")
            print("1.October to February - 5 days and 4 nights---- 27,000 per person")
            print("2.July to August - 5 days and 4 nights---- 25,000 per person")
    
            pk=int(input("Enter Your Choice: "))
            if pk==1:
                package_no = 1
            elif pk==2:
                package_no = 2
            else:
                print("Invalid choice")
                return
            if pk==1:
                
                op=input("Do you want to include activities (yes/no): ")
                op=op.lower()
                if op=="yes":
                    cost=0
                    while True:
                        
                        print("**********TRAVEL ACTIVITIES OPTIONS**********")
                        print("1.Church site seeing--- 1,500/-")
                        print("2.Romeo Lane --- 2,2000/-")
                        print("PRESS 0 FOR FINISHING")
                
                    
                        ch=int(input("Enter Your Choice: "))
                        
                        if ch==1:
                            p=int(input("Enter how many people will do activities: "))
                            cost=cost+(1500*p)
                        elif ch==2:
                            p=int(input("Enter how many people will do activities: "))
                            cost=cost+(2200*p)
                        elif ch==0:
                            break
                        else:
                            print("Invalid choice")
                
                    print("The activities charge is: ",cost)
                
                    print("********BILLING DETAILS********")
                    
                    fcost=(jain*400)+(regular*450)
                    pcost=(27000*per)
                    t=fcost+pcost+cost
                    print("FOOD COST: ",fcost)
                    print("ACTIVITY COST: ",cost)
                    print("PACKAGE COST: ",pcost)
                    print("TOTAL AMOUNT IS ",t)
                
                elif op=="no":
                    print("********BILLING DETAILS********")
                    
                    fcost=(jain*400)+(regular*450)
                    pcost=(27000*per)
                    t=fcost+pcost
                    print("FOOD COST: ",fcost)
                    print("PACKAGE COST: ",pcost)
                    print("TOTAL AMOUNT IS ",t)
                
            elif pk==2:
                op=input("Do you want to include activities (yes/no): ")
                op=op.lower()
                if op=="yes":
                    cost=0
                    while True:
                        
                        print("**********TRAVEL PLACES OPTIONS**********")
                        print("1.Church site seeing--- 1,500/-")
                        print("2.Romeo Lane --- 2,2000/-")
                        print("PRESS 0 FOR FINISHING ")
                        
                        
                        ch=int(input("Enter how many people will do activities: "))
                        
                        if ch==1:
                            p=int(input("Enter how many people will do activities: "))
                            cost=cost+(500*p)
                        elif ch==2:
                            p=int(input("Enter how many people will do activities: "))
                            cost=cost+(1200*p)
                        elif ch==0:
                            break
                        else:
                            print("Invalid choice")
                
                    print("The activities charge is: ",cost)
                
                    print("********BILLING DETAILS********")
                
                    fcost=(jain*400)+(regular*450)
                    pcost=(25000*per)
                    t=fcost+pcost+cost
                    print("FOOD COST: ",fcost)
                    print("ACTIVITY COST: ",cost)
                    print("PACKAGE COST: ",pcost)
                    print("TOTAL AMOUNT IS ",t)
                    
                elif op=="no":
                    print("********BILLING DETAILS********")
                    
                    fcost=(jain*400)+(regular*450)
                    pcost=(15000*per)
                    t=fcost+pcost
                    print("FOOD COST: ",fcost)
                    print("PACKAGE COST: ",pcost)
                    print("TOTAL AMOUNT IS ",t)
                    
            else:
                print("Invalid Choice")
                
    else:
        print("Invalid choice")
                
    cur.execute("insert into cust(first_name,last_name,mobline_no,age,person,total,place,pno) values('"+fname+"','"+lname+"','"+mob+"','"+age+"',"+str(per)+","+str(t)+",'"+place+"',"+str(package_no)+")")
    db.commit() 
    cur.execute("delete from cust where person=0")
    db.commit()
    
def update_no():
    o=input("Enter the mobile no that has to be chnaged: ")
    n=input("Enter the new mobile number: ")
    cur.execute("update cust set mobline_no='"+n+"' where mobline_no='"+o+"'") 
    db.commit() 
    print("MOBILE NUMBER UPDATED!")    
    
def delete():
    mob=input("Enter Booking ID: ")    
    cur.execute("delete from cust where id='"+mob+"'")
    db.commit()
    print("The Details are deleted successfully.....")
    
def display():
    print("The Active bookings are: ")
    cur.execute("select * from cust where total>0")
    for i in cur:
        print(i)
    print("The Cancelled bookings are: ")
    cur.execute("select * from cust where total=0")
    for j in cur:
        print(j)

def search():
    mob=input("Enter Mobile Number: ")    
    cur.execute("select * from cust where mobline_no='"+mob+"'")     
    f=cur.fetchall() #fetches all rows with the same mobile number
    if f:
        print(f)
    else:
        print("No Booking found!")  

def cancel_booking():
    mob=input("Enter mobile number to cancel booking: ")
    cur.execute("select id,total,place from cust where mobline_no='"+mob+"'")
    r=cur.fetchall()
    if not r:
        print("No booking found!")
        return
    
   
    for i in r:
        print("Booking ID:",i[0],"Amount:",i[1],"Place: ",i[2])
        
    bid=int(input("Enter Booking ID to cancel: "))
    
    cur.execute("select total from cust where id="+str(bid))
    r=cur.fetchone()
    #print(r)
    if r:
        total=int(r[0])  
        if total==0:
            print("Booking already cancelled!")
            return
        
        refund=int(total*0.8)
        print("Total amount paid for the trip:",total)
        print("Refund Amount (80%):",refund)
        cur.execute("update cust set total=0 where id="+str(bid))
        db.commit()
        print("Booking cancelled successfully!")
        print("Refund of",refund,"will be processed soon.")
    else:
        print("Invalid Booking ID")


def customer_login():
    mob=input("Enter your mobile number: ")
    cur.execute("select first_name, last_name,age from cust where mobline_no='"+mob+"'")
    data=cur.fetchone()
    
    if data:
        print("Welcome back",data[0],data[1])
        return mob,data[0],data[1]
    else:
        print("New Customer Registration")
        fname=input("Enter First Name: ")
        lname=input("Enter Last Name: ")
        age=input("Enter your age: ")
        cur.execute("insert into cust(first_name,last_name,mobline_no,age,person,total) values('"+fname+"','"+lname+"','"+mob+"','"+age+"',0,0)" )
        db.commit()
        print("Account created successfully!")
        return mob,fname,lname

    
                       
def admin_menu():
    id=input("Enter Admin ID: ")
    pswd=input("Enter Admin Password: ")
    
    if id=="Admin123":
        
        if pswd=="12345":
            
            print("LOGIN SUCCESSFUL!")
            while True:
                print("*****ADMIN MENU*****")
                print("1.VIEW ALL BOOKINGS")
                print("2.DELETE BOOKINGS")
                print("3.VIEW BOOKINGS BY PLACE") 
                print("0.EXIT")
                ch=int(input("Enter your choice: "))
                
                if ch==1:
                    display()                    
                elif ch==2:
                    delete()
                elif ch==3:
                    view_place()
                elif ch==0:
                    break
                else:
                    print("Invalid choice")
        else:
            print("Wrong Password")
    else:
        print("Wrong ID")

def view_place():
    place = input("Enter place to search: ").upper()  
    cur.execute("select first_name, last_name, person, pno FROM cust WHERE place='"+place+"' and total>0")
    r=cur.fetchall()
    if r:
        for i in r:
            print("Name:",i[0],i[1],", persons:",i[2],", Package:",i[3])
    else:
        print("No bookings found for",place)
        
while True:
    print("**********SANYA'S TOURS & TRAVELS**********")
    print("1.ADMIN LOGIN")
    print("2.CUSTOMER LOGIN")   
    print("0.EXIT")
    ch=int(input("Enter your choice: "))
    
    if ch==1:
        admin_menu()
    elif ch==2:
        mob,fname,lname=customer_login()
        while True:
            print("**********WELCOME**********")
            print("1.ADD BOOKINGS")
            print("2.UPDATE PHONE NUMBER")
            print("3.CANCEL BOOKING BY PHONE NUMBER")
            print("4.SEARCH BOOKING BY MOBILE NUMBER")
            print("0.EXIT")
            ch=int(input("Enter Your Choice: "))
            
            if ch==1:
                add_booking(mob,fname,lname)
            elif ch==2:
                update_no()
            elif ch==3:
                cancel_booking()
            elif ch==4:
                search()
            elif ch==0:
                break
            else:
                print("Invalid choice")
    
    elif ch==0:
        break
    else:
        print("Invalid choice")
    

    
    
