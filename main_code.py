print("hello")
with open('data_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


import functions
functions.greeting("Andi")
print(functions.calculate(5))
