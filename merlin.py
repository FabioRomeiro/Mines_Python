import re
class Merlin:
    def __init__(self):
        self.__alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.__name = ''

    def __convert_to_number(self, letter):
        return self.__alphabet.index(letter)

    def __convert_to_coords(self, string):
        return (self.__convert_to_number(string[0].upper()),int(string[1:])-1)

    def __valid_action(self, action):
        letters_allowed = ['F','D']
        action = action.upper()
        if action != '' and action in letters_allowed: return action
        else:
            while action=='' or action not in letters_allowed:
                action = input("What you are gonna do? Type 'F' or 'D'\n F = Flag\n D = Dig\n").strip().upper()
            return action
        pass

    def __valid_coord(self, coord):
        pattern = re.compile("[A-Za-z]{1}\d")
        coord = coord.upper()
        if coord != '' and pattern.match(coord): return coord
        else:
            while coord=='' or not pattern.match(coord):
                coord = input("Where? (Ex: A12)\n").strip().upper()
            return coord
        pass

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
        action = self.__valid_action(input("What you are gonna do? Type 'F' or 'D'\n F = Flag\n D = Dig\n").strip())
        place = self.__valid_coord(input("Where? (Ex: A12)\n").strip())
        place = self.__convert_to_coords(place)
        return [action.strip().upper()[0],place]
