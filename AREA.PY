# 30. Write a Python program that will accept the base and height of a triangle and compute its area.
def areaOfTri(Base,height):
 a =0.5*(height * Base)
 return a

def areaofRect(Length, Breadth):
 a =Length * Breadth
 return a
 
def areaofacircle(Radius):
 a=3.141*(Radius*Radius)
 return a
# def areaofacircle2(Diameter):
#  a=(Diameter/2)*(Diameter/2)*3.141
#  return a
def areaOfKite(diagonal1,diagonal2):
  a = 0.5 * diagonal1 * diagonal2
  return a


while True:
  print('This is your metric solver,What would you like to solve: ')
  print('1.Press 1 to solve for the area of a triangle')
  print('2.press 2 to solve for the area of a rectangle')
  print('3.press 3 to solve for the area of a circle')
  print('4.press 4 to solve for the area of a Kite')
  print('5.press end to exit')
  option=int(input("Please, Enter the number based on what you want to calculate: "))
  if option==1:
   B=int(input('Enter the base: '))
   H=int(input('Enter the height: '))
   print(areaOfTri(B, H)) 
  elif option==2:
   L=int(input('Enter the Length: ')) 
   B=int(input('Enter the breadth: '))
   print(areaofRect(L,B))
  elif option==3:
  #  C= input('DO YOU WANT TO USE Diameter OR Radius: ')
   R= int(input('Enter the Radius: '))
  #  D= int(input('Enter the Diameter: '))
  #  if C=='radius':
  #   print((R))
  #  elif C=='diameter' :
  #   print((D))
   print(areaofacircle(R))
   
  elif option== 4:
   d1=int(input('Enter the first diagonal'))
   d2=int(input('Enter the second diagonal'))
   print(areaOfKite(d1,d2))
  elif option=='end':
   print("Bye and thank you!")
  break
   