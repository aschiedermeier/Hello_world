# starsigns
# tool to understand and momorize starsigns
# startsigns class is subclass from classes modalities and elements

# bugs:


# next step:


# difficulty levels
# ##hide all helper print commands

# seperate recall_list for element

# learnfactor (def 0) sigmoid learn factor (def 0.5)
# simgoid learn factor: SLF= =1/(1+EXP(-LF))

# done:
# intro and manual
# tip: only 3 letters as answer ok.
# let user choose to see review first
# Introduce starsigns in quizlist so user can review first
# make introduction specific (month,element,modality)
# chose different recall modes based on choice
# give choice between month and element recall
# method ask zodiac element and modality
# recall game element and modality
# ask for input how many rounds
# ask for input how long StarsignList: if below 3, then quizlist short too
# final result number differs after all rounds and finished early
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
# recall 5 times


class Element():
    ''' element class '''
    def __init__(self,name="",aspect=""):
        '''initialze name and aspect attributes'''
        self.name = name
        self.aspect = aspect

    def get_descriptive_name(self):
        '''return a neatly formatted name and desctiption'''
        if self.aspect != "":
            long_name = "Element " + self.name + " represents " + self.aspect + "."
            return long_name
        else:
            long_name = "Element " + self.name + "."
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

"""
elementsList = [fire,water,air,earth]
for i in elementsList:
    print(i.get_descriptive_name())
"""    

class Modality():
    ''' class modality '''
    def __init__(self,name="",power=""):
        '''initialze name and power attributes'''
        self.name = name
        self.power = power

    def get_descriptive_name(self):
        '''return a neatly formatted name and desctiption'''
        if self.power != "":
            long_name = "The " + self.name + " modality marks the power of " + self.power + "."
            return long_name
        else:
            long_name = self.name + " modality" + "." 
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

"""
ModalityList = [cardinal,fixed,mutable]
for i in ModalityList:
    print(i.get_descriptive_name())
"""

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
            long_name = "The starsign " + self.name + " is born in " + self.month + "\nIt's root power is " + self.modality.name + " " + self.element.name + "."
            return long_name

    def get_month(self):
            '''return month of sign'''
            long_name = "The starsign " + self.name + " is born in " + self.month + "."
            return long_name

    def get_element(self):
            '''return element of sign'''
            long_name = "The starsign " + self.name + "'s element is " + self.element.name + ", which represents " + self.element.aspect + "."
            return long_name
                
    def get_modality(self):
            '''return modality of sign'''
            long_name = "The starsign " + self.name + "'s modality is " + self.modality.name + " with the power of " + self.modality.power + "."
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
        ans = input("Answer: ").lower()
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
        
    def recall_element(self):
        ''' recall month of starsign '''
        print ("What is the element of " + self.name + "?")
        print ("Hint:",self.element.name)
        ans = input("Answer: ").lower()
        ans = ans[0:3]
        self.recalled += 1
        if ans == self.element.name[0:3].lower():
            print ("Yes, it's " + self.element.name + "! :-)")
            self.correct += 1
            del(self.recall_list[0])
            self.recall_list.append(1)
        else:
            print ("No, it's " + self.element.name + "! :-(")
            self.incorrect += 1
            del(self.recall_list[0])
            self.recall_list.append(-1)
        self.grade = sum(self.recall_list)

    def recall_modality(self):
        ''' recall month of starsign '''
        print ("What is the modality of " + self.name + "?")
        print ("Hint:",self.modality.name)
        ans = input("Answer: ").lower()
        ans = ans[0:3]
        self.recalled += 1
        if ans == self.modality.name[0:3].lower():
            print ("Yes, it's " + self.modality.name + "! :-)")
            self.correct += 1
            del(self.recall_list[0])
            self.recall_list.append(1)
        else:
            print ("No, it's " + self.modality.name + "! :-(")
            self.incorrect += 1
            del(self.recall_list[0])
            self.recall_list.append(-1)
        self.grade = sum(self.recall_list)
        

# define 12 starsign objects
aries = Starsign("Aries","April")
aries.set_modality(cardinal)
aries.set_element(fire)
taurus = Starsign("Taurus","May")
taurus.set_modality(fixed)
taurus.set_element(earth)
gemini = Starsign("Gemini","June")
gemini.set_modality(mutable)
gemini.set_element(air)
cancer = Starsign("Cancer","July")
cancer.set_modality(cardinal)
cancer.set_element(water)
leo = Starsign("Leo","August")
leo.set_modality(fixed)
leo.set_element(fire)
virgo = Starsign("Virgo","September")
virgo.set_modality(mutable)
virgo.set_element(earth)
libra = Starsign("Libra","October")
libra.set_modality(cardinal)
libra.set_element(air)
scorpio = Starsign("Scorpio","November")
scorpio.set_modality(fixed)
scorpio.set_element(water)
sagittarius = Starsign("Sagittarius","December")
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

# list of 12 signs
StarsignList = [aries,taurus,gemini,cancer,leo,virgo,libra,scorpio,sagittarius,capricorn,aquarius,pisces]

# Intro text
print ()
print ("*"*60)
print (" "*20, "ZODIAC TRAINER")
print ("""Program to learn month, element and modality of the 12 western startsigns.

The twelve zodiac signs are grouped into four elements with their distinct traits. 
Each of the four elements presents a cardinal expression, a fixed expression, and a mutable expression.
Four elements times three modalities equals twelve distinct energy fields and therefore the twelve signs. 

In this program, month means the main birthmonth until around the 20th of each starsign:
e.g. April for Aries means March 21 to April 20.
This is not 100% perfect (Libra: September 24 – October 23), but an easy way to cover most people's birthdays.

A sign is mastered, if you recall it correctly 3 times in a row.
To type in an answer, the first 3 letters are sufficient, e.g. apr for Aril.

This is my first program in Python, for feedback email to: aschiedermeier@gmail.com
Have fun studying!
""")


# Recall quiz of Starsigns using recall method

# ask what to recall: month, element or modality 
modeDict = {"mon":"month","ele":"element","mod":"modality"}
entered = False
while entered == False:
    mode = input("What do you want to recall: Month, element or modality of starsign?\nRecall: ")
    mode = mode[0:3]
    if  mode not in modeDict:
        print ("Please choose one of the 3!")
    else: 
        entered = True
modeDict = {"mon":"month","ele":"element","mod":"modality"}
print ("We will recall the", modeDict[mode], "of starsigns.")
print()

# ask how many Starsigns to recall (1-12)
entered = False
while entered == False:
    try:
        signs = int(input("Recall how many Starsigns? \n1-12: "))
    except ValueError:
        print ("Error: wrong input")
        print()
        continue
    except : #catches ctrl-C error
        print ("No!")
        print()
        continue
    if  not (1 <= signs <= 12):
        print ("Error: the value is not within permitted range (1-12)")
        print()
    else: 
        entered = True

# based on choice shortening of StarsignList after shuffling
from random import shuffle
shuffle(StarsignList)
StarsignList = StarsignList[:signs]

# list containing elements to choose from in this round
# beginning fixed  number of elements
# add elements later if elements progress
quiz_list=[] # list with object (hard to read, but callable)
quiz_list_names=[] # list with object names (easy to read, but as str not usable)
import random as rn

# len_quiz_list defines initial lenght of quiz_list
if signs < 3:
    len_quiz_list = signs
else:
    len_quiz_list = 3
## print("signs:",signs)
## print("len_quiz_list:",len_quiz_list)

# fill quiz_list with len_quiz_list starsigns
# chosen randomly out of StarSignList
# no doubles allowed
while len(quiz_list) < len_quiz_list:
    i = rn.randint(0,len(StarsignList)-1)
    new_sign = StarsignList[i]
    if new_sign not in quiz_list:
        quiz_list.append(new_sign)
        quiz_list_names.append(new_sign.name)

print("\nSigns to recall:")
for sign in StarsignList:
    print ("- " + sign.name)


entered = False
while entered == False:
    review = input("\nDo you want to review those starsigns first?\ny/n: ")
    print()
    if  review == "y":
        for sign in StarsignList:
            if mode == "mon":
                print(sign.get_month())
            if mode == "ele":
                print(sign.get_element())
            if mode == "mod":
                print(sign.get_modality())
    else: 
        print ("Cool, let's go!")
    entered = True  
print()        


# ask how many rounds of recalling 
entered = False
while entered == False:
    try:
        rounds = int(input("Recall how many rounds?  \n1-100: "))
    except ValueError:
        print ("Error: wrong input")
        continue
    except : #catches ctrl-C error
        print ("No!")
        continue
    if  not (1 <= rounds <= 100):
        print ("Error: the value is not within permitted range (1-100)")
    else: 
        entered = True
print()
## rounds = 20

# recall quiz
for r in range(rounds):
    # call out mode and round
    print (modeDict[mode].capitalize(), "of starsigns: Round", r+1, "out of",rounds)

    # show Quizlist
    print ("Quizlist:",quiz_list_names)
    
    # recall random sign out of quiz_list
    i = rn.randint(0,len(quiz_list)-1) 
    print ("Starsign",i+1, "out of",len(quiz_list))
    print(quiz_list[i].get_recall_stats())
    if mode == "mon":
        quiz_list[i].recall_month()
    if mode == "ele":
        quiz_list[i].recall_element()
    if mode == "mod":
        quiz_list[i].recall_modality()
    print(quiz_list[i].get_recall_stats())

    #good_list: signs i learnt
    good_list = [i for i in StarsignList if sum(i.recall_list) == i.len_recall_list]
    good_list_names = [i.name for i in StarsignList if sum(i.recall_list) == i.len_recall_list]
    print ("good_list:",good_list_names)
    
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
            print("Added to Quizlist:", add_sign.name)
    
    # game over, if quiz_list is empty
    if len(quiz_list) == 0:
        print("\nWohoo, you have mastered all", len(good_list),"items!\n" + ":-) "*9)
        break
    
    print()
    
print ("\nAfter",r+1,"rounds you have mastered the following signs:")
for sign in good_list_names:
    print (sign)
    
#print ("good_list:",good_list_names)
print("\nGrades:")
for sign in StarsignList:
    print (sign.name, " --> Grade:", sum(sign.recall_list))
