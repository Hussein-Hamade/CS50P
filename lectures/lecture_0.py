# print("hello,world")    print the what's betweem ""

#  name=input("what is your name? ")    take the value from the input and assgin it in the variable called name

# print("hello, ", name)    same as print but it take the name variable and ouyput it, to make it take the variable we need the comma outside of the "" (usually for multi argu) or we can use the + sgin

'''
name = input("what is your name? ")
print("hello", end=" ")
print(name)

The offical documentation for print is print(*object, sep= ' ', end='\n')

the *object means that the print function can hold as many orgument as you want

the sep=' ' means that the objects are separated with space between them

The end='\n' means that when the function end go to new line
'''

# for string

'''
name = input("what is your name? ")

name = name.strip()     this is a string method that removes the wiht spaces form the variable in the () it can hold parameter

name = name.capitalize()    this method capitalize the string var, we can also use the title() method  (!!! we can use multiple method in the same command like "name = name.strip().title()")

first, last = name.split(" ")  this method split the string variable into tow part at the space between them " " where it will reaggin them to frist and last according to thier position left to left, right to right

print(f"hello, {name}")    the f is called the f method it is used to add the argument in the "" without the use of comma or + sgin
'''

# for int

'''
int(x)  this function turn the var x from string to int, we can add it to input like "int(input(""))"

float(x) for real number like 3.4

round(numbeer[, ndigits])  this method is used to round a real number number the the ndigits option to specify the presession of the rounding mehtod (optional) example "round(x/y, 2)" we are specifying 2 digits after the comma

print(f"{x:,}") this is also an optional method where when the number is big like 1000 it will write it as 1,000 

square(x) is a function that return the square value of x or we can use the pow(x,2) function that allow us to get the power that we want
'''

# functions

'''
def main():  # its not necessary to define the main function but its mor practical so when you need to define a new function you can define it where ever you want without breaking the call function 
    name = input("what is your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)

main()  # you need to call the main since it is also a function 
'''