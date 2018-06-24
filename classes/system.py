import os

class Game:
    def __init__(self,playerName=''):
        self.__playerName = playerName

        self.__show_mine_coords = False

    def __breakLines(self,num=1):
        for i in range(num):
            print()

    @property
    def __pressEnter(self):
        self.__breakLines()
        input("Press enter...")

    @property
    def __cls(self):
        os.system('cls')

    @property
    def introduction(self):
        self.__cls
        print(' --------------------------------------------------- ')
        print('|                                                   |')
        print('|  Welcome to the Minefield - O.O. Python version   |')
        print('|                                                   |')
        print(' --------------------------------------------------- ')
        self.__breakLines()
        self.__playerName = self.__valid_name(input('Please enter with your name: ').strip().title())
        self.__cls
        print("Very well, %s, in this game you'll have to flag all the mines in the field." %self.__playerName)
        print("This is a cool game, so we'll tell you when you flag all the mines... And when you step in one...")
        self.__breakLines()
        print("Good luck, try not to die :)")
        self.__pressEnter

    def __valid_name(self, name):
        if name != '': return name
        else:
            while name=='':
                name = input("Please enter with your name: ").strip().title()
            return name

    def progress(self,field):
        self.__cls
        print("Game progress:")
        print("Flags (F): %d" %(field.numbers_of_mines - len(field.flags_location)))
        if self.show_mine_coords: print("Mines location:\n"+str(field.minesLocation))
        self.__breakLines()
        print("The field: ")
        print(field.map)

    def gameOver(self,field):
        sentence = ''
        self.__breakLines(2)
        print("----------------------------------------------------------------------------")
        self.__breakLines()
        if len(field.flagged_mines):
            if len(field.flagged_mines)>1: plural = 's'
            else: plural = ""
            sentence = "But look, you flagged "+str(len(field.flagged_mines))+" mine"+plural+"!!\n   Keep trying and some day you will get there sz"
        else:
            sentence = "And you even flagged a single mine...\n   This is sad..."
        print("   Damn %s... I think you died... %s" %(self.playerName, sentence))
        self.__breakLines()
        print("----------------------------------------------------------------------------")
        self.__breakLines()
        self.__pressEnter

    @property
    def won(self):
        self.__breakLines(2)
        print("****************************************************************************")
        self.__breakLines()
        print("    CONGRATS %s!! You just flagged all the mines in the field!!\n    You are a fucking god \o/" %(self.playerName.upper()))
        self.__breakLines()
        print("****************************************************************************")
        self.__breakLines()
        self.__pressEnter

    @property
    def play_again(self):
        self.__cls
        ans = input(" Do you wanna play again?? (Y/N)\n").upper()
        if ans != '' and ans in ['Y','N']: return ans
        else:
            while ans=='' or ans not in ['Y','N']:
                ans = input(" Do you wanna play again?? (Y/N)\n").upper()
            return ans

    @property
    def playerName(self):
        return self.__playerName

    @property
    def show_mine_coords(self):
        return self.__show_mine_coords

    @show_mine_coords.setter
    def show_mine_coords(self,ans):
        self.__show_mine_coords = ans
