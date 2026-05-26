''''
x = int(input("x: "))
y = int(input("y: "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
'''
'''
x = int(input("x: "))
y = int(input("y: "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal thtoan y")
'''
'''
x = int(input("x: "))
y = int(input("y: "))

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
'''

################################################################
'''
score = int(input("score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# more efficient way

score = int(input("score: "))

if score >= 90 :
    print("Grade: A")
elif score >= 80 :
    print("Grade: B")
elif score >= 70 :
    print("Grade: C")
elif score >= 60 :
    print("Grade: D")
else:
    print("Grade: F")
'''

##########################################################
'''
name = input("what's your name: ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
'''