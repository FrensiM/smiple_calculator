#!/usr/bin/python3
import math
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return 0
    else:
        return a / b
def factorial(a):
    result = 1
    for i in range(i, a + 1):
        result *= i
    return result

def display_menu():
    print("Welcome to calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")
    print("6. Exit")
    
def get_user_choice():
    choice = input("Enter your choice 1-6: ")
    return choice
def perform_calculator():
    choice = get_user_choice
    
    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = add(num1, num2)
        print(f"{result}")
    elif choice == '2':
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))
         result = sub(num1, num2)
         print(f"{result}")
    elif choice == '3':
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))
         result = mul(num1, num2)
         print(f"{result}")
    elif choice == '4':
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))
         result = div(num1, num2)
         print(f"{result}")
    elif choice == '5':
         num1 = float(input("Enter the number: "))
         result = factorial(num1)
         print(f"{result}")        
    elif choice == '6':
         print("Goodbye")
         exit()
    else:
        print("Invalid choice , please try again")
while True:
    display_menu()
    perform_calculator()
    print()