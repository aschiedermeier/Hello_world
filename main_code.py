print("hello")
with open('data_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


import functions
functions.greeting("Andi")
(A,B) = functions.calculate(5)
print (A)
print (B)

import matplotlib.pyplot as plt
#%matplotlib inline

x = [i for i in range (11)]
y = [i**2 for i in x]

plt.plot(x,y) 
plt.show()
