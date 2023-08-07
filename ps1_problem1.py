#user inputs

annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))

#assigning variables

portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12
months = 0

down_payment = total_cost * portion_down_payment

#calculate number of months required to save enough money for down payment

while current_savings < down_payment:
    current_savings += current_savings * r / 12 + portion_saved * monthly_salary
    months += 1

print("Number of months:", months)
