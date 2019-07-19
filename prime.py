try:
 N=int(input("Enter the number: "))
 if(N==1):
  print("It's neither prime nor composite")
 elif(N>1):
  for i in range(1,N):
   Divisor=N/i
   count=+i
  if(count>2):
   print("Not a prime")
  else:
    print("Prime")
except ValueError:
  print("Invalid")
