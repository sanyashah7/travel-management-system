import pymysql as m

db=m.connect(host="localhost",user="root",password="Root@1234")
cur=db.cursor()
cur.execute("create database if not exists tat")
cur.execute("use tat")
cur.execute("create table if not exists cust(id int primary key auto_increment,first_name varchar(20),last_name varchar(20),mobline_no varchar(10),age varchar(5),person int,total int)")

def add_booking():
    fname=input("Enter your First Name: ")
    sname=input("Enter your Last Name: ")
    mnum=input("Enter your Mobile Number: ")
    age=input("Enter your Age: ")
    per=int(input("Enter number of persons travelling: "))
    kids=int(input("Enter number of kids travelling: "))
    jain=int(input("Enter people for jain food: "))
    regular=int(input("ENter people for regular food: "))
    
    print("**********TRAVEL PLACES OPTIONS**********")
    print("1.MANALI")
    print("2.RISHIKESH")
    print("3.GOA")
    
    ch=int(input("Enter Your Choice: "))
    
    if ch==1:
        print("-----PACKAGE OPTIONS------")
        print("1.October to February - 10 days and 9 nights---- 15,000 per person")
        print("2.July to August - 10 days and 9 nights---- 11,000 per person")
    
        ch=int(input("Enter Your Choice: "))
        
        if ch==1:
            op=input("Do you want to include activities (yes/no): ")
            op=op.lower()
            if op=="yes":
                cost=0
                while true:
                    
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
            
        elif ch==2:
            op=input("Do you want to include activities (yes/no): ")
            op=op.lower()
            if op=="yes":
                cost=0
                while true:
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

    if ch==2:
            print("-----PACKAGE OPTIONS------")
            print("1.October to February - 10 days and 9 nights---- 15,000 per person")
            print("2.July to August - 10 days and 9 nights---- 11,000 per person")
    
            ch=int(input("Enter Your Choice: "))
            if ch==1:
                
                op=input("Do you want to include activities (yes/no): ")
                op=op.lower()
                if op=="yes":
                    cost=0
                    while true:
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
                
            elif ch==2:
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
                
    if ch==3:
            print("-----PACKAGE OPTIONS------")
            print("1.October to February - 5 days and 4 nights---- 27,000 per person")
            print("2.July to August - 5 days and 4 nights---- 25,000 per person")
    
            ch=int(input("Enter Your Choice: "))
            if ch==1:
                
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
                
            elif ch==2:
                op=input("Do you want to include activities (yes/no): ")
                op=op.lower()
                if op=="yes":
                    cost=0
                    while True:
                        
                        print("**********TRAVEL PLACES OPTIONS**********")
                        print("1.Church site seeing--- 1,500/-")
                        print("2.Romeo Lane --- 2,2000/-")
                        print("PRESS 0 FOR FINISHING ")
                        
                        
                        p=int(input("Enter how many people will do activities: "))
                        

                
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
                
    cur.execute("insert into cust(first_name,last_name,mobline_no,age,person,total) values('"+fname+"','"+sname+"','"+mnum+"','"+age+"','"+str(per)+"','"+str(t)+"')")
    db.commit() 
    
def update_no():
    o=input("Enter the mobile no that has to be chnaged: ")
    n=input("Enter the new mobile number: ")
    cur.execute("update cust set mobline_no='"+n+"' where mobline_no='"+o+"'") 
    db.commit() 
    print("MOBILE NUMBER UPDATED!")    
    
def delete():
    mob=input("Enter mobile number to delete details: ")    
    cur.execute("delete from cust where mobline_no='"+mob+"'")
    db.commit()
    print("The Details are deleted successfully.....")
    
def display():
    cur.execute("select * from cust")
    for i in cur:
        print(i)

def search():
    mob=input("Enter Mobile Number: ")    
    cur.execute("select * from cust where mobline_no='"+mob+"'")     
    f=cur.fetchall() #fetches all rows with the same mobile number
    if f:
        print(f)
    else:
        print("No Booking found!")   
                       
def admin_menu():
    id=input("Enter Admin ID: ")
    pswd=input("Enter Admin Password: ")
    
    if id=="Admin123":
        
        if pswd=="12345":
            
            print("LOGIN SUCCESSFUL!")
            while True:
                print("*****ADMIN MENU*****")
                print("1.VIEW ALL BOOKINGS")
                print("2. DELETE BOOKINGS")
                print("0.EXIT")
                ch=int(input("Enter your choice: "))
                
                if ch==1:
                    display()
                    
                elif ch==2:
                    delete()
                elif ch==0:
                    break
                else:
                    print("Invalid choice")
        
while True:
    print("**********SANYA'S TOURS & TRAVELS**********")
    print("1.ADMIN LOGIN")
    print("2.CUSTOMER LOGIN")    
    print("0.EXIT")
    ch=int(input("Enter your choice: "))
    
    if ch==1:
        admin_menu()
    elif ch==2:
        while True:
            print("**********WELCOME**********")
            print("1.ADD BOOKINGS")
            print("2.UPDATE PHONE NUMBER")
            print("3.CANCEL BOOKING BY PHONE NUMBER")
            print("4.SEARCH BOOKING BY MOBILE NUMBER")
            print("0.EXIT")
            ch=int(input("Enter Your Choice: "))
            
            if ch==1:
                add_booking()
            elif ch==2:
                update_no()
            elif ch==3:
                delete()
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
    

    
    