#user inputs

annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))

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

#salary increase for every six months

    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * portion_saved

print("Number of months:", months)
