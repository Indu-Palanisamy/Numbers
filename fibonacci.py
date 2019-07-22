n=int(input("Enter the value: "))
a=0
b=1
count=0
lst=[]
if(n<=0):
 print("Enter a positive number")
elif(n==1):
  print(a)
else:
  while(count<n):
    lst.append(a)
    c = a+b
    a=b
    b=c
    count += 1
print(lst)
