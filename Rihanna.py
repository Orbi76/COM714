def explain(what, where):
    # Write your code here (remember to indent correctly)
    if what == "Monster" and where == "Bed":
        print("I'm friends with the monster that's under my bed")
    elif what == "Doctor" and where == "Hospital":
        print("You're trying to save me, stop holding your breath")
    else:
        print("You think I'm crazy, yeah, you think I'm crazy")

# The following are calls to the function for testing purposes
explain("Monster", "Bed")
explain("Doctor", "Hospital")
explain("Stranger", "Street")

