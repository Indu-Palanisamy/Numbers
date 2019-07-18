try:
 a=int(input("Enter the year: "))
 if(a%4==0):
  print("Leap year")
 else:
  print("Not a Leap year")
except ValueError:
  print("Invalid input")
