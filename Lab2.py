#!/usr/bin/python3
from datetime import date

current_date = date.today()

people = {}

# the class object that holds all the definitions
class Person:
    def __init__(self, first, last, gender, age, weight, height, bmi):
        self.c_first = first
        self.c_last = last
        self.c_gender = gender
        self.c_age = age
        self.c_weight = weight
        self.c_height = height
        self.bmi()
        self.min()
        self.max()
        self.bmivalue()

    # determines the BMI
    def bmi(self):
        self.c_bmi = weight * 703 / height * height

    # Determines the BMI Value
    def bmivalue(self):
        if self.c_bmi >= 30:
            self.c_bmivalue = "Obese"
        if self.c_bmi >= 25 and self.c_bmi <= 29.9:
            self.c_bmivalue = "Overweight"
        if self.c_bmi >= 18.5 and self.c_bmi <= 24.9:
            self.c_bmivalue = "Normal"
        if self.c_bmi <= 18.5:
            self.c_bmivalue = "Underweight"

    # Determines heart rate minimum
    def min(self):
        min = x * 0.5

    # Determines heard rate Maximum
    def max(self):
        max = x * 0.8

    # Prints part of the output

    def display(self):
        print("%-10s\t%-10s\t%-10s\t%-10s\t%-15s\t%-10s\t%-10s\t%-10s" % (
            self.c_first, self.c_last, self.c_gender, self.c_age, self.c_weight, self.c_height, self.c_bmi,
            self.c_bmivalue))

    # Why are there 2 display defs?!
    '''def display(first, last, gender, age, weight, height, bmi, bmivalue):
        print("First Name Last Name Gender Age Target Heart Rate BMI BMI Value")
        print(first + last + gender + age + min + '-' + max + bmi + bmivalue)'''


# getting the variables to put into the class. Still need to validate ssn and make a dictionary for it
persons = []
total = int(input("Please enter the number of people: "))
for x in range(total):
    ssn = input("please enter your ssn for person " + str(x + 1) + ": ")
    first_name = str(input("Please enter your first name for person " + str(x + 1) + ": "))
    last_name = input("Please enter your last name for person " + str(x + 1) + ": ")
    gender = input("Please enter your gender for person " + str(x + 1) + ": ")
    weight = int(input("Please enter your weight for person " + str(x + 1) + ": "))
    height = int(input("Please enter your height for person " + str(x + 1) + ": "))
    age = int(input("Please enter your age for person " + str(x + 1) + ": "))
    birthday = input("Please enter the day you were born for person " + str(x + 1) + ": ")
    birthMonth = input("Please enter the month you were born for person " + str(x + 1) + ": ")
    birthYear = int(input("Please enter the year you were born fro person " + str(x + 1) + ": "))
    while int(birthYear) > int(current_date.year):
        birthYear = int(input("Please enter a year before " + str(current_date.year) + ':'))
    # person=Patient(ssn,....)
    person = Person(ssn, first_name, last_name, gender, age, weight, height)
    persons.append(person)

# the first part of the print
print("%-10s\t%-10s\t%-10s\t%-10s\t%-15s\t%-10s\t%-10s" % (
    "First Name", "Last Name", "Gender", "Age", "Target Heart Rate", "BMI", "BMIValue"))
print("=" * 100)
print(persons)

# I think that this is what were supposed to do but it doesnt work
for c in persons:
    c.display()

# ssn,last_name, gender, weight, height, age, birthday, birthMonth, birthYear
# this doesn't exist in the final project
"""for i in range(n):
    cname = input("Please enter customer name: ")
    obalance = 0
    while obalance <= 50:
        obalance = float(input("Please enter opening balance > 50: "))
    customer = customer(cname, obalance)
    customers.append(customer)"""

''' def person(self, ssn, first_name, last_name, gender, weight, height, age, birthday, birthMonth, birthYear):
        list = list(ssn, first_name, last_name, gender, weight, height, age, birthday, birthMonth, birthYear)
        lists.append(list)'''
