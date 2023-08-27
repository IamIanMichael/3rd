Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name="Conan"
>>> print("The barbarian hero of the Hyborian Age is:{}".format(name))
The barbarian hero of the Hyborian Age is:Conan
>>> name="Conan"
>>> place="Cimmeria"
>>> print("{} hailed from the North, in a cold land known as {}".format(name, place))
Conan hailed from the North, in a cold land known as Cimmeria
>>> numbers=1, 3, 45, 567546, 3425346345
>>> print("Some numbers: {}, {}, {}, {}, {}".format(*numbers))
Some numbers: 1, 3, 45, 567546, 3425346345
>>> numbers=1, 4, 7, 9
>>> print("More numbers: {3}, {0}, {2},{1}.".format(*numbers))
More numbers: 9, 1, 7,4.
>>> characters=["Conan", "Belit", "Valeria",19, 27, 20]
>>> print ("{0} is {3} years old. Whereas {1} is {4} years old.".format(*characters))
Conan is 19 years old. Whereas Belit is 27 years old.
>>> name=input("What’s your name? ")
What’s your name? Von
>>> print("Hello {}.".format(name)
...       Von
...       
SyntaxError: incomplete input
>>> names=["Conan", "Belit", "Valeria"]
...       
>>> ages=[25, 21, 22]
...       
>>> print("{0[0]} is {1[0]} years old. Whereas {0[1]}is {1[1]} years old.".format(names, ages))
...       
Conan is 25 years old. Whereas Belitis 21 years old.
