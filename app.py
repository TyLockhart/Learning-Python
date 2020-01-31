"""
print("Ty Lockhart")
print("o----")
print(" ||||")
print("*" * 10)



price = 10
price = 20
rating = 4.9
name2 = "Ty"
is_published = True
print(name2)


name3 = "John Smith"
age = 20
is_new = False

print("*"*20)

name = input("What is your name? ")
print("Hi "+ name)

print("*"*20)

name_question = input("What is your name? ")
colour_question = input("What is your favourite colour? ")
print(name_question + " likes " + colour_question)


birth_year = input("Birth year: ")
print(type(birth_year))
age = 2019-int(birth_year)
#2019 - "1982"

print(type(age))
print(age)

lb_weight=input("What is your weight (in lbs)? ")
kg_weight=0.453592*float(lb_weight)
print("You weigh (in kg) "+ str(kg_weight))



course = "Python for Beginners"
course2='''
Hi John,

Here is our first email to you.

Thank you,
The support team

'''
course3="Python for Beginners"
print(course3[0:3])
another = course3[:]
print(another)



name = "Jennifer"
print(name[1:-1])
#guessing it will print e and r // Print ennife

first = "John"
last = "Smith"
message=first+" [" + last + "] is a coder"
msg= f"{first} [{last}] is a coder" #formatted strings
print(msg)

#stopped at 40:00 https://www.youtube.com/watch?v=_uQrJ0TkZlc



course = "Tom Thumb is the subject of several films. In 1936, a short animated version directed by Ub Iwerks was released, and in 1940 another animated version by Chuck Jones called Tom Thumb in Trouble. In 1958, George Pal directed a live action musical, tom thumb (rendered in lowercase to denote the character's small size) starring Russ Tamblyn, based on the Brothers Grimm's story Thumbling. Also in 1958, although not released in the U.S. until 1967 in a dubbed version, a Mexican version of Tom Thumb (originally titled Pulgarcito) was made based loosely on Charles Perrault's ';'Le petit Poucet';. A darker, modernized film version using stop motion animation called The Secret Adventures of Tom Thumb was released in 1993, and Tom Thumb Meets Thumbelina and the 2002 direct-to-DVD animated movie, The Adventures of Tom Thumb and Thumbelina brought together the two most famous tiny people of literature, with Tom voiced by Elijah Wood. Text stories and later comic strips based on the Tom Thumb character appeared in the anthology comic The Beano from the first issue in 1938 until the late fifties."
print(len(course))
print(course.upper())
print(course.lower())
print(course.find("Tom"))
print(course.replace("Tom","Abs"))
print("Python" in course)


print(10%3)

print(10**3)#^

x=10
x=x+3#x+=3
print(x)


x=10+3*2**2#uses bedmas
print(x)

import math

print(math.ceil(2.9))#3
print(math.floor(2.9))#2

x=2.9
print(round(x))
print(abs(x))#|x| always positive

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

price=1000000
credit_good = False

if credit_good:
    down_payment=.1*price
else:
    down_payment=.2*price

print(f"Down payment: ${down_payment}")

has_high_income=True
has_good_credit=True
has_criminal_record=False

if has_high_income and has_good_credit:#and
    print("Eligible for loan")

if has_high_income or has_good_credit:#or
    print("Eligible for loan")

if has_high_income and not has_criminal_record:#not
      print("Eligible for loan")


temperature=31

if temperature>30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = "tony"

name_length = len(name)

if name_length<3:
    print("Name is shorter than 3 characters")
elif name_length>50:
    print("Name is longer than 50 characters")
else:
    print("Name looks good!")


weight_question=input("Weight: ")
lb_or_kg=input("(L)bs or (K)g: ")

if lb_or_kg.lower()=="k":
    print(float(weight_question)*2.20462)
elif lb_or_kg.lower()=="l":
    print(float(weight_question)*0.453592)

#stopped at 1:20:00 https://www.youtube.com/watch?v=_uQrJ0TkZlc
"""





































































































