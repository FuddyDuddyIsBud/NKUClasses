
#task1
temp=[]
below=[]
newlist=[]

number=int(input("input number of temps you wish to add:"))
for i in range(number):
    user=int(input("input temprature:"))
    temp.append(user)

for user in temp:
    c = (user - 32) * 5 / 9
    if c<10:
        below.append(c)
        newlist.append(c)
    else:
        newlist.append(c)
print("Your tempratures in Celcius are:", newlist)
print("Your tempratures below 10 degree celcus are:", below)

#task2
from time import localtime, mktime, strftime

cur_time=localtime()
given_time = int(input("Input chosen time:"))
converted_given_time = localtime(given_time)

def hour_difference(converted_given_time, cur_time):
    hour1=converted_given_time.hour()
    hour2=cur_time.hour()
    difference=hour1-hour2
    print(difference)

def years(converted_given_time, cur_time):
    mktime.tm_year = cur_time.year
    while cur_time.year!=converted_given_time.year:
        print(converted_given_time.year + 1)

hour_difference(converted_given_time, cur_time)
years(converted_given_time, cur_time)

#task3

from time import localtime, mktime, strftime

cur_time = localtime()
chosen_time=int(input("Please input chosen time: "))
chosen_time=localtime(chosen_time)
chosen_time=mktime(chosen_time)
converted_time_in_number = mktime(cur_time)

appointment = converted_time_in_number+chosen_time
appointment=localtime(appointment)

print(strftime("Your appointment is: %B %d Time: %H:%M%p ", appointment))
