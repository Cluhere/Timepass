command = ""
started = False
while True:
    command = input(">").lower()
    if command == "help":
        print('''
Start - type start to start the car
stop - type stop to stop the car
quit - to exit the game
        ''')
    elif command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print("car is already stoped")
        else:
            started = False
            print("Car stoped")
    elif command == "quit":
        break
    else:
        print("i don't understand that")
