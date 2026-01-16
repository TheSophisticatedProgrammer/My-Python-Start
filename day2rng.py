import random
import time
import matplotlib.pyplot as plt

greater = 'is greater than 10'
one = 1
total_sum = 0
average_list = []


for i in range(1000):
    for i in range(1):
    # while (one < 5):
        rng = random.randint(1,20)
        total_sum += (rng)
        wait = rng / 10
        #print(f'{wait} seconds between prints.')
        #time.sleep(wait)

        #if rng > 10:
            #print(f'{rng} {greater}') 
        #elif rng < 10:
            #print(f'{rng} is less than 10.')
        #else: 
            #print(f'{rng} is equal to 10.')

        average = total_sum
        print(f'average: {average}')
        average_list.append(average)
        total_sum = 0

print(average_list)

plt.title('Average Results of Random Number Runs')
plt.xlabel('Run Number')
plt.ylabel('Calculated Average')

plt.plot(average_list, marker='o', ms=3, linestyle='', color='k')
plt.show()

