'''
Name: <Aidan Riordan>
program name: <interest.py>
problem: Calculate monthly interest
I Aidan Riordan certify that this is my own work
'''

def main():
    annual_rate = eval(input("what is the annual interest rate?"))
    billing_cycle = eval(input("how many days are there in the billing cycle?"))
    net_ballence=eval(input("what is the previous net balance?"))
    net_payment_recieved = eval(input("what is the net payment recieved?"))
    day_cycle = eval(input("What day of the billing cycle is the payment made"))


    scaled_value= net_ballence * billing_cycle
    spread_payment = net_payment_recieved * (billing_cycle - day_cycle)
    remaining_spread = scaled_value - spread_payment
    avg_daily_balance = remaining_spread/billing_cycle
    monthly_interest_charge = avg_daily_balance*(annual_rate/12)*.01
    print(round(monthly_interest_charge), 2)

if __name__ == "__main__":
    main()
