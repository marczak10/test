# coding: utf8
"""
Write a program that prompts the user to enter a password, and then prints
exactly one of the following messages: ‘The password is secure.’ or
‘The password is insecure!’. A secure password must meet the following
conditions:

* have at least one lowercase letter,
* have at least one capital letter,
* have at least one digit.

Examples:

Enter the password: Katar7yna
The password is secure.
Enter the password: catastrophe01
The password is insecure!

"""

# your code here
password = input("Enter the password: ")

def password_check(password):
    if not any(char.isupper() for char in password):
        return "The password is insecure!"
    if not any(char.islower() for char in password):
        return "The password is insecure!"
    if not any(char.isdigit() for char in password):
        return "The password is insecure!"
    return "The password is secure!"


print(password_check(password))