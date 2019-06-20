###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 5: If funcitons
###########################################

# if else function
def want_five(a):
    if a != 5:
        print ("i want 5")
    else:
        print("happy now")
want_five(3)

# list comprehension
# list and count 10 millions
# mil = [value for value in range(1,10000001)]
# print(sum(mil))

# for if
# list of random numbers, print missing numbers
import random as rn
rands = [rn.randint(1,6)for value in range (1,11)]
print (rands)
print ("missing numbers: ")
for i in range(1,11):
    if i  not in rands:
        print (i)


# if elif else
# points for shooting aliens
def alien_shoot(alien):
    if alien == "green":
        points = 5
    elif alien == "yellow":
        points = 10
    elif alien == "red":
        points = 15
    else:
        points = 0
    print (points)
alien_shoot("red")

# if else
# print list elements, checks if list is empty
def print_list (check_list):
    if check_list:
        for i in check_list:
            print(i)
    else:
        print ("empty list")
a = []
print_list(a)

