def main():
  a=int(input("enter the number: "))
  if(a%2==0):
   print("Even")
  elif(a%2==1):
   print("Odd")
try:
 main()
except ValueError:
  print("Invalid")
