def chamillionaire_program():
    print("Who sees me rolling? (cops, wardens, other)?")
    user_response = input().lower()

    if user_response == "cops":
        print("They see me rolling. I am ashamed of myself. I have to apologize to them!")
    elif user_response == "wardens":
        print("My music's so loud. I'm was distracted. They reprimanded me. The warden was just smiling!")
    else:
        print("The warden was just smiling!")

# Run Chamillionaire's program
chamillionaire_program()