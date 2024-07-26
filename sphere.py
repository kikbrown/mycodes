# 15. Write a Python program to get the volume of a sphere with radius six.
 
def volumeofasphere(radius):
    a= 4.188*(radius*radius*radius)
    return a

def volumeofacube(edge):
    a= (edge*edge*edge)
    return a
def volumeofacylinder(height, radius):
   a= 3.141*(radius*radius)*height
   return a




while True:
 print('This is your Volume solver,What would you like to solve: ')
 print('1.Press 1 to solve for the volume of a sphere. ')
 print('2.press 2 to solve for the area of a cube. ')
 print('3.press 3 to solve for the area of a cylinder. ')
 print('4.press end to exit')
 
 option=int(input("Please, Enter the number based on what you want to calculate: "))
 if option==1:
  radius =int(input('Enter the radius: '))
  print(volumeofasphere(radius))
  
 elif option==2:
  edge=int(input("Enter thr edge sides: "))
  print(volumeofacube(edge))
  
 elif option==3:
   rad=int(input('Enter the radius: '))
   hei=int(input('Enter the height: '))
   print(volumeofacylinder(rad, hei))
 elif option=='end':
   print("Bye and thank you!")
 break