#Ask user their name
print("What is your name?")
name = input()
print("How old are you in years?")
age = int(input())
print("How tall are you in meters?")
tall = float(input())
print("How much do you weigh (in kilograms?")
weight = int(input())
bmi = weight / (tall**2)
print(f"{name} you are {age} years old and your bmi is {bmi:1f}.")
