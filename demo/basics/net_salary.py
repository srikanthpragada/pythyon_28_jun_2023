# Take salary and display net salary by adding HRA and DA

# input
salary = int(input("Enter salary :"))

# process
hra = salary * 30 // 100
da = salary * 20 // 100
net_salary = salary + hra + da

# output
print(f"Basic Salary     {salary:8}")
print(f"+ HRA            {hra:8}")
print(f"+ DA             {da:8}")
print(f"Net Salary       {net_salary:8}")
