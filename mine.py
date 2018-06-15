class Mine:
    def __init__(self):
        self.__it_exploded = False
        self.__all_flagged = False

    @property
    def spread_mines(self):
        minesLocation = [(2,8),(8,12),(4,8)]
        return minesLocation

    @property
    def it_exploded(self):
        return self.__it_exploded

    @it_exploded.setter
    def it_exploded(self, ans):
        self.__it_exploded = ans

    @property
    def all_flagged(self):
        return self.__all_flagged

    @all_flagged.setter
    def all_flagged(self, ans):
        self.__it_exploded = ans
