#! /usr/bin/python

def is_prime(x):
    temp = 2
    while temp < x:
        if x % temp != 0:
            if temp == x-1:
                return True
        else:
            return False
            break
        temp+=1

print("\t\t\t||  Welcome To The Prime World  ||\n\n")
a = int(input('''\tEnter the Starting number from where you want to find the prime number
\t(minimum starting point is 3) : '''))

b = int(input('''\tHow many prime number is required: '''))

i = 1
while i <= int(b):
    if is_prime(a) == True:
        print(a)
        i+=1
    a+=1