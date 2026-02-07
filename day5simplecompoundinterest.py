savings_annual = int(input('Savings: '))
age = int(input('Age: '))
withdrawal_age = int(input('Withdrawal Age: '))
year_to_withdraw =  withdrawal_age - age
balance = 0

for i in range(year_to_withdraw):
    balance += savings_annual
    balance = round(balance * 1.07, 2) # Uses a 7% interest rate which is the historical average return for S&P 500 after inflation. (Do not use this as financial advice.)

# if you wanna swap out the interest rate you can make a variable by:
# interest = whatever your decimal multiplier is then 
# change: (balance * 1.07, 2) to: (balance * interest)

print(balance)

# This assumes you invest at start of year & that it always stays at 7%, this was made for educational purposes to help teach others how to make a simple compound interest calculator for beginners