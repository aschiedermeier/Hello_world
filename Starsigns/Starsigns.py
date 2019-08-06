# starsigns
# tool to understand and momorize starsigns
# startsigns class is subclass from classes modalities and elements


class Element():
    ''' element class '''
    def __init__(self,name,aspect=""):
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
    def __init__(self,name,power=""):
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
            return long_name         

    def set_power(self,power):
        ''' set the the power of the modality'''
        self.power = power

cardinal = Modality("cardinal")
cardinal.set_power("initiation")

fixed = Modality("fixed")
#fixed.set_power("sustaining")

mutable = Modality("mutable","change")


ModalityList = [cardinal,fixed,mutable]
for i in ModalityList:
    print(i.get_descriptive_name())



"""
elements = {"fire":"action & creativity",
            "water":"emotions",
            "air":"intellect",
            "earth":"substance & practicality"}

for k,v in elements.items():
    print(k+ ": " + v)


for k,v in elements.items():
    print (k)
    k = Element(k,v)

print (k.name)
print (k.aspect)
print (k.get_descriptive_name())



element_list = []
for i in range(len(elements)):
    print (i)
    key = sorted(elements)[i]
    print (key)
    value = elements[key]
    print (value)
    i = Element(key,value)
    print (i.get_descriptive_name())


print (i.get_descriptive_name())

"""