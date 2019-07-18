try:
  a=int(input("Enter the count:"))
  n=0
  for i in range(0,a+1,1):
   n=n+i
  print(n)
except ValueError:
  print("Enter only valid count")
