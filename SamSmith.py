def howDoYouSleep():
    numberOfPoints = 0
    print("Let's find out how you sleep...")
    for i in range(4):
        print("...Baby, how do you sleep when you lie to me?")
        response = input().lower()
        if response == "very well":
            numberOfPoints -= 10
            print("I'm hopin' that my love will keep you up tonight.")
        elif response == "poorly":
            numberOfPoints +=20
            print("All that fear and all that pressure.")
        else:
            print("Love to you is just a game.")

    print(f"You achieved {numberOfPoints} points.")
   # print("Hello", numberOfPoints, "points")  --- other option to print out intiger in strings.

howDoYouSleep()

