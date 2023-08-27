import random

print(">>>>>>>>>>Random Word Finder<<<<<<<<<<")
print("\nUsing a 466K English word text file I can pick any words at random.\n")
wds=int(input("\nHow many words shall I choose? "))
with open("/home/pi/Downloads/words.txt", "rt") as f:
 words = f.readlines()
words = [w.rstrip() for w in words]

print("--------------------")
for w in random.sample(words, wds):
 print(w)
print("--------------------")
