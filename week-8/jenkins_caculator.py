#*============================================; 
#Title: Assignment 8.3; 
#Author: Professor Krasso ;
# Date: 4 December 2020; 
# Modified By: Douglas Jenkins; 
#Description: using calculator in python
#;===========================================*/

#displays the name
first_name = 'Douglas'
last_name = 'Jenkins'
print(first_name + ' ' + last_name)

#creates the add, subtract and divide functions and they are returned 
def add(num1, num2): return num1 + num2
def subtract(num1, num2): return num1 - num2
def divide(num1, num2): return num1 / num2

#prints the math 
print(add(1,2))
print(subtract(4,2))
print(divide(8,2))