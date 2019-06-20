#############################
# Test code from Python book
# Chaptet 5: If funcitons
# chapter 6: Dictionaries
###############################

# if else function
def want_five(a):
    if a != 5:
        print ("i want 5")
    else:
        print("happy now")
want_five(3)

#list and count 10 millions
#mil = [value for value in range(1,10000001)]
#print(sum(mil))

#list of random numbers, print missing numbers
import random as rn
rands = [rn.randint(1,6)for value in range (1,11)]
print (rands)
print ("missing numbers: ")
for i in range(1,11):
    if i  not in rands:
        print (i)

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

#print list elements, checks if list is empty
def print_list (check_list):
    if check_list:
        for i in check_list:
            print(i)
    else:
        print ("empty list")
a = []
print_list(a)

###########################################
# define dictionary alien with one key-value-pair
alien = {"color":"green"}
# acces value
print (alien["color"])
# add key-value-pair
alien ["location"] = 0
print (alien)
# add more key-value-pairs
alien.update({"speed":"medium","power":5})
print (alien)
# remove key-value-pair
del alien["color"]
print(alien)

# move function
def move_creature (creature):
    if creature["speed"]== "fast":
        creature ["location"]=creature ["location"]+2
    else:
        creature ["location"]=creature ["location"]+1

# move 5 times
for i in range (1,6):
    move_creature(alien)
print (alien)

# speed up
alien ["speed"]="fast"
print (alien)
# move 5 more times, this time fast
for i in range (1,6):
    move_creature(alien)
print (alien)

###########################
# print out key-value-pairs of dictionary 
for k,v in alien.items():
    print ("\n"+k)
    print (v)
# print out keys, two methods
for keys in alien.keys():
    print (keys.title())
for keys in alien:
    print (keys.title())
# print out values
for values in alien.values():
    print (values)

##############################
# print out values without doubles
fav_food = {
    "Andi":"Tofu",
    "Berti":"Pizza",
    "Carl":"Burger",
    "Doris":"Pizza",
    }
# no doubles due to set method
# sorted order
for values in sorted(set(fav_food.values())):
    print (values)