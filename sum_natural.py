try:
  a=int(input("Enter the count:"))
  n=0
  if(a>0):
   for i in range(0,a+1,1):
    n=n+i
   print(n)
  else:
   print("Enter only natural numbers")
except ValueError:
  print("Enter only digits")
