
"""
Assignment:
Create a database for a veterinarian.  You will need to create your own tables and choose the variable types that best suit these fields/columns.
There will be 3 tables:
customers
    id : primary key integer
    fname: first name 
    lname: last name
    phone: phone number
    email: email address
    address: phyiscal address
    city: city where they live
    postalcode: their postal code

pets
    id: primary key integer
    name: pet name
    type: dog or cat
    breed: description of breed (example German Sheperd, Mixed, Persion)
    birthdate: birthdate of pet (could be used to calculate their age)
    ownerID: to match the ID number in customers ID

visits
    id: primary key integer
    ownerid: the id of the owner who brought in their pet. Matches primary key of owner table
    petid: the id of the pet that was brought in. Matches primary key of pets table
    details: details what the visit was about.  Could be quite lengthy!
    cost: how much was the visit
    paid: how much has been paid so far, used to find outstanding debts

Create a program that allows you to interface with this database. 
We will be doing this in parts over the next few classes.

Part 1.
Create a function that will add a new customer.  
Ask the user for their relevant details and add them to the customers table
Optional enhancements.
Ideas for Check for duplicates:
* Check to see if there is already a username with the same phone number or email before adding and warn that the customer already exists
* List all users with the same last name and ask for confirmation before adding

Create a function that will allow you to search for a customer by any part of their record.
Example: search for all customers with a specific last name
Optional Enhancements.
* search for all users that partially match a specific last name
* search for multiple criteria
"""
import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
cursor.execute("drop table if exists customers")

cursor = connection.cursor()
query = """
create table if not exists customers (
    id integer primary key autoincrement,
    fname text,
    lname text,
    phoneNum text,
    email text,
    address text, 
    city text,
    postalcode text
);
"""
cursor.execute(query)
"""---------------------------------"""
cursor = connection.cursor()
query = """
create table if not exists pets (
    id integer primary key autoincrement,
    pname text,
    type text,
    breed text,
    birthdate text,
    ownerID int,
    foreign key (ownerID) references customers(id)
    );
    """
cursor.execute(query)
"""-------------------------------"""
cursor = connection.cursor()
query = """
create table if not exists visits (
    id integer primary key autoincrement,
    ownerid int,
    petid int,
    details text,
    cost int,
    paid int,
    foreign key (ownerid) references customers(id),
    foreign key (petid) references pets(id)
);
"""
cursor.execute(query)

print("Tables created")

"""-----------------------------"""
print("add a customer")
id = input("ID: ")
fname = input("first name: ")
lname = input("last name: ")
phone = input("phone number: ")
email = input("email: ")
address = input("address: ")
city = input("city: ")
postal = input("postal code: ")

data = (id, fname, lname,phone,email,address,city,postal)


query = f"""
insert into customers (fname, lname, phoneNum, email, address, city, postalcode) 
values ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{data[6]}')
"""

cursor.execute(query)
for i in data:
    print(i)
connection.commit()

def searches():
    g = input("Do you want to search the database? (yes or no): ")
    
    if g.lower() == "yes":
        
        table = input("Do you want to search customers, pets, or visits? Type: 'customers', 'pets', or 'visits': ")
        
        if table == "customers":
            field = input("Search by: fname, lname, email, phoneNum, address, city, or postal code?: ")
            value = input(f"Enter the {field}: ")
            if field == "fname":
                cursor.execute(f"select * from customers where fname = '{value}'")
            elif field == "lname": 
                cursor.execute(f"select * from customers where lname = '{value}'")
            elif field == "email": 
                cursor.execute(f"select * from customers where email = '{value}'")
            elif field == "phoneNum": 
                cursor.execute(f"select * from customers where phoneNum = '{value}'")
            elif field == "address": 
                cursor.execute(f"select * from customers where address = '{value}'")
            elif field == "city": 
                cursor.execute(f"select * from customers where city = '{value}'")
            elif field == "postal code": 
                cursor.execute(f"select * from customers where postal code = '{value}'")
            else:
                print("Invalid field for customers.")
                return

        elif table == "pets":
            field = input("Search by: pname, breed, ownerID, birthdate, or type: ")
            value = input(f"Enter the {field}: ")
            if field == "pname":
                cursor.execute(f"select * from pets where pname = '{value}'")
            elif field == "breed": 
                cursor.execute(f"select * from pets where breed = '{value}'")
            elif field == "ownerID": 
                cursor.execute(f"select * from pets where ownerID = '{value}'")
            elif field == "birthdate": 
                cursor.execute(f"select * from pets where birthdate = '{value}'")
            elif field == "type": 
                cursor.execute(f"select * from pets where type = '{value}'")
            else:
                print("Invalid field for pets.")
                return

        elif table == "visits":
            field = input("Search by: details, cost, amount paid, ownerID, or petID: ")
            value = input(f"Enter the {field}: ")
            if field == "details":
                cursor.execute(f"select * from visits where details like '%{value}%'")
            elif field == "cost": 
                cursor.execute(f"select * from visits where cost = {value}")
            elif field == "paid": 
                cursor.execute(f"select * from visits where paid = {value}")
            elif field == "ownerID": 
                cursor.execute(f"select * from visits where ownerID = {value}")
            elif field == "petID": 
                cursor.execute(f"select * from visits where petID = {value}")
            else:
                print("Invalid field for visits.")
                return

        else:
            print("choose customers, pets, or visits. It's not that hard")
            return
        
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No results found.")
    
    elif g.lower() == "no":
        connection.close()
        exit()
    
    else:
        print("type yes or no RIGHT NOW, NOTHING ELSE ONLY YES OR NO")
    return

searches()

connection.close()
