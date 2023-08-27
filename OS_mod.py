Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> home=os.getcwd()
>>> print(home)
C:\Program Files\Python311
>>> import os
>>> browser=os.system(“/usr/bin/chromium-browser”)
SyntaxError: invalid character '“' (U+201C)
>>> import os
>>> browser=os.system("/usr/bin/chromium-browser")
>>> import os
>>> os.system('start chrome "https://www.youtube.com/feed/music"')
0
>>> import os
>>> os.system('chromium-browser "http://bdmpublications.com/"')
1
>>> import os
>>> a=('chromium-browser "http://bdmpublications.com/"')
>>> b=('chromium-browser "http://www.google.co.uk"')os.system(a + b)
SyntaxError: invalid syntax
>>> import os
>>> a=('chromium-browser "http://bdmpublications.com/"')
>>> b=('chromium-browser "http://www.google.co.uk"')
>>> os.system(a + b)
1
>>> import os
>>> os.mkdir(“NEW”)
SyntaxError: invalid character '“' (U+201C)
>>> import os
>>> os.mkdir("NEW")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    os.mkdir("NEW")
PermissionError: [WinError 5] Access is denied: 'NEW'
>>> import os
>>> os.rename(“NEW”, “OLD)
SyntaxError: invalid character '“' (U+201C)
