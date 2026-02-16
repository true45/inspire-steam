#Name :Millward Jeremy 
#date : 16/02/2026
#program to calculate tax using if statements


salary = int(input("Enter your gross salary"))


if salary < 50000:
    tax = (2.5 * salary) /100
    net_Salary = (salary - tax)


print(f"Gross salary is: ${salary}")
print(f"Net salary =  (net_salary)")
print(f"Net salary is: ${net_Salary}")