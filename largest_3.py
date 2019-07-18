try:
 a=int(input("Enter 1st value: "))
 b=int(input("Enter 2nd value: "))
 c=int(input("enter 3rd value: "))
 if(a>b and a>c):
   print(str(a)+" greater than "+str(b)+" and "+str(c))
 elif(b>c and b>a):
  print(str(b)+" greater than "+str(a)+" and "+str(c))
 else:
  print(str(c)+" greater than "+str(a)+" and "+str(b))
except ValueError:
  print("Enter only digits!")  

