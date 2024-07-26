while True:
 print ('Welcome to your angle calculator ')
 print('1.Press 1 to solve for the hypotenuse angle in CM')
 print('2.press 2 to solve for the ajacent angle in CM')
 print('3.press 3 to solve for the opposite angle in CM')
 key=int(input("Please, Enter from the above: "))
 if key ==1:
   o=int(input('Enter opposite angle: '))
   a=int(input('Enter ajacent angle: '))
   print((a*a)+(o*o))
 if key ==2:
   h=int(input('Enter hypotenuse angle: '))
   o=int(input('Enter opposite angle: '))
   if h < o:
      print('Invalid')
   else:
    print((h*h)-(o*o))
 if key ==3:
   h=int(input('Enter hypotenuse angle: '))
   a=int(input('Enter ajacent angle: '))
 if h < a:
      print('Invalid!!!')
 else:
   print((h*h)+(a*a))
 if key==4:
   print("Bye and thank you!")
   break