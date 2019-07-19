try:
 N=int(input("Enter the number: "))
 K=int(input("Enter the exponent: "))
 print(N**K)
except ValueError:
  print("Invalid")
