def to_snake(sent: str) ->str:
    for i, letter in enumerate(sent):
        if letter.isupper():
            new_sent = sent[:i] + "_" + letter.lower() + to_snake(sent[i + 1:])
            return new_sent
    return sent
    
    

def main() ->None:
    sent = input("Camel: ")
    print(to_snake(sent))

main()