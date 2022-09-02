import time

time.sleep(1)

print('ez test')
time.sleep(2)

num=38,15.44,12,50

print('you have 6 chances to guess')
time.sleep(2)

for i in range(6) :
    guess=int(input('guess number 0 to 50  :'))
    if guess==num :
        print( 'good job :)')
        break 
    else :
        print('try again : ')
else :
    print('u r done my friend :( ')