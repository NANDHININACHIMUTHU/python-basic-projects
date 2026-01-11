### Traffic Light Simulation
##A Python program that simulates traffic signals.  
##Based on user input (Red, Yellow, Green), the program displays appropriate actions like STOP, READY, and GO.

color=input("User enter a signal color").strip().lower()

if color == "red":
    print("STOP")
elif color == "yellow":
    print("GET READY")
elif color == "green":
    print("GO")
else:
    print("INVALID SIGNAL ")
