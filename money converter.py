def display_menu():
  print("Welcome,I am converter,what would you like to convert!")
  print("1. Convert Euro(EUR) to NAIRA (NGN)")
  print("2. Convert British Pound Sterling (GBP) to NAIRA (NGN)")
  print("3. Convert United states Dollar (USD) to  NAIRA (NGN)")
  print("4. Convert Kuwaiti Dinar (KWD) to NAIRA (NGN)")
  print("5. Exit")
  print("Please, Enter from the above: ")
def EUR_to_NAIRA(amount):
  return amount*1764.88
def GBP_to_NAIRA(amount):
  return amount*2100.49
def USD_to_NAIRA(amount):
  return amount*1617.65
def KWD_to_NAIRA(amount):
  return amount*5293.04
while True:
  display_menu()
  choice=int(input())
  if choice==5:
    print("Bye and thank you!")
    break
  else:
    amount=int(float(input("Enter an amount: ")))
    if choice==1:
      print(amount,"Euro",EUR_to_NAIRA(amount),"NAIRA")
    elif choice==2:
      print(amount,"GBP",GBP_to_NAIRA(amount),"NAIRA")
    elif choice==3:
      print(amount,"USD",USD_to_NAIRA(amount),"NAIRA")
    elif choice==4:
      print(amount,"KWD",KWD_to_NAIRA(amount),"NAIRA")