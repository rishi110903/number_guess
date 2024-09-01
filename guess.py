import random
import time
import sys

text = "Enter the highest range number you want to guess. Guess range starts from 1 to the number you are entering: "

for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()  
    time.sleep(0.05)  

def guess(x):
    rand_num = random.randint(1,x)
    guess = 0
    while guess!=rand_num:
        guess = int(input(f'Guess the number between 1 to {x} : '))
        if guess > rand_num :
            print("Guess too HIGH")
        elif guess < rand_num :
            print("Guess too LOW")
        
    print(f'YES U GUESSED IT RIGHT, ITS {rand_num}')

x = int(input())
guess(x)