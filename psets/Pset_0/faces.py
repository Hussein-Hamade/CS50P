def main():
    message = input()
    convert(message)

def convert(message):
    message = message.replace(":)", "🙂")
    message = message.replace(":(", "🙁")
    print(message)

main()
