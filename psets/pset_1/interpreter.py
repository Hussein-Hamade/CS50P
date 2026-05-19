equation  = input("Expression: ")

x, y, z = equation.split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "/" and float(z) == 0.0:
    print("can't devid by zero")
elif y == "/" and float(z) != 0.0:
    print(float(x) / float(z))
else:
    print("invalid operator")
    