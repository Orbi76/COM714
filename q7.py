def display_inside(phrase):
    length = len(phrase) + 4
    print("-" * length)
    print(f"| {phrase} |")
    print("-" * length)

def display_left(phrase):
    length = len(phrase) + 4
    print(" " * (length -2) + "-" * length)
    print(f"{phrase}  |{' ' * (length-2)}|")
 #   print(f"{phrase}| {' ' * (length - len(phrase))}|")
    print(" " * (length-2) + "-" * length)

def display_right(phrase):
    length = len(phrase) + 4
    print("-" * length)
    print(f"|{' ' * (length-2)}|  {phrase}")
    print("-" * length)

def display_grid(phrase, size):
    rowLength = len(phrase) * size +(size-1)+2 +2
    print("-" * rowLength)
    for _ in range(size):
        row = "| " + " ".join([phrase] * size) + " |"
        print(row)
    print("-" * rowLength)

def run_program(phrase, choice, size=None):
    if choice == 1:
        display_inside(phrase)
    elif choice == 2:
        display_left(phrase)
    elif choice == 3:
        display_right(phrase)
    elif choice == 4:
        display_grid(phrase, size)
    else:
        print("Invalid choice!")


