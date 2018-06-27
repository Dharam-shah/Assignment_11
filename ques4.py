from threading import *

def fact(num):
        if num == 1:
         return 1
        else:
         return (num * factorial(num-1))
         return 1 if num == 1 else (num * factorial(num-1))

num = int(input("Enter Number to be factorial:"))
print('Factorial of {} is {}'.format(num, factorial(num)))

T1 = Thread(target = fact,args = (num,))
T1.start()