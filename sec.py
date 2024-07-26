# 62. Write a Python program to convert all units of time into seconds.
 

def millisec_seconds(millisec):
    a=millisec*0.001
    return a


def minutes_seconds(minutes):
    a=minutes*60
    return a

def hour_seconds(hours):
    a=hours*3600
    return a

def days_seconds(days):
    a=days*86400
    return a

 

print('This is your timeconverter,What would you like to convert: ')
print('1.Press 1 to convert from milliseconds to seconds. ')
print('2.press 2 to convert from minutes to seconds. ')
print('3.press 3 to convert from hours to seconds. ')
print('41.press 4 to convert from days to seconds.')
print('5.press 5 to exit')

key=int(input("Please, Enter the number based on what you want to calculate: "))
if key ==1:
     m=int(input('Enter the time in milliseconds: '))
     print(millisec_seconds(m))

if key==2:
    min=int(input('Enter the time in minutes: '))
    print(minutes_seconds(min))

if key==3:
    hour=int(input('Enter the time in hours: '))  
    print(hour_seconds(hour))  

if key==4:
    days=int(input('Enter the time in days: ')) 
    print(days_seconds(days))   
if key==5:
    print("Bye and thank you!")