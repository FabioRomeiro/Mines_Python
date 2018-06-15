class Merlin:
    def __init__(self):
        self.__flagedMines = 0
        self.__alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.__name = ''

    def __convert_to_number(self, letter):
        return self.__alphabet.index(letter)+1

    @property
    def step(self):
        stepCoordinate = input("Your next step coordinate (Ex: A12)").strip().upper()
        stepCoordinate = (self.__convert_to_number(stepCoordinate[0]),int(stepCoordinate[1:]))
        return stepCoordinate

    @property
    def flag(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name
