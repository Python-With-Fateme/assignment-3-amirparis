import random 
user_sc=0
pc_sc=0
while user_sc!=3 and pc_sc!=3 :
    pc=random.choice(['sang' , 'kaghaz' , 'gheichi'])
    user=input('your choice : ')
    if pc=='sang' and user=='kaghaz' :
        user_sc+=1
        print('user win')
    elif pc=='kaghaz' and user=='sang' :
        pc_sc+=1
        print('pc win')
    elif pc=='sang' and user=='gheichi' :
        pc_sc+=1
        print('pc win')
    elif pc=='gheichi' and user=='sang' :
        user_sc+=1
        print('user win')
    elif pc=='kaghaz' and user=='gheichi' :
        user_sc+=1
        print('user win')
    elif pc=='gheichi' and user=='kaghaz' :
        pc_sc+=1
        print('pc win')
    elif user==pc :
        print('mosavi')
print('user point :' , user_sc )
print('pc point : ' , pc_sc)
print('user win')
print('pc win')