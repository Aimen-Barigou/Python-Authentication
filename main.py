import json
import time
import sys
import random

def homePage():
    print("\nHello and Welcome to BTech!\n\n--------------------------------------------\n\nWould you like to Login or SignUp?")
    print("[1] Login")
    print("[2] SignUp")
    print("[0] Exit The Program")
    option = input("Please enter your choice: ")
    if option == "1":
        accountHomePage()
    if option == "2":
        signUp()
    if option == "0":
        print("Thank you for using BTech. Goodbye!")
    if option != "1" or option != "2" or option != "0":
        while option != "1" or option != "2" or option != "0":
            print("Invalid option please try again")
            print("[1] Login")
            print("[2] SignUp")
            print("[0] Exit The Program")
            option = input("Please enter your choice: ")
            if option == "1":
                accountHomePage()
                option = 100
                break
            if option == "2":
                signUp()
                option = 100
                break
            if option == "0":
                print("Thank you for using BTech. Goodbye!")
                return

def signUp():
    passwordChars = list(" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    numbers = list("1234567890")
    print("           \nSignUp Page\n\n--------------------------------------------\n\nPlease enter your chosen Username:\n")
    username = input("Username: ")
    print("Now please enter a secure chosen Password")
    password = input("Password: ")
    for specialChar in passwordChars:
        if specialChar in password:
            for number in numbers:
                if number in password:
                    userInfo = { 
                        "users": [
                            {
                                "username" : username,
                                "password" : password
                            }
                        ]
                    }
                    with open("userInfo.json", "w") as outfile:
                        json.dump(userInfo, outfile, indent=4)
                elif number not in password:
                    while any(number in password for number in numbers) is False:
                        print("You must have at least one special character and number in your password. Please try again...")
                        password = input("Password: ")
                userInfo = { 
                        "users": [
                            {
                                "username" : username,
                                "password" : password
                            }
                        ]
                    }    
                with open("userInfo.json", "w") as outfile:
                    json.dump(userInfo, outfile, indent=4)    
        elif specialChar not in password:
            while any(specialChar in password for specialChar in passwordChars) is False:
                print("You must have at least one special character and number in your password. Please try again...")
                password = input("Password: ")
            userInfo = { 
                        "users": [
                            {
                                "username" : username,
                                "password" : password
                            }
                        ]
                    }
            with open("userInfo.json", "w") as outfile:
                json.dump(userInfo, outfile, indent=4)    
            
    print("Account successfully created! Exiting program . . . ")
    homePage()

def login():
    with open("userInfo.json") as openfile:
        data = json.load(openfile)
    while True:
        usernameLoginInput = input("Username: ")
        passwordLoginInput = input("Password: ")
        for user in data["users"]:
            if user["username"] == usernameLoginInput and user["password"] == passwordLoginInput:
                print("Logged in")
                username = user['username']
                return username
        print("Ether username or password incorrect\n\nPlease try again\n")

def accountHomePage():
    with open('userInfo.json') as openfile:
        data = json.load(openfile)
    print(f"\nHello {login()}! Welcome to your BTech account!\n What would you like to do first?\n")
    print("[0] Return to Homepage")
    option = input("Please enter your choice: ")
    if option == "0":
        homePage()
    if option != "0":
        while option != "0":
            print("Invalid option please try again")
            option = input("Please enter your choice: ")

homePage()