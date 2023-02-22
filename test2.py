#!/usr/bin/python3
from datetime import date

current_date = date.today()


# the class object that holds all the variables and definitions
class HealthProfile:
    def __init__(self, ssn, first, last, gender, b_day, b_month, b_year, weight, height, day, month, year):
        self.ssn = ssn
        self.dict = {}
        self.c_first = first
        self.c_last = last
        self.c_gender = gender
        self.c_day = int(day)
        self.c_month = int(month)
        self.c_year = int(year)
        self.b_day = int(b_day)
        self.b_month = int(b_month)
        self.b_year = int(b_year)
        self.age()
        self.c_weight = weight
        self.c_height = height
        self.m_rate = 220 - self.c_age
        self.bmi()
        self.min()
        self.max()
        self.bmivalue()
        self.dict[ssn] = (
            self.c_first, self.c_last, self.c_gender, self.c_age, str(self.c_min), str(self.c_max), self.c_bmi,
            self.c_bmivalue)

    # Determines the age of the input, got the formula from stackoverflow
    def age(self):
        self.c_age = self.c_year - self.b_year - ((self.c_month, self.c_day) < (self.b_month, self.c_month))

    # determines the BMI
    def bmi(self):
        self.c_bmi = round(self.c_weight / (self.c_height * self.c_height) * 703, 2)

    # Determines minimum heart rate
    def min(self):
        self.c_min = round(self.m_rate * 0.5)

    # Determines maximum heart rate
    def max(self):
        self.c_max = round(self.m_rate * 0.8)

    # Determines the BMI Value
    def bmivalue(self):
        if self.c_bmi >= 30:
            self.c_bmivalue = "Obese"
        if 25 <= self.c_bmi <= 29.9:
            self.c_bmivalue = "Overweight"
        if 18.5 <= self.c_bmi <= 24.9:
            self.c_bmivalue = "Normal"
        if self.c_bmi <= 18.5:
            self.c_bmivalue = "Underweight"

    # Prints part of the output
    def display(self):
        print("%-10s\t%-10s\t%-10s\t%-10s\t%-16s\t%-10s\t%-13s" % (
            self.c_first, self.c_last, self.c_gender, self.c_age, str(self.c_min) + " - " + str(self.c_max), self.c_bmi,
            self.c_bmivalue))


# Inputs from the user to put into the class and definitions
persons = []
dict = {}
total = int(input("Please enter the number of people: "))
for x in range(total):
    ssn = input("please enter your ssn for person " + str(x + 1) + ": ")
    while ssn in dict.keys():
        ssn = input("please enter your ssn for person " + str(x + 1) + ": ")  # ssn repeat checker
    first_name = str(input("Please enter your first name for person " + str(x + 1) + ": "))
    last_name = input("Please enter your last name for person " + str(x + 1) + ": ")
    gender = input("Please enter your gender for person " + str(x + 1) + ": ")
    weight = int(input("Please enter your weight for person " + str(x + 1) + ": "))
    height = int(input("Please enter your height for person " + str(x + 1) + ": "))
    birthMonth = input("Please enter the month you were born for person " + str(x + 1) + ": ")
    birthDay = input("Please enter the day you were born for person " + str(x + 1) + ": ")
    birthYear = int(input("Please enter the year you were born for person " + str(x + 1) + ": "))
    while int(birthYear) > int(current_date.year):
        birthYear = int(input("Please enter a year before " + str(current_date.year) + ': '))  # Birth year under current year checker
    day = current_date.day
    month = current_date.month
    year = current_date.year
    dict[ssn] = (first_name, last_name)
    person = HealthProfile(ssn, first_name, last_name, gender, birthDay, birthMonth, birthYear, weight, height, day,
                           month, year)
    persons.append(person)

# the first part of the print
print("%-10s\t%-10s\t%-10s\t%-10s\t%-15s\t%-10s\t%-10s" % (
    "First Name", "Last Name", "Gender", "Age", "Target Heart Rate", "BMI", "BMIValue"))
print("=" * 100)

# call to the print of all the information in the chart
for c in persons:
    c.display()