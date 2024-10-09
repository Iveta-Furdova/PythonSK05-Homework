# 1) Write a Python script that prints "Hello, World!" to the console.
from setuptools.command.build_ext import if_dl

print("Hello, World")

#2) Create variables to store your name, age, and favorite color.1113

name="Iveta"
age = 29
color = "blue"
print(f"My name is {name}, I am {age}, and my favourite color is {color}.")

#3) Write a program that calculates the area of a rectangle. Prompt the user to enter the length and width, calculate the area, and then print it.
length = float(input("Enter length:"))
width = float(input("Enter width"))

area = length * width

print("The area of the rectangle is: {}".format(area))

area = length * width

print("The area of the rectangle is: {}".format(area))

# 4) temperature cenvert from Fahrenheit to Celsius
fahrenheit = float(input("Enter the temperature in Fah: "))
celsius = (fahrenheit - 32)* 5/9

print("Temperature in celsius: " , celsius)

#5)Create a program that asks the user to enter two numbers and then prints out the sum, difference, product, and quotient of those numbers.
numer1 = float(input("Enter first number: "))
numer2 = float(input("Enter second number: "))

sabirane = numer1 + numer2
difference = numer1 - numer2
product = numer1 * numer2
quotient = numer1 / numer2 if numer2 !=0 else "division"

print("sum is", sabirane)
print("difference is", difference)
print("The product is:", product)
print("The quotient is:", quotient)


#6)Write a program that prompts the user to enter a radius and then calculates and prints the area and circumference of a circle with that radius.

radius = float(input("Enter radius"))

area = 3.14 * (radius ** 2)
circumference = 2 * 3.14 * radius

print("are of the circle is ", area)
print("circumference of the circle is: ", circumference)

#7)Create a program that checks whether a given number is even or odd. Prompt the user to enter a number and then print out whether it's even or odd.

chislo = int(input("Ener your number"))
if chislo % 2 == 0:
    print("chisloto e chetno")
else:
    print("chisloto e nechetno")

#8)Write a program that prompts the user lto enter their age and then determines and prints out whether they are eligible to vote (i.e., if they are 18 or older).

user = int(input("Please enter your age?"))
if user <18:
    print("Sorry, you must be older than 18 to proceed. Please come back when you are eligible.")
else:
    print("Congratulations! You are eligible to proceed.")

#9)Create a program that prompts the user to enter a string and then prints out the length of the string.

userstring = input("Please enter string")

lengthofstring = len(userstring)

print("The lenght of the string is",lengthofstring)

#10)Write a program that prompts the user to enter two strings and then concatenates them together (i.e., joins them into one string) and prints out the result.

userstring1 = input("Please add your sting")
userstring2 = input("Please add your second string")

result = userstring1 + userstring2

print("The result is:", result)