def describe_friend(friend):
    if friend == "50 Cent":
        return "He be getting rich or die trying."
    elif friend == "Dr Dre":
        return "He be needing California love."
    elif friend == "Rihanna":
        return "She be needing an umbrella."
    else:
        return "They be cool."

def display_friend(friend):
    print(f"The {friend} can be described as follows:")
    description = describe_friend(friend)
    print(description)

def run():
    friend = input("Enter a friend: ")
    command = input("Enter 'describe' or 'display': ")

    if command == "describe":
        result = describe_friend(friend)
        print(result)
    elif command == "display":
        display_friend(friend)
    else:
        print("Invalid command.")

# Run the program
run()
