import os

class Game:
    def __init__(self,playerName=''):
        self.__playerName = playerName

    def __breakLines(self,num=1):
        for i in range(num):
            print()

    def __pressEnter(self):
        self.__breakLines()
        input("Press enter...")

    @property
    def introduction(self):
        os.system('cls')
        print(' --------------------------------------------------- ')
        print('|                                                   |')
        print('|  Welcome to the Minefield - O.O. Python version   |')
        print('|                                                   |')
        print(' --------------------------------------------------- ')
        self.__breakLines()
        self.__playerName = self.__valid_name(input('Please enter with your name: ').strip().title())
        os.system('cls')
        print("Very well, %s, in this game you'll have to flag all the mines in the field." %self.__playerName)
        print("This is a cool game, so we'll tell you when you flag all the mines... And when you step in one...")
        self.__breakLines()
        print("Good luck, try not to die :)")
        self.__pressEnter()

    def __valid_name(self, name):
        if name != '': return name
        else:
            while name=='':
                name = input("Please enter with your name: ").strip().title()
            return name

    def progress(self,field):
        os.system('cls')
        print("Game progress:")
        print("Flags (F): %d" %(field.numbers_of_mines - len(field.flags_location)))
        self.__breakLines()
        print("The field: ")
        print(field.map)

    @property
    def playerName(self):
        return self.__playerName
