def ariana_program():
    print("How many times should I break free?")
    num_breaks = int(input())

    print("I'm stronger than I've been before...")

    for i in range(num_breaks - 1, 0, -1):
        print(f"...{i}: this is the part when I break free")

    print("'Cause I can't resist it no more!")

# Run Ariana's program
ariana_program()