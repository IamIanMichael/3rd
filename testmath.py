from minimath import*

print ("Select operation.\n")
print ("1. Times by Two")
print ("2. Times by Three")
print ("3. Square")
print ("4. Power of")

choice = input ("\nEnter choice (1/2/3/4): ")

num1 = int(input("\nEnter number:"))

if choice == '1':
 print(timestwo(num1))
elif choice == '2':
 print(timesthree(num1))
elif choice == '3':
 print(square(num1))
elif choice == '4':
 num2 = int(input("Enter second number: "))
 print(power(num1, num2))
else:
 print("Invalid input")                
