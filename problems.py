import json
import random
import string
from datetime import datetime


# staff class
# =========================================================================================================
class Staff:
    # __intit__ => like a constructor
    def __init__(self) -> None:
        self.staff = self.load_staff()

    def load_staff(
        self,
    ):  # method load is a method to start the file if it does not exist or read its data of it exists
        try:
            with open("staff.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):  # Handle exceptions
            return []

    # method save is a method that used to close the file after adding or updating or deleteing somthing from it
    def save_staff(self):
        with open("staff.json", "w") as f:
            json.dump(self.staff, f, indent=4)

    # add a new staff methode
    def add_staff(self):
        len = 8
        char = string.ascii_letters + string.digits
        who_is_adding = int(input("enter your id: "))
        for member in self.staff:
            if member["id"] == who_is_adding and member["job"] == "manager":
                new_member = str(input("enter the name : "))
                job = str(input("enter the job : "))
                id = "".join(random.choice(char) for _ in range(len))
                self.staff.append({"name": new_member, "job": job, "id": id})

                self.save_staff()

    # delete a staff if it exists
    def delete_staff(self):
        with open("staff.json", "r") as f:
            who_is_deleting = int(input("enter your id: "))
            for member in self.staff:
                if member["id"] == who_is_deleting and member["job"] == "manager":
                    name = str(input("enter the staff name: "))
                    for member in self.staff:
                        if member["name"] == name:
                            self.staff.remove(member)
                            self.save_staff()
                            break
                else:
                    print("you are not allowed to do such a thing")
                    break

    # update staff
    def update_staff(self):
        who_is_updating = int(input("Enter your ID: "))
        for member in self.staff:
            if member["id"] == who_is_updating:
                if member["job"] == "manager":
                    updated_id = int(
                        input("Enter the ID of the person you want to update: ")
                    )
                    for person in self.staff:
                        if person["id"] == updated_id:
                            answer = input("What do you want to update (name, job)? : ")
                            if answer == "name":
                                new_name = str(input("Enter the new name: "))
                                person["name"] = new_name
                            elif answer == "job":
                                new_job = str(input("Enter the new job: "))
                                person["job"] = new_job
                            else:
                                print("Invalid update option.")
                            self.save_staff()
                            print(
                                f"Staff member with ID {updated_id} has been updated."
                            )
                            return
                    print(f"Staff member with ID '{updated_id}' not found.")
                else:
                    print(
                        "You are not allowed to update staff. Only managers can perform this action."
                    )
                return
        print("ID not found.")

    # get all the staff
    def get_staff(self):
        who_is_getting = int(input("enter your id: "))
        for member in self.staff:
            if member["id"] == who_is_getting:
                if member["job"] == "manager":
                    print(f"{self.staff}")
                    return
        print("you are not allowed to do this only managers")

    # search for staff
    def search_for_staff(self):
        who_is_searching = int(input("enter your id: "))
        for member in self.staff:
            if member["id"] == who_is_searching and member["job"] == "manager":
                found_mamanger = True
                wanted_staff = input(
                    "enter the id,name of the user you wnat to search about: "
                )
                found = False
                for person in self.staff:
                    if wanted_staff.isdigit():
                        if person["id"] == int(wanted_staff):
                            print(person)
                            found = True
                            break
                    # Otherwise, compare as name
                    elif (
                        person["name"].lower() == wanted_staff.lower()
                    ):  # Case-insensitive name comparison
                        print(person)
                        found = True

                if not found:
                    print("Nothing found")
        if not found_mamanger:
            print("you are not allowed to do this only managers")
# ====================================end of staff class====================================================


class Books(Staff):
    def __init__(self):
        super().__init__() 
        self.books = self.load_books()
            

    def load_books(self):
        try:
            with open("Books.json","r") as f:
                return json.load(f)        
        except(FileNotFoundError,json.JSONDecodeError):
            return[]
        
    def save_books(self):
        with open("Books.json","w") as f:
            json.dump(self.books,f,indent=4)
    
    def add_books(self):
        who_is_adding = int(input("enter your id: "))
        char = string.ascii_letters + string.digits
        len = 8
        for staff in self.staff:
            if staff["id"] == who_is_adding:
                book_name = input("enter the book name: ")
                book_author = input("enter the book author: ")
                book_price = float(input("enter the book price: "))
                who_added_it = staff
                when_added_it = datetime.now().isoformat()
                book_id = ''.join(random.choice(char) for _ in range(len))
                self.books.append(
                    {
                        "book_name" : book_name,
                        "book_author" : book_author,
                        "book_price" : book_price,
                        "book_id" : book_id,
                        "who_added_it" : who_added_it,
                        "when_added_it" : when_added_it
                    }
                )
                self.save_books()
    
    
    def update_books(self):
        who_is_updating = int(input("enter your id: "))
        found_manager = False  # Move this initialization outside the for loop
        for staff in self.staff:
            if staff["id"] == who_is_updating and staff["job"] == "manager":
                found_manager = True  # Set this to True when a manager is found
                updated_book = input("enter the book id:  ")
                found = False
                for book in self.books:
                    if book["book_id"] == updated_book:
                        change_what = input("enter what do you want to change (name, author, price): ").lower()
                        if change_what == "name":
                            new_name = input("enter the new book name: ")
                            found = True
                            book["book_name"] = new_name  # Use assignment '='
                        elif change_what == "author":
                            new_authorname = input("enter the new author name: ")
                            found = True
                            book["book_author"] = new_authorname  # Use assignment '='
                        elif change_what == "price":
                            new_price = float(input("enter the new price: "))
                            found = True
                            book["book_price"] = new_price  # Use assignment '='
                        else:
                            print("Invalid choice for update.")
                        self.save_books()  # Save the updated book information
                        break  # Exit loop after finding and updating the book
                if not found:
                    print("No book found with the given ID.")
        if not found_manager:
            print("You are not allowed to do this, only managers.")
   
        
                   
                        








print("Books management , staff management")
answer = str(input("enter a choise: "))
if answer == "books":
    print("what do you want to do? ")
    message = str(input("enter a choise(add,delete,update,search,get,search): "))
    if message == "add":
        Books().add_books()
    elif message == "update":
        Books().update_books()

else:
    print("what do you want to do? ")
    message = str(input("enter a choise(add,delete,update,search,get,search): "))
    if message == "add":
        Staff().add_staff()
    elif message == "delete":
        Staff().delete_staff()
    elif message == "update":
        Staff().update_staff()
    elif message == "get":
        Staff().get_staff()
    elif message == "search":
        Staff().search_for_staff()
