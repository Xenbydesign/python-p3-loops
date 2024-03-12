#!/usr/bin/env python3

# need a while loop to do count down 
def happy_new_year():
    countdown = 10 
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print('Happy New Year!')

# need to  iterating through the list 
def square_integers(int_list):
    squared_list =[]
    for num in int_list:
        squared_list.append(num**2)
    return squared_list

# loop is needed here 
def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else: print(i)