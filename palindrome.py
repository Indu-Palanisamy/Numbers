try:
 N=int(input("Enter the number: "))
 if(N<=1000):
  temp=N
  rev=0
  rem=0
  while(N>0):
    rem=N%10
    rev=rev*10+rem
    N=N//10
  if(temp==rev):
   print("YES")
  else:
   print("NO") 
 else:
   print("Enter within 1000")
except ValueError:
  print("Invalid")
