try:
 n=int(input("Enter numbers of input: "))
 k=int(input("Enter the limits: "))
 lst=[]
 add=0
 for i in range(1,n+1):
  lst.append(i)
 print(lst)
 for j in range(0,k):
  add+=lst[j]
 print(add)
except ValueError:
  print("Invalid")
