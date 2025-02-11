"""
Do this now 1:

Write pseudocode (an algorithm) to calculate how much a TV streaming service will cost per year
based on a monthly subscription cost the user enters

Pseudocode:

get monthly_subscription_cost
cost_per_year = monthly_subscription_cost * 12
print cost_per_year

Python:

monthly_subscription_cost = input("Enter monthly subscription cost: ")
cost_per_year = monthly_subscription_cost * 12
print("TV streaming service will cost ", cost_per_year, "per year")
"""

"""
Solution:
Pseudocode:

get monthly_cost
total_cost = monthly_cost * 12
print total_cost
"""

# monthly_cost = float(input("Monthly cost: $"))
# total = monthly_cost * 12
# print(f"Total cost is ${total:.2f}")

"""
Do this now 2:

Write an algorithm first, then Python code to calculate a user's net pay after deducting tax.
We'll need to get (input) the gross pay and tax rate.
(It's simple taxation, no thresholds or different rates)

Pseudocode:

get gross_pay and tax_rate
net_pay = gross_pay - gross pay * tax_rate
print net_pay

Python:

gross_pay = float(input("Gross pay: "))
tax_rate = float(input("Tax rate: "))
net_pay = gross_pay - gross_pay * tax_rate
print(f"The user's net pay after deducting tax is ${net_pay:.2f}")
"""

"""
Solution 2:

get gross_pay, tax_rate
tax_amount = gross_pay * tax_rate
net_pay = gross_pay - tax_ amount
print net_pay
"""

gross_pay = float(input("Gross pay: $"))
tax_rate = float(input("Tax rate(eg. 0.3 is 30%): "))
tax_amount = gross_pay * tax_rate
net_pay = gross_pay - tax_amount
print(f"The user's net pay after deducting tax is ${net_pay:.2f}.")
