def validwage():
    wage=-1
    while(wage<1 or wage>75):
        wage=float(input("please enter hourly wage [1-75] :"))
    return wage
def validhour():
    hour=-1
    while(hour<0 or hour>90):
        hour=float(input("please enter number of hours [1-90] :"))
    return hour
def getdata():
    wage=validwage()
    hour=validhour()
    return wage,hour
def calcgross(wage,hour):
    return wage*hour
def calcdeductions(gross):
    ss_ret=gross*0.065
    if gross<2000:
        tax=gross*0.15
    else:
        tax=gross*0.4
    return ss_ret+tax
def calcnet(gross,deductions):
    return gross-deductions
def displaystub(gross,deductions,net):
    print("Gross salary :"+str(round(gross,2)))
    print("Deductions :"+str(round(deductions,2)))
    print("Net Salary :"+str(round(net,2)))
w,h=getdata()
gross=calcgross(w,h)
deductions=calcdeductions(w*h)
net=calcnet(gross,deductions)
displaystub(gross,deductions,net)