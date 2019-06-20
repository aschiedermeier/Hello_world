###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 6: dictionaries
###########################################

# nested dictionary
# friends dictionary
# every friend is dictionary
# some values can be list
# using excel function to created nested dictionary "friends"
# every key value pair is dictionary "username"
# kvs: gender, first_name, family_name, dances
# values of "dances" is list of max 3 dances

Andi = {"gender": "m"}
#print (Andi)
#print (Andi["gender"])

friends = {"AlexA":{"gender": "m"},}
print (friends["AlexA"])
for user_name,user_info in friends.items():
    print (user_name)
    print (user_info)
    print (user_info["gender"])
    
# nested dictionary
# friends dictionary
# every friend is dictionary
# some values can be list

# created dictionary using excel function
friends={"AlexA":{"gender": "m","first_name": "Alex","family_name": "All","location": "Munich","dances":["Salsa","Bachata","Kizomba",]},"BertaB":{"gender": "f","first_name": "Berta","family_name": "Butt","location": "Munich","dances":["Salsa","","",]},"ChrisC":{"gender": "m","first_name": "Chris","family_name": "Cheese","location": "Paris","dances":["Salsa, ","Kizomba","",]},"DorisD":{"gender": "f","first_name": "Doris","family_name": "Done","location": "Prague","dances":["Zouk","Bachata","",]},}

# have an extra look at the print out results below this line
print ("\ncheck a look !!!\n".upper())

for user_name,user_info in sorted(friends.items()):
    #print (friends)
    print ("\nUsername: " + str(user_name))
    print ("\nuser_info: " + str(user_info))
    print ("\nuser_info[gender]: " + str(user_info["gender"]))
    print ("\nuser_info[family_name]: " + str(user_info["family_name"]))
    print ("\nuser_info[first_name]: " + str(user_info["first_name"]))
    print ("\nuser_info[dances]: " + str(user_info["dances"]))
