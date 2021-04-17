"""
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass


root = tk.Tk()
app = Application(master=root)
app.mainloop()
"""

from json import load
from modules import datalibs
import datetime


class Application:

    def __init__(self):
        pass

    @staticmethod
    def start():
        print("---------------------------\n"
              "Welcome To Breeze Libraries\n"
              "---------------------------")

        Application.login()

    @staticmethod
    def login():
        username = input("-> Enter Username: ").lower().strip()
        password = input("-> Enter Password: ").lower().strip()

        with open("./data/employee.json", "r") as file:
            employees = load(file)
            for employee in employees:
                if employee["username"] == username:
                    if employee["password"] == password:
                        print(f"-------------------------\n"
                              f"Hello! {employee['name']}\n"
                              f"-------------------------")
                        Application.run()
                    else:
                        print("-> you entered a wrong username or password")
                        Application.login()
                else:
                    print("-> you entered a wrong username or password")
                    Application.login()

    @staticmethod
    def run():
        print(f"Time: {datetime.datetime.now().strftime('%H:%M')} | "
              f"Date: {datetime.datetime.now().strftime('%d/%m/%y')}")

        inp = Application.get_input()

        if inp == 1:
            Application.search_book()
        elif inp == 2:
            Application.search_account()
        elif inp == 3:
            pass
        elif inp == 4:
            pass
        elif inp == 5:
            pass

    @staticmethod
    def get_input():
        print("---------------------------------------------\n"
              "Enter the number next to what you want to do:\n"
              "1) Search Book\n"
              "2) Search Account\n"
              "3) Check Issues\n"
              "4) Manage Book\n"
              "5) Manage Account\n"
              "5) Report\n"
              "---------------------------------------------")
        valid_num = [str(i+1) for i in range(5)]
        num = input("-> Enter Number: ")
        if num in valid_num:
            return int(num)
        else:
            print(f"-> \"{num}\" is not a valid responce. Please enter numbers 1 - 5")
            Application.get_input()

    @staticmethod
    def search_book():
        print("-----------\n"
              "Search Book\n"
              "-----------\n"
              "Enter the book details (if unknown leave blank)")
        isbn = input("-> Enter isbn: ")
        books = datalibs.Get.book(isbn=isbn)
        if books:
            print("---------------------------------------------\n")
            for book in books:
                print(book)
            print("---------------------------------------------")
        else:
            title = input("-> Enter Title: ")
            author = input("-> Enter author: ")
            books = datalibs.Get.book(title=title, authors=author)
            if books:
                print("---------------------------------------------\n")
                for book in books:
                    print(book)
                print("---------------------------------------------")
            else:
                print("-------------\n"
                      "No book found\n"
                      "-------------")

    @staticmethod
    def search_account():
        print("--------------\n"
              "Search Account\n"
              "--------------\n"
              "Enter the account details (if unknown leave blank)")
        id_ = input("-> Enter account ID: ")

        accounts = datalibs.Get.account(id_=id_)

        if accounts:
            print("--------------------------------------------------\n")
            print(accounts)
            print("--------------------------------------------------\n")
        else:
            name = input("-> Enter Name: ")
            accounts = datalibs.Get.account(name=name)
            if accounts:
                print("--------------------------------------------------\n")
                for account in accounts:
                    print(account)
                print("--------------------------------------------------")
            else:
                print("----------------\n"
                      "No account found\n"
                      "----------------")

    @staticmethod
    def enter_book():
        print("----------"
              "Enter book"
              "----------")
    

    @staticmethod
    def add_account():
        print("-----------"
              "Add Account"
              "-----------")


if __name__ == "__main__":
    while True:
        Application.search_account()