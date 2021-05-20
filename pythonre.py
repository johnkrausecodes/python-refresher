#Challenge 1 Variables
"""age = 28

name = 'John'

print(f'My name is {name} and I am {age} years old')"""

#Challenge 2 Statements
"""year = 2050

if year >= 2000 and year <= 2099:
    print('Welcome to the 21st Century!')
else:
    print('You are before or after the 21st Century')"""

#Challenge 3 Functions
"""def tripleprint(word):
    print('{}{}{}'.format(word, word, word))

tripleprint("Hello")"""

#Challenge 4 Lists
"""Shoes = ["Spizikes", "Air Force 1", "Curry 2", "Melo 5"]

Shoes.insert(1, 3.124)

print (Shoes[1])
print (Shoes)"""

#Challenge 5 Loops
"""numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

for num in numbers:
    if num > 90:
        print (num)"""

#Challenge 6 Dictionaries
"""words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

cooldictionary = {}
for n in range(0,3):
    cooldictionary[words[n]] = definitions[n]

print(cooldictionary["Spange"])"""

#Challenge 7 Classes

"""class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        print(f"2020 - {self.year}")

mycar = Car(2021, "Ford", "Expedition")
mycar.age()"""
