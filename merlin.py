class Merlin:
    def __init__(self):
        self.__alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.__name = ''

    def __convert_to_number(self, letter):
        return self.__alphabet.index(letter)

    def __convert_to_coords(self, string):
        return (self.__convert_to_number(string[0].upper()),int(string[1:])-1)


    @property
    def flag(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def action(self):
        action = input("What you are gonna do? Type 'F' or 'D'\n F = Flag\n D = Dig\n")
        place = input("Where? (Ex: A12)\n")
        place = self.__convert_to_coords(place)
        return [action.strip().upper()[0],place]
