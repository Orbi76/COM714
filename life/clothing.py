from clothingSize import ClothingSize


class Clothing:

    def __init__(self, color: str, material: str, size: ClothingSize):
        self.__color = color
        self.__material = material
        self.__size = size

    def __repr__(self):
        return f"Color: {self.__color}, Material: {self.__material}, Size: {self.__size}"

    def __str__(self):
        return f"This cloth has {self.__color} color, from {self.__material} material in {self.__size} size! "

    def getSize(self):
        # return self.__size
        return self.ClothingSize.name

    def setSize(self, size):
        self.__size = size
        # self.__size = ClothingSize.name


gatya = Clothing("Blue", "Jeans", "S")
gatya2 = Clothing("Red", "Jeans", 2)

if __name__ == '__main__':
    print(repr(gatya))
    print(str(gatya))
    # print(gatya.getSize())
    print(repr(gatya2))
    print(str(gatya2))
    # print(gatya2.getSize())
