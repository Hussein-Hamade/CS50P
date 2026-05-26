def playback(message):
    message = message.replace(" ", "...")
    print(message)

message = input()
playback(message)