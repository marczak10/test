# coding: utf8
"""
Write a program that will ask the user for an integer (the size of the triangle)
and then print an isosceles triangle composed of `*` characters of the given
size. E.g:

Enter the size of the triangle: 3
  *
 ***
*****

"""

# your code here
size = int(input("Enter the size of the triangle: "))

for i in range(1, size + 1):
    spaces = " " * (size - i)
    stars = "*" * ((2 * i) - 1)
    print(spaces + stars + spaces)
  
