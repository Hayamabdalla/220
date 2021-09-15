"""
name: Hayam Abdalla
interest.py

problem: interest on credit card accounts
certification of authenticity:
I certify that this assignment is entirely my own work.
"""

def main():
    # user inputs
    annual_rate   = eval(input("_the_annual_ interest _rate:"))
    days_in_cycle = eval(input("the number of days in the billing cycle:"))
    net_balance   = eval(input("the previous net balance:"))
    payment       = eval(input("the payment amount:"))
    payment_day   = eval(input("the day of the month in which the payment was recived:"))
    # calculations steps
    step_1 = net_balance * days_in_cycle
    days   = days_in_cycle - payment_day
    step_2 = payment * days
    step_3 = step_1 - step_2
    step_4 = step_3 / days_in_cycle
    monthly_interest_rate = (annual_rate / 12) / 100
    monthly_interest_charge = step_4 * monthly_interest_rate
    monthly_interest_charge = round (monthly_interest_charge, 2)
    print (monthly_interest_charge)

if __name__== '__main__':
    main()
