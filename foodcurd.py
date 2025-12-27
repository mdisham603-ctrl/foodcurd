from pymysql import*

def signup():
    try:
        user_name = input("Enter user Name: ")
        password = input("Enter password: ")
        
        conn =connect(host="localhost",user="root",password="ranham307306",database="foodbase")
        
        q= f"INSERT INTO user values('{user_name}','{password}')"
        cursor = conn.cursor()
        cursor.execute(q)
        conn.commit()
        conn.close()
        print("Signup successful! Please login now.")
        
    except Exception as e:
        print("Error:", e)
        
def login():
    try:
        user_name = input("Enter user Name: ")
        password = input("Enter password: ")
        
        conn =connect(host="localhost",user="root",password="ranham307306",database="foodbase")
        q=f"select * from user where user_name = '{user_name}' and password ='{password}'"
        
        cur = conn.cursor()

        # Check username exists or not
        cur.execute("SELECT * FROM user WHERE user_name=%s", (user_name,))
        user = cur.fetchone()

        if user is None:
            print("❌ Invalid Username")
            conn.close()
            return False

        # Username exists → check password
        cur.execute(
            "SELECT * FROM user WHERE user_name=%s AND password=%s",
            (user_name, password)
        )
        valid = cur.fetchone()
        conn.close()

        if valid:
            print("✅ Login successful!")
            return True
        else:
            print("❌ Invalid Password")
            return False

    except Exception as e:
        print("❌ Error:", e)
        return False

        
def add_item():
    try:
        ID = int(input("enter the id no:"))
        item_name = input("Enter item name: ")
        item_count = int(input("Enter item count: "))
        gst = float(input("Enter GST %: "))
        price = float(input("Enter item price: "))
        amt=item_count*price

        total = amt+(amt * gst/100)
        cash_given = float(input("Enter cash given by customer: "))
        balance = cash_given - total

        conn =connect(host="localhost",user="root",password="ranham307306",database="foodbase")
        
        q= f"INSERT INTO product values({ID},'{item_name}', {item_count}, {gst}, {price},{total},{cash_given},{balance})"
        
        
        cursor = conn.cursor()    
        cursor.execute(q)
        conn.commit()
        conn.close()
        print("Item added successfully.") 
        
    except Exception as e:
        print(e)
       
def update_menu():
    try:
        ID = int(input("enter the id no:"))
        item_name = input("Enter item name: ")
        item_count = int(input("Enter item count: "))
        price = float(input("Enter item price: "))
        
        conn =connect(host="localhost",user="root",password="ranham307306",database="foodbase")
        
        q= f"update product set item_name='{item_name}',price={price},item_count={item_count} where ID={ID}"
        
        cursor = conn.cursor()
        cursor.execute(q)
        conn.commit()
        conn.close()
        print("Item update_menu successfully." if(cursor!=0)else"invalid name") 
        
    except Exception as u:
        print(u)
        
def delete_menu():
    try:
        ID = int(input("Enter item ID: "))
        conn =connect(host="localhost",user="root",password="ranham307306",database="foodbase")
        
        q= f"delete from product where ID={ID}"
        
        cursor = conn.cursor()
        cursor.execute(q)
        conn.commit()
        conn.close()
        print("Item delete_menu successfully." if(cursor!=0)else"invalid ID") 
        
    except Exception as d:
        print(d)

def find_item_name():
    try:
        ID = int(input("enter the id no:"))
        
        
        conn =connect(host="localhost",user="root",password="ranham307306",database="foodbase")
        
        q=f"select * from product where ID={ID}"
        
        cursor = conn.cursor()
        cursor.execute(q)
        res=cursor.fetchall()
        count=0
        print("ID\t\titem_name\titem_count\tgst\t\tprice\t\ttotal\t\tcash_given\tbalance")
        for i in res:
            for j in i:
                print(j,end="\t\t")
                count=1
            print("")
        print("data found.....")
        conn.close
        if(count==0):
            print("data not found....")
        
    except Exception as d:
        print(d)
        
def print_info():
    try:
        conn =connect(host="localhost",user="root",password="ranham307306",database="foodbase")
        q=f"select * from product"
        
        c = conn.cursor()
        c.execute(q) 
        res=c.fetchall()
        count=0
        print("add_item\tupdate_menu\tdelete_menu\tdata_find")
        for i in res:
            for j in i:
                print(j,end="\t")
                count=1
                print()
                
            if(count==0):
                print("no data found")
                conn.close()
    except Exception as e:
        print(e)
    
def product():
 while(True):
    ch=int(input("1.add_item\n2.update_menu\n3.delete_menu\n4.data_find\n5.print_info\n6.exit\nselect any one choice:"))
    if(ch==1):
        print("\nAdding data processing....\n")
        add_item()
        print("\n")
    elif(ch==2):
        print("\nUpdating data processing....\n")
        update_menu()
        print("\n")
    elif(ch==3):
        print("\nDeleting data processing....\n")
        delete_menu()
        print("\n")
    elif(ch==4):
        print("\nFinding data processing....\n")
        find_item_name()
        print("\n")
    elif(ch==5):
        print("\nprint_info data processing....\n")
        print_info()
        print("\n")
    elif(ch==6):
        print("\nExiting data processing....\n")
        print("thank you...")
        break
    else:
        print("\ninvalid choice...\n")
    
def user():
 while(True):
    ch=int(input("1.signup.\n2.login.\n3.exit.\nselect any one choice:"))
    if(ch==1):
        signup()
        
    elif(ch==2):
        if login(): 
                print("login successful! Please select choise.")
                product()
                print("\n")
    elif(ch==3):
            print("\nExiting data processing....\n")
            print("thank you...")
            break
    else:
            print("\ninvalid choice...\n")
          
while(True):
    ch=int(input("1.Employee_ID.\n2.Admin_ID.\n3.exit.\nselect any one choice:")) 
    if(ch==1):
        ch=int(input("1.add_item\n2.delete_menu\n3.exit\nselect any one choice:"))
        if(ch==1):
            print("\nAdding Admindata processing....\n")
            add_item()
            print("\n")
        elif(ch==2):
            print("\nDeleting data processing....\n")
            delete_menu()
            print("\n")
        elif(ch==3):
            print("\nExiting data processing....\n")
            print("thank you...")
            break
        else:
            print("\ninvalid choice...\n")
    elif(ch==2):
        print("\nAdmin data processing....\n")
        user()
       
        print("\n")
    elif(ch==3):
        print("\nExiting data processing....\n")
        print("thank you...")
        break
    else:
        print("\ninvalid choice...\n")
            
