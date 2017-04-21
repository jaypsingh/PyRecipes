import math
def avg_grade(x,y,z):
    print("Average Grade Method")
    average = (x+y+z)/3
    print (average)

def print_name(firstName, lastName):
    print(firstName+" "+lastName)

def add_num(a, b):
    sumnum = a+b
    print (sumnum)

def avg_grade2(grades):
    print("Average Grade Method")
    average = sum(grades)/len(grades)
    print (average)

def print_name2(name):
    print("Print Name Method")
    myName = " " .join(name)
    print(myName)

def add_num2(numList):
    print("Add Sum Method")
    sumnum = sum(numList)
    print (sumnum)


print ("==================== DEMO-1 =======================")
# Demo 1
# Notice the arguments are passed WITH astrics as prefix to
# pass it as individual argument in the method.
methodCall = [('avg_grade',2,3,4),
    ('print_name', 'Tyrion', 'Lannistor'),
    ('add_num', 1,2)]

for tag, *args in methodCall:
    print (tag)
    print (*args)    
    if tag == "avg_grade":
        avg_grade(*args)
    if tag == 'print_name':
        print_name(*args)
    if tag == 'add_num':
        add_num(*args)
    print ("--------------------------")
print ("==================== DEMO-2 =======================")
# Demo 2
# Notice the arguments are passed WITHOUT astrics as prefix to
# pass it as list argument.
student, *grades = ['Dolores',1,2,3,4,5,6,7,8,9]
avg_grade2(grades)
House, *name = ['Baratheon', 'Tyrion','Lannister', 'son', 'of', 'Tywin']
print_name2(name)
operation, *numList = ['Sum', 1,2,3,4,5,6,7,8,9]
add_num2(numList)

