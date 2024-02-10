from life.human import Human


class Planet:

    def __init__(self, name:str=''):
        self.__name = name
        self.__humans = []

    def __repr__(self):
        return f"Planet(name='{self.__name}', humans={self.__humans})"

    def __str__(self):
        return f"This is planet {self.__name}. It is inhabited by {len(self.__humans)} humans."

    def add(self, human: Human) -> bool:
        self.__humans.append(human)
        return (human in self.__humans)

    def has(self, human: Human) -> bool:
        return (human in self.__humans)

    def population(self) -> int:
        return len(self.__humans)

    def remove(self, human: Human) -> bool:
        self.__humans.remove(human)
        return (human not in self.__humans)







