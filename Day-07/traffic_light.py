# Traffic lights

colour = input("Enter the color red or yellow or green: ").lower()

if colour == "Red":
    print("Stop")
elif colour == "Yellow":
    print("Slow down")
elif colour == "Green":
    print("Go")
else:
    print("Enter the correct colour")