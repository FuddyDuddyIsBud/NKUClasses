#!/usr/bin/python3
from datetime import date
current_date=date.today()
#This is the main class which has every bit of data that will be used for the rest of this lab
class HealthProfile:
    def __init__(self, social, first, last, gender, b_day, b_month, b_year, weight, height, day, month, year):
        self.social=social
        self.storage={}
        self.c_first=first
        self.c_last=last
        self.c_gender=gender
        self.c_day=int(day)
        self.c_month=int(month)
        self.c_year=int(year)
        self.b_day=int(b_day)
        self.b_month=int(b_month)
        self.b_year=int(b_year)
        self.age()
        self.c_weight=weight
        self.c_height=height
        self.m_rate=220-self.c_age
        self.bmi()
        self.min()
        self.max()
        self.bmivalue()
        self.storage[social]=(self.c_first, self.c_last, self.c_gender, self.c_age, str(self.c_min), str(self.c_max), self.c_bmi, self.c_bmivalue)
    #Calculates the age of the user from their birthmonth, birthday, and birthyear.
    def age(self):
        self.c_age=self.c_year-self.b_year-((self.c_month, self.c_day)<(self.b_month, self.c_month))
    # calculates the BMI for the individual
    def bmi(self):
        self.c_bmi=round(self.c_weight/(self.c_height*self.c_height)*703, 2)
    # gets the mininum heart rate
    def min(self):
        self.c_min=round(self.m_rate*0.5)
    # Gets the max heart rate
    def max(self):
        self.c_max=round(self.m_rate*0.8)
    # Calculates the BMI
    def bmivalue(self):
        if self.c_bmi>=30:
            self.c_bmivalue="Obese"
        if 25 <= self.c_bmi<=29.9:
            self.c_bmivalue="Overweight"
        if 18.5 <= self.c_bmi<=24.9:
            self.c_bmivalue="Normal"
        if self.c_bmi<=18.5:
            self.c_bmivalue="Underweight"
#Display for information
    def display(self):
        print("%-10s\t%-10s\t%-10s\t%-10s\t%-16s\t%-10s\t%-13s" % (self.c_first, self.c_last, self.c_gender, self.c_age, str(self.c_min) + " - " + str(self.c_max), self.c_bmi, self.c_bmivalue))
#List and dictionary for people by the SSN(Was told the Dictonary wasn't mandatory by the TA)
user=[]
storage={}
#for loop by the number of people entered
total=int(input("Enter the number of people: "))
for i in range(total):
    social=input("Enter Social Security Number for person " + str(i + 1) + ": ")
    while social in storage.keys():
        social=input("Enter your Social Security Number for person " + str(i + 1) + ": ")
    first_name=str(input("Enter your first name for person " + str(i + 1) + ": "))
    last_name=input("Enter your last name for person " + str(i + 1) + ": ")
    gender=input("Enter your gender for person " + str(i + 1) + ": ")
    weight=int(input("Enter your weight for person " + str(i + 1) + ": "))
    height=int(input("Enter your height for person " + str(i + 1) + ": "))
    month=input("Enter the month you were born for person " + str(i + 1) + ": ")
    day=input("Enter the day you were born for person " + str(i + 1) + ": ")
    year=int(input("Enter the year you were born for person " + str(i + 1) + ": "))
    while int(year) > int(current_date.year):
        year=int(input("Enter a year before " + str(current_date.year) + ': '))
    currentday=current_date.day
    currentmonth=current_date.month
    currentyear=current_date.year
    #Inputs the dictionary and list and apends it
    storage[social]=(first_name, last_name)
    information=HealthProfile(social, first_name, last_name, gender, day, month, year, weight, height, currentday, currentmonth, currentyear)
    user.append(information)
#spaces for the display
print("%-10s\t%-10s\t%-10s\t%-10s\t%-15s\t%-10s\t%-10s" % ("First Name", "Last Name", "Gender", "Age", "Target Heart Rate", "BMI", "BMIValue"))
print("=" * 100)
#calls upon the display and inputs the people list
for c in user:
    c.display()
