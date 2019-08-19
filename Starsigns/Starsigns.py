# starsigns
# tool to understand and momorize starsigns
# startsigns class is subclass from classes modalities and elements

# bugs:

# next step:

# make quiz list of 4 items to recall, choose randomly from them
# if at least one value has recall list sum of plus 2, then add another element to quiz list

# method ask zodiac element and modality
# learnfactor (def 0) sigmoid learn factor (def 0.5)
# method ask: changed answered right or wrong and edit LF: +1 wenn richtig, -1 wenn falsch, simgoid learn factor: SLF= =1/(1+EXP(-LF))

# done:
# recall list is a 3 element stack list
# fixed bug: recall list is now instance attribute, not class attribute. hat to be initiated with constructor
# method ask month
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
        # list of recall stats
        self.recall_list=[0,0,0]
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
        + "\tGrade: " + str(sum(self.recall_list)) )
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
        print (self.month)
        ans = input().lower()
        ans = ans[0:3]
        self.recalled += 1
        if ans == self.month[0:3].lower():
            print ("Yes, it's " + self.month)
            self.correct += 1
            del(self.recall_list[0])
            self.recall_list.append(1)
        else:
            print ("No, it's " + self.month)
            self.incorrect += 1
            del(self.recall_list[0])
            self.recall_list.append(-1)

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
capricorn = Starsign("Capricorn","January")
capricorn.set_modality(cardinal)
capricorn.set_element(earth)
aquarius = Starsign("Aquarius","February")
aquarius.set_modality(fixed)
aquarius.set_element(air)
pisces = Starsign("Pisces","March")
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

signs = 2
rounds = 5


# Recall month of Starsign using recall method
print("\n!!!recalling game!!!\n")

import random as rn
for r in range(rounds):
    i = rn.randint(0,signs-1) # recall how many starsigns
    print ("Round", r+1, "out of",rounds)
    print ("Starsign",i+1, "out of",signs)
    print(StarsignList[i].get_recall_stats())
    StarsignList[i].recall_month()
    print(StarsignList[i].get_recall_stats())
    print()

print("\n!!!recalling list!!!\n")
print(aries.recall_list)
print(taurus.recall_list)
print(gemini.recall_list)

print (aries.get_recall_stats())
print (taurus.get_recall_stats())
print (gemini.get_recall_stats())

# recall elements and modality
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