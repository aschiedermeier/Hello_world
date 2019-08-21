# starsigns
# tool to understand and momorize starsigns
# startsigns class is subclass from classes modalities and elements

# bugs:


# next step:



# method ask zodiac element and modality
# learnfactor (def 0) sigmoid learn factor (def 0.5)
# simgoid learn factor: SLF= =1/(1+EXP(-LF))

# done:
# starsigntoadd has elements of quizlist, need to take them out
# tell how many rounds i did at the end
# good_list: list with words i learnt (max level)
# check when to add new sign
# check if there is anything to add
# if yes, then add out of to addlist (avoid double)
# List StarsignListGrades: grades of all signs
# List StarsignsToAdd: grade below max, so i can add to quiz_list
# evaluate quiz_list with list quiz_list_grades: grade of every sign in quiz_list
# Grade as its own attribute (sum of recall_list)
# during recall game: check if grade is max: then kick out of list
# if quiz_list is empty, give feedback that game is finished
# make quiz list of 4 items to recall, in each round choose randomly from them
# recall list is a 3 element stack list
# fixed bug: recall list is now instance attribute, not class attribute. hat to be initiated with constructor
# method ask month: changed answered right or wrong and edit LF: +1 wenn richtig, -1 wenn falsch, 
# 3 object attributes: recalled, correct and incorrect 
# object list stats to collect correct and incorrect results
# recall only 2 signs
# ask how many to recall 
# recall 5 times
# ask how often recall

class Element():
    ''' element class '''
    def __init__(self,name="",aspect=""):
        '''initialze name and aspect attributes'''
        self.name = name
        self.aspect = aspect

    def get_descriptive_name(self):
        '''return a neatly formatted name and desctiption'''
        if self.aspect != "":
            long_name = "Element " + self.name + " represents " + self.aspect
            return long_name
        else:
            long_name = "Element " + self.name
            return long_name         

    def set_aspect(self,aspect):
        ''' set the the aspect of the element'''
        self.aspect = aspect

    def set_name(self,name):
        ''' set the the name of the element'''
        self.name = name

fire = Element("fire")
fire.set_aspect("action & creativity")

water = Element("water")
water.set_aspect("emotions")

air = Element("air","intellect")
earth = Element ("earth","substance & practicality")

elementsList = [fire,water,air,earth]
for i in elementsList:
    print(i.get_descriptive_name())
    

class Modality():
    ''' class modality '''
    def __init__(self,name="",power=""):
        '''initialze name and power attributes'''
        self.name = name
        self.power = power

    def get_descriptive_name(self):
        '''return a neatly formatted name and desctiption'''
        if self.power != "":
            long_name = "The " + self.name + " modality marks the power of " + self.power
            return long_name
        else:
            long_name = self.name + " modality" 
            return long_name.capitalize()         

    def set_power(self,power):
        ''' set the the power of the modality'''
        self.power = power

    def set_name(self,name):
        ''' set the the name of the modality'''
        self.name = name


cardinal = Modality("cardinal")
cardinal.set_power("initiation")

fixed = Modality("fixed")
fixed.set_power("sustaining")

mutable = Modality("mutable","change")


ModalityList = [cardinal,fixed,mutable]
for i in ModalityList:
    print(i.get_descriptive_name())

class Starsign ():
    '''class starsign with classes Element & Modality as attributes'''
    # length recall list, is also max grade
    len_recall_list = 3
    def __init__(self,name = "",month="",recalled = 0,correct=0,incorrect=0):
        '''initialze name and aspect attributes'''
        self.name = name
        self.month = month
        # how often recall method was used
        self.recalled = recalled
        # how often answered correctly
        self.correct = correct
        # how often answered incorrectly
        self.incorrect = incorrect
        # list of recall stats, list length can be parameter for tuning later
        self.recall_list=[0]*self.len_recall_list
        self.grade =  sum(self.recall_list)
        self.modality = Modality()
        self.element = Element()
         

    def get_descriptive_name(self):
            '''return a neatly formatted name and desctiption'''
            if self.modality.name != "" and self.element.name != "":
                long_name = "The starsign " + self.name + " is born in " + self.month + "\nIt's root power is " + self.modality.name + " " + self.element.name
                return long_name
            else:
                long_name = "The starsign " + self.name + " is born in " + self.month
                return long_name
    
    def get_recall_stats(self):
        '''return how often been recalled: correct and incorrect'''
        recall_stats = ("The starsign " + self.name + " has been recalled " + str(self.recalled) + " times.\nCorrect: " 
        + str(self.correct) + "\t\tIncorrect: " + str(self.incorrect)+ "\nStats: " + str(self.recall_list)
        + "\tGrade: " + str(self.grade) )
        return recall_stats
        
    def set_element(self,element):
        '''set the element of a starsign'''
        self.element = element

    def set_modality(self,modality):
        '''set the modality of a starsign'''
        self.modality = modality 

    def recall_month(self):
        ''' recall month of starsign '''
        print ("When is the month of " + self.name + "?")
        print ("Hint:",self.month)
        ans = input().lower()
        ans = ans[0:3]
        self.recalled += 1
        if ans == self.month[0:3].lower():
            print ("Yes, it's " + self.month + "! :-)")
            self.correct += 1
            del(self.recall_list[0])
            self.recall_list.append(1)
        else:
            print ("No, it's " + self.month + "! :-(")
            self.incorrect += 1
            del(self.recall_list[0])
            self.recall_list.append(-1)
        self.grade = sum(self.recall_list)

# define 12 starsign objects
aries = Starsign("Aries","april")
aries.set_modality(cardinal)
aries.set_element(fire)
taurus = Starsign("Taurus","may")
taurus.set_modality(fixed)
taurus.set_element(earth)
gemini = Starsign("Gemini","june")
gemini.set_modality(mutable)
gemini.set_element(air)
cancer = Starsign("Cancer","july")
cancer.set_modality(cardinal)
cancer.set_element(water)
leo = Starsign("Leo","august")
leo.set_modality(fixed)
leo.set_element(fire)
virgo = Starsign("Virgo","september")
virgo.set_modality(mutable)
virgo.set_element(earth)
libra = Starsign("Libra","october")
libra.set_modality(cardinal)
libra.set_element(air)
scorpio = Starsign("Scorpio","november")
scorpio.set_modality(fixed)
scorpio.set_element(water)
sagittarius = Starsign("Sagittarius","december")
sagittarius.set_modality(mutable)
sagittarius.set_element(fire)
capricorn = Starsign("Capricorn","january")
capricorn.set_modality(cardinal)
capricorn.set_element(earth)
aquarius = Starsign("Aquarius","february")
aquarius.set_modality(fixed)
aquarius.set_element(air)
pisces = Starsign("Pisces","march")
pisces.set_modality(mutable)
pisces.set_element(water)

# list 12 signs
StarsignList = [aries,taurus,gemini,cancer,leo,virgo,libra,scorpio,sagittarius,capricorn,aquarius,pisces]
print (len(StarsignList))
for i in StarsignList:
    print(i.get_descriptive_name())
    print(i.modality.get_descriptive_name())
    print(i.element.get_descriptive_name())
    print()

# Recall month of Starsign using recall method
print("\n!!!recalling game!!!\n")

# list containing elements to choose from
# minumum 4 elements
# add elements: if one element has max grade - 1
quiz_list=[] # list with object (hard to read, but callable)
quiz_list_names=[] # list with object names (easy to read, but as str not usable)
import random as rn

# fill quiz_list with len_quiz_list starsigns
# chosen randomly out of StarSignList
# no doubles allowed
len_quiz_list = 3
while len(quiz_list) < len_quiz_list:
    i = rn.randint(0,len(StarsignList)-1)
    new_sign = StarsignList[i]
    if new_sign not in quiz_list:
        quiz_list.append(new_sign)
        quiz_list_names.append(new_sign.name)


# recall quiz
rounds = 20
for r in range(rounds):
    print ("Round", r+1, "out of",rounds)
    
    # delete items out of quiz_list, if grade is max
    quiz_list = [i for i in quiz_list if sum(i.recall_list) != i.len_recall_list]
    # update quiz_list_names after deletion of items in quiz_list
    quiz_list_names = [i.name for i in quiz_list if sum(i.recall_list) != i.len_recall_list]
    print ("Quizlist:",quiz_list_names)
    
    # evaluate quiz_list 
    quiz_list_grades = []
    for sign in quiz_list:
        quiz_list_grades.append(sign.grade)
    print("Quizlistgrades:",quiz_list_grades)
    
    # evaluate StarsignList 
    StarsignListGrades = []
    for sign in StarsignList:
        StarsignListGrades.append(sign.grade)
    print("StarsignListGrades:",StarsignListGrades)
    
    # Starsigns to add to quiz_list
    # grade below max
    StarsignsToAdd = []
    StarsignsToAddNames = []
    for sign in StarsignList:
        if sign.grade < sign.len_recall_list and sign not in quiz_list:
            StarsignsToAdd.append(sign)
            StarsignsToAddNames.append(sign.name)       
    #print(StarsignsToAdd)
    print("StarsignsToAddNames:",StarsignsToAddNames)
    
    # check, if i need to add new items
    # bad_list: items, that are still bad (2 below max).
    # len(bad_list) must be like initial len(quiz_list)
    bad_list = [i.name for i in quiz_list if sum(i.recall_list) < i.len_recall_list-1]
    print ("bad_list:",bad_list)
    if len(bad_list) < len_quiz_list:
        # check if i should add
        # if yes, add random item from StarsignsToAdd
        if len(StarsignsToAdd)!=0:
            i = rn.randint(0,len(StarsignsToAdd)-1)
            add_sign = StarsignsToAdd[i]
            quiz_list.append(add_sign)
            quiz_list_names.append(add_sign.name)
            print("Added to quiz_list:", add_sign.name)
    
    # game over, if quiz_list is empty
    if len(quiz_list) == 0:
        print("Wohoo, you have learnt all items!\n" + ":-) "*9)
        quiz = False
        break

    # recall random sign out of quiz_list
    i = rn.randint(0,len(quiz_list)-1) 
    print ("Starsign",i+1, "out of",len(quiz_list))
    print(quiz_list[i].get_recall_stats())
    quiz_list[i].recall_month()
    print(quiz_list[i].get_recall_stats())

    #good_list: signs i learnt
    good_list = [i for i in StarsignList if sum(i.recall_list) == i.len_recall_list]
    good_list_names = [i.name for i in StarsignList if sum(i.recall_list) == i.len_recall_list]
    print ("good_list:",good_list_names)
    print()


print ("Final result after",r,"rounds:")

print ("good_list:",good_list_names)

for sign in StarsignList:
    print (sign.name, " --> Grade:", sum(sign.recall_list))

"""
# recalling month of starsigns
# ask how many starsigns to recall 
entered = False
while entered == False:
    try:
        signs = int(input("Recall how many Starsigns? \n1-12: "))
    except ValueError:
        print ("Error: wrong input")
        continue
    except : #catches ctrl-C error
        print ("No!")
        continue
    if  not (1 <= signs <= 12):
        print ("Error: the value is not within permitted range (1-12)")
    else: 
        entered = True
"""

"""
# ask how many rounds of recalling 
entered = False
while entered == False:
    try:
        rounds = int(input("Recall month of Starsign how often?  \n1-10: "))
    except ValueError:
        print ("Error: wrong input")
        continue
    except : #catches ctrl-C error
        print ("No!")
        continue
    if  not (1 <= rounds <= 10):
        print ("Error: the value is not within permitted range (1-10)")
    else: 
        entered = True
"""


"""
# Recall element of Starsign
import random as rn
i = rn.randint(0,11)
print ("What is the element of " + StarsignList[i].name + " ?")
print (StarsignList[i].element.name)
ans = input().lower()
ans = ans[0:3]
if ans == StarsignList[i].element.name[0:3]:
    print ("Yes, it's " + StarsignList[i].element.name)
else:
    print ("No, it's " + StarsignList[i].element.name)
"""

"""
# Recall modality of Starsign
import random as rn
i = rn.randint(0,11)
print ("What is the modality of " + StarsignList[i].name + " ?")
print (StarsignList[i].modality.name)
ans = input().lower()
ans = ans[0:3]
if ans == StarsignList[i].modality.name[0:3]:
    print ("Yes, it's " + StarsignList[i].modality.name)
else:
    print ("No, it's " + StarsignList[i].modality.name)
    
   
"""