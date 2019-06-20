# load a file and print it
print("hello")
with open('data_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    
# importing functions from another file
import functions
functions.greeting("Andi")
(A,B) = functions.calculate(5)
print (A)
print (B)

# draw simple plot
import matplotlib.pyplot as plt
#%matplotlib inline
x = [i for i in range (11)]
y = [i**2 for i in x]
plt.plot(x,y) 
# this line will show the plot, but then the code does not continue. have to figure out
plt.show()
import time
time.sleep(5)
plt.close()