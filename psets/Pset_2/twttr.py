def ommit_va(message: str) ->str:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in message:
        if letter in vowels:
            message = message.replace(letter, "")
    return message

def main():
    message = input("Input: ")
    print("Output:", ommit_va(message))

main()