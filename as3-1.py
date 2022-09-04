import time
import random

print('ez test')
time.sleep(2)

print('you have 6 chances to guess')
time.sleep(2)

x=[1,2,3,4,5,6,7,8,9,10]
num=random.choice(x)

for i in range(6) :
    guess=int(input('guess number 0 to 10  :'))
    if guess==num :
        print( 'good job :)')
        break 
    else :
        print('guess another number : ')
else :
    print('you lost my friend :( ')