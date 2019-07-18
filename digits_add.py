try:
  a=int(input("Enter the value:"))
  sum=0
  t=0
  c=len(str(a))
  if(a>0):
   for i in range(0,c):
    t=a%10
    sum=sum+t
    a=a//10
   print(sum)
  else:
   print("Enter only positive numbers")
except ValueError:
  print("Enter only digits")
