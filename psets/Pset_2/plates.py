import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid = True
    
    if s[:3].isdigit():
        valid = False
    elif len(s) < 2 or len(s) > 6:
        valid = False
    elif s[-1].isalpha():
        valid = False

    for i in range(len(s)):
        if not (s[i].isdigit() or s[i].isalpha()):
            valid = False

    for i in range(len(s)):
        if s[i].isdigit() and s[i] == "0":
            valid = False
            break

    return valid
    
    

if __name__ == "__main__":
    main()