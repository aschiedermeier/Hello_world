# starsigns
# tool to understand and momorize starsigns
# startsigns class is subclass from classes modalities and elements


class Element():
    ''' element class '''
    def __init__(self,name,aspect):
        '''initialze name and aspect attributes'''
        self.name=name
        self.aspect = aspect

    def get_descriptive_name(self):
        '''return a neatly formatted name and desctiption'''
        long_name = "Element " + self.name + " represents " + self.aspect
        return long_name

# fire = Element("fire","action")
# print (fire.name)
# print (fire.aspect)
# print (fire.get_descriptive_name())

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