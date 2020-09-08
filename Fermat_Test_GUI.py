# Taras Zherebetskyy
import random
from tkinter import *

def GCD(x, y): #gcd calculator
   while(y): 
       x, y = y, x % y 
   return x 

def isPrime(n):
    #testing for the most simple cases like: odd numbers
    if n <= 3:
        return True
    elif n % 2 == 0:
        return False

    #testing for 7 times, should be enought to find any pseudo prime numbers
    for i in range(5):
        a = random.randint(2, n-1)

        if GCD(a,n) == 1:
            if (a ** (n-1)) % n == 1: continue
            else: return False
        else: return False
    return True

def MainFunction():
    num = int(ent.get())
    print(num)
    if isPrime(num):
        lab = Label(root, text = str(num) + " is possibly prime")
    else:
        lab = Label(root, text = str(num) + " is not prime")
    lab.place(y=30, relwidth=0.5)


#Creating a root
root = Tk()
root.title('Prime Number Tester')
root.geometry('300x70')
# Variable needed
ent = Entry(root, borderwidth = 5)
ent.place(width=195, x=5)
button = Button(root, text='Test', command = MainFunction)
button.place(width=90,x=205)

root.mainloop()
