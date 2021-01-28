import tkinter as tk

user_choice = int(input("Choose: \n 1/Addition \n 2/Subtraction \n 3/Multiplication \n 4/Division \n"))

def addition():
    num_1 = input("Input first number: ")
    num_2 = input("Input second number: ")
        
    result = float(num_1) + float(num_2)
    print(result)

def subtraction():
    num_1 = input("Input first number: ")
    num_2 = input("Input second number: ")
        
    result = float(num_1) - float(num_2)
    print(result)

def multiplication():
    num_1 = input("Input first number: ")
    num_2 = input("Input second number: ")
        
    result = float(num_1) * float(num_2)
    print(result)

def division():
    num_1 = input("Input first number: ")
    num_2 = input("Input second number: ")
        
    result = float(num_1) / float(num_2)
    print(result)            

if user_choice == 1:
    addition()

if user_choice == 2:
    subtraction()

if user_choice == 3:
    multiplication()

if user_choice == 4:
    division()
