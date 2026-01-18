# Settings.
list_printing_boolean = False
element_printing_boolean = False
money_printing_boolean = True
import time

# Creating lists & accessing their elements.
mylist = ['mango', 'bananas', 'watermelon']
mylist2 = [5, True, 'apple']
mathlist = [2+2, 5*5, 10-2]

# Accessing elements from the lists.
mango = mylist[0]
bananas = mylist[1]
watermelon = mylist[2]
five = mylist2[0]
True_value = mylist2[1]
apple = mylist2[2] 

# Printing the lists.
if list_printing_boolean == True:
    print('my list is', mylist) 
    print('my list 2 is', mylist2) 
    print('math list is', mathlist)
    print(len(mylist), 'elements are in mylist')

# Printing accessed elements.
if element_printing_boolean == True:
    for i in mylist:
        print(i)
    if 'bananas' in mylist:
        print('yes, bananas is in mylist')
    else:
        print('no, bananas is not in mylist')

# Currency
money = 1000
growth_amount = 1.10
year = 0
interest = 0
growth = money * growth_amount

for i in range(10):
    time.sleep(0.5)
    money = growth
    year += 1
    interest = money - 1000
    rounded_money = round(money, 2)
    rounded_interest = round(interest, 2)

    if money_printing_boolean == True:
        print('after', year, 'year(s)', 'interest has added an extra', rounded_interest, 'making the total', rounded_money,)
    
    growth = money * growth_amount

final_interest_percentage = round(100 / money * interest, 2)
print(final_interest_percentage,'% is how much your investment is from interest.')

# Compound interest is way easier then I thought! I thought you would have to use complicated formulas to do, when I seached up. But I choose try do myself & I done it!
# I was also experimenting with lists, to find new knowledge.