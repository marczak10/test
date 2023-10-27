# coding: utf8
"""
Write a program that prompts user to enter some text and prints the number
of CAPITAL LETTERS on the screen. E.g:

Enter text: Data Science is SUPER!
7

"""

# your code here  
def letter_counter(word):
    n = 0
    for letter in word:
        if letter.isupper():
            n += 1
        else:
            pass
    return n
 

text = input("Enter text: ")
print(letter_counter(text))      
    
