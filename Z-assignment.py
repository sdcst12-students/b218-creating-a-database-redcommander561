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
cursor.execute("""
create table if not exists visits (
    id integer primary key autoincrement,
    ownerid int,
    petid int,
    details text,
    cost real,
    paid real,
    foreign key (ownerid) references customers(id),
    foreign key (petid) references pets(id)
);
""")
connection.commit()
print("Tables created successfully")

connection.close()