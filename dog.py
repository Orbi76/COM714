class Dog:
    species = "Bull dog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"


kon= Dog('kon', 7)
print(kon.description())
print(kon.speak("vau"))
