#!/usr/bin/python3
def get_age():
    check = True
    while check == True:
        try:
            age = int(input("Please enter your age: "))
            if age < 1:
                print("Please enter a positive number!")
            else:
                check = False
        except ValueError:
            print("Error Please enter a valid input!")
    return age

def get_gender():
    check = True
    while check == True:
            gender = input("Please enter your gender: (M/F) ").upper()
            if (gender != "M") and (gender != "F"):
                print("Please enter a valid input!")
            else:
                check = False
    return gender


def get_email():
    check = True
    while check == True:
            email = input("Please enter your email: ")
            email_characters = list(email)
            if "@" not in email_characters:
                print("Attention! your email is incorrect")
            else:
                check = False
    return email

def get_name():
    name = input("Please enter your name: ")
    return name


def display(name,age,gender,email):
    print("Name: ", name, "\nAge: ", age, "\nE-mail: ", email)
    if gender == "M":
        print("Gender: Male")
    else:
        print("Gender: Female")
        check = True
        while check == True:
            answer = input("\nIs the information aboce correct? (yes/no").lower()
            if answer == "yes":
                repeat = False
            elif answer == "no":
                repeat = True
            else:
                print("Please enter \"Yes\" or \"No\"")
        return repeat

print("***WELCOME***")
age = get_age()
gender = get_gender()
email = get_email()
name = get_name()
repeat = display(name,age,gender,email)
