greeting = str(input("Greeting: "))

if greeting == ("hello" or "Hello"):
    print("$0")
elif greeting[0] == ("h" or "H"):
    print("$20")
else:
    print("$100")