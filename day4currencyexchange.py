def pound_to_dollar(pound):
    return pound * 1.36

def dollar_to_pound(dollars):
    return dollars * 0.73

PD = True
while True:
    Convert = str(input('Put 1 to convert from Pounds to dollars, 2 to convert Dollars to Pounds & 0 to exit: '))

    if Convert == '1':
        pound = float(input('Enter how much pounds you wanna convert:'))

        dollars = pound_to_dollar(pound)

        print('You have:', round(dollars, 2), 'dollars')

    if Convert == '2':
        dollars = float(input('Enter how much dollars you wanna convert:'))

        pound = dollar_to_pound(dollars)

        print('You have:', round(pound, 2), 'Pounds')

    if Convert == '0':
        break
