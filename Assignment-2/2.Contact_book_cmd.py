# Create a command line contact book through which user can search for provided details

import csv
from os import path

print("\nContact Book")
# Taking the path of the current working directory
cur_dir = path.dirname(__file__)

# Joining the path with the Excel file
filename = path.join(cur_dir, "Contact_Book.csv")

# Data to be stored in CSV File
field_names = ['Name', 'Phone number', 'Email address', 'Address']

with open("Contact_Book.csv", "a") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)

print("1.Store Details\n2.Retrive Details")
ch = int(input("Enter your choice: "))

if (ch == 1):
    print("\nEnter Details -")
    name = str(input("Enter name: "))
    ph_no = int(input("Enter phone number: "))
    email_add = str(input("Enter email address: "))
    add = str(input("Enter address: "))

    # Store Data in csv file in Dictionary Format using DictWriter
    data = {'Name': name, 'Phone number': ph_no, 'Email address': email_add, 'Address': add}
    with open("Contact_Book.csv", "a") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
        csv_writer.writerow(data)

elif (ch == 2):
    print("Search details by entering:\n1.Name\n2.Phone number\n3.Email address")
    ch2 = int(input("Enter your choice: "))

    # Read CSV File using DictReader and search in respective column
    with open("Contact_Book.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=field_names)

        if (ch2 == 1):
            name = str(input("Enter name to be searched: "))

            # Search for name in the Name column in csv file
            for row in csv_reader:
                if (name == row["Name"]):
                    print("\nDetails:\nName:", row['Name'], "Phone number:", row['Phone number'], "Email Address:",
                          row['Email address'])
                else:
                    print("The Entered name is not present in the Contact list")

        elif (ch2 == 2):
            ph_no = str(input("Enter phone number to be searched: "))
            for row in csv_reader:
                if (ph_no == row["Phone number"]):
                    print("\nDetails:\nName:", row['Name'], "Phone number:", row['Phone number'], "Email Address:",
                          row['Email address'])
                else:
                    print("The Entered name is not present in the Contact list")

                    elif (ch2 == 3):
                    email_add = str(input("Enter email address to be searched: "))
                    for row in csv_reader:
                        if(email_add == int(row["Email address"])):
                    print("\nDetails:\nName:", row['Name'], "Phone number:", row['Phone number'], "Email Address:",
                          row['Email address'])
                    else:
                    print("The Entered name is not present in the Contact list")

                    else:
                    print("Invalid Input")

                    else:
                    print("Invalid Input")