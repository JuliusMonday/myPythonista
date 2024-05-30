#print("Hello World")

#Check the Python version of the editor
#import sys
#print(sys.version)

#VARIABLES
"""
name = "JuTeLabs"
age = 105

print(name, age)
"""

is_checkedin = True
age = 20
name = "John Smith"
is_new = False

if is_checkedin:
    print("We checked In " + name)

    print(age)
    if is_new:
        print(name + " is also a new patient")
    else:
        print(name+" is an old patient, with some medical records")
else:
    print(name +" is not checked in our hospital")