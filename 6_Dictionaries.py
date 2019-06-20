###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 6: Dictionaries
###########################################

# dictionary: creation, modification
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

# dictionary modification example
# function to change location: move creature
def move_creature (creature):
    if creature["speed"]== "fast":
        creature ["location"]=creature ["location"]+2
    else:
        creature ["location"]=creature ["location"]+1

# use if in range to loop command
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
