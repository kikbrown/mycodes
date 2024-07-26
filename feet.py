# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.

def feet_inch(inch):
   inc=inch*12
   return inc


def feet_yards(yards):
   yar=yards*0.33
   return yar

def feet_kilo(kilometre):
   kilo=kilometre*0.000304
   return kilo


def feet_miles(miles):
   mile=miles*0.000189
   return mile

while True:
 print('This is your metric solver,What would you like to convert: ')
 print('1.Press 1 to convert feet to inches: ')
 print('2.press 2 to convert feet to yards: ')
 print('3.press 3 to convert feet to kilometre: ')
 print('4.press 4 to convert feet to miles: ')
 print('5.press 5 to exit')
 button=int(input("Please, Enter from the above: "))
 if button ==1:
    inc=int(input('Enter values in feet:'))
    print(feet_inch(inc))
 if button ==2:
    yard=int(input('Enter values in feet:'))
    print(feet_yards(yard))
 if button ==3:
    kilo=int(input('Enter values in feet:')) 
    print(feet_kilo(kilo))
 if button==4: 
      miles=int(input('Enter values in feet:')) 
      print(feet_miles(miles)) 
      if button==5:
           print('Bye and thank you' )
           break