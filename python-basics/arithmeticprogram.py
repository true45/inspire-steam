# Millward Jeremy
# Date : 13/02/2026
# program to calculate arithmetic  proggression in python 

#calculating nth term

a = int(input("Enter the first number:"))
n = int(input("Enter the number of the terms:"))
d = int(input("Enter the common difference:"))

nth_term = a + (n - 1)
sn = (n/2) *( (2*a + (n-1) *d) )
print(f"The nth term is :(nth_term)")


print(f"")

