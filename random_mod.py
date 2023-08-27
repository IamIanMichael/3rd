Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> print(random.randint(0,5))
1
>>> import random
>>> print(random.random() *100)
70.85316084163614
>>> import random
>>> KeyboardInterrupt
random.choice([“Conan”, “Valeria”, “Belit”]) 
>>> import random
>>> 
... random.choice(["Conan", "Valeria", "Belit"])
'Valeria'
>>> import random
>>> lst=["David", 44, 'BDM Publications", 3245.23, "Pi", True, 3.14, "Python"]
...      
SyntaxError: incomplete input
>>> import random
...      
>>> lst=["David", 44, "BDM Publications", 3245.23, "Pi", True, 3.14, "Python"]
...      
>>> rnd=random.choice(lst)
...      
>>> print(rnd)
...      
BDM Publications
>>> random.shuffle(lst)
...      
>>> print(lst) 
...      
[True, 'David', 'Python', 'BDM Publications', 'Pi', 44, 3245.23, 3.14]
>>> import random
...      
>>> lst=[[i] for I in range(20)]
...      
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    lst=[[i] for I in range(20)]
  File "<pyshell#16>", line 1, in <listcomp>
    lst=[[i] for I in range(20)]
NameError: name 'i' is not defined. Did you mean: 'I'?
random.shuffle(lst)
     
print(lst)
     
['Pi', 'David', 'Python', 'BDM Publications', True, 3.14, 3245.23, 44]
import random
for i in range(10):
 print(random.randrange(0, 200, 7))

 
105
0
14
133
112
49
77
42
161
161
