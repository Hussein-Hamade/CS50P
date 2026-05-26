def main():
    time = input("What time is it? ")
    time = time.strip()
    hours, minuts = time.split(":")
    time = convert(time)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        return "lunch time"
    elif 18.0 <= time <= 19.0:
        return "dinner time"
    else:
        return


def convert(time):
    hours, minuts = time.split(":")
    minuts = float(minuts)/60
    time = float(hours) + float(minuts)
    return time


if __name__ == "__main__":
    main()