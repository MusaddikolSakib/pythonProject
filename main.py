#first_name = "Lord"
#last_name = "Simmk"
#full_name = first_name+" "+last_name
#print("Hello "+full_name)
from itertools import filterfalse

#age = 23
#age +=1
#print("Your age is:  "+str(age))
#print(type(age))

#height = 250.2
#print("your height is "+str(height)+"cm")
#print(type(height))

#Boolian code.
#human = True
#print("Are you a human: "+str(human))
#print(type(human))

#Multiple variable.
#name, age, attractive="Simmk", 23, True
#print(name,age,attractive)

#How to find the length of the string.
#name = "Simmk"
#print(len(name))

#how to find a character within a string.
#name = "Simmk"
#print(name.find("k"))

#Few usefull method.
#name = "Simmk"
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("m"))
#print(name.replace("m","a"))
#print(name*5)

#type casting..-convert the data type of a value to another data type.
#x=1
#y=2.4
#z="5"

#print(float(x))
#print(int(y))
#print(int(z)*3)


#user input
#name=input("What is your name..?: ")
#age=int(input("How old are you..?:"))
#height=float(input("How tall are you..?:"))

#print("Hello "+name)#+" "+" So you are "+str(age)+" years old")
#print("So you are "+str(age)+" years old")
#print("Your are "+str(height)+"cm tall")


#math codes
#import math
#pi=3.14
#x=1
#y=2
#z=3
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))
#print(max(x,y,z,pi))
#print(min(x,y,z,pi))


#practice
#f_number=int(input("Enter the first Number: "))
#scnd_number=int(input("Enter the second Number: "))
#Addition=f_number+scnd_number
#print("The addition of the given numbers: "+str(Addition))

#slcing string
#              index[] or slice()
#              [start:stop:step]
#index...
#name="Mr Simmk"
#first_name=name[:2]
#print(first_name)
#last_name=name[3:8]
#print(last_name)
#code_name=name[0:8:3]
#print(code_name)
#reversed_name=name[::-1]
#print(reversed_name)
#slice()...
#website="http://google.com"
#website2="http://wikipidia.com"
#slice = slice(7,-4,)
#print(website[slice])
#print(website2[slice])


#condition(if & else)...
#number=int(input("Enter the score: "))
#
#if 0<=number<=100:
#    if 80<number<=100:
#        grade="A+"
#    elif 70<number<80:
#        grade="A"
#    elif 60<number<=70:
#        grade="B"
#    elif 50<=number<=60:
#        grade="C"
#    else:
#        grade="F"
#else:
#    grade="Iligible Score"
#
#print(f"Youre Grade is: {grade}")

#number1=int(input("Enter the 1st number: "))
#number2=int(input("Enter the 2nd number: "))

#if number1<number2:
#    print(f"{number2} is greater then {number1}")
#elif number2<number1:
#    print(f"{number1} is greater then {number2}")
#else:
#    print("Bothe numbers are equal")

#while loop....
#number=int(input("Enter the height of the piramid: "))
#i=1
#while i<=number:
#    j=1
#    while j<=i:
#        print("$", end=" ")
#        j+=1
#    print()
#    i += 1

#for loop...
# adj=["Red", "Big", "Testy"]
# fruits =["apple", "banana", "cherry"]
# for x in adj:
#     for y in fruits:
#         print(x,y)
# for x in range(1, 6, 2):
#     print(x)
#     if x==3:
#         break
# else:
#     print("Finally finished")
# for x in (1, 10,2):
#     pass

# number=int(input("Enter the height of the piramid: "))
# i=1
# for x in i<=number:
#     j=1
#     for y in j<=i:
#         print("$", end=" ")
#         j += 1
#     print()
#     i+=1

# Number of rows for the pyramid
# rows = int(input("Enter the number of rows for the pyramid: "))
#
# for y in range(1, rows+1):
#     print(" "*(rows-y), end=" ")
#     print("@"*(2*y-1))

# name=[str(input("Enter your name: "))]
# for x in name:
#     print(f"Hello {x}!!!")
# name=str(input("Enter your name: "))
# while name:
#     print(f"Hey {name}!")
#     if name==str(name):
#         break

#function in python...
# def hey(name, feel):
#     print(f"Hey {name}!")
#     print(f"How are you!..{feel}.?")
#     print("How was your day..?")
#
# hey("Max", "good")
# hey("Jhon", "good")
# hey("Mac", "good")

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due {due_date}")
#
# display_invoice("Max", 95.574, "01-05-2025")

# def add(x, y):
#     z=x+y
#     return z
# def multiply(x, y):
#     z=x*y
#     return z
# def divide(x, y):
#     z=x/y
#     return z
# def subtract(x, y):
#     z=x-y
#     return z
#
# print(add(2,5))
# print(multiply(2,5))
# print(divide(5,2))
# print(subtract(10,9))

# def create_name(first, last):
#     first=first.capitalize()
#     last=last.capitalize()
#     return first+ " "+last
# full_name=create_name("mr.","max")
# print(full_name)

def region(country="Bangladesh"):
    print(f"Philipp is from {country}")
region("Pakistan")
region("Japan")
region()