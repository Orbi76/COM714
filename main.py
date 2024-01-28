from q7 import run_program

if __name__ == "__main__":
    phrase = input("Enter a phrase (preferably Poker Face): ")
    choice = int(input("Choose an option (1-4): "))
    if choice == 4:
        size = int(input("Enter grid size: "))
        run_program(phrase, choice, size)
    else:
        run_program(phrase, choice)

