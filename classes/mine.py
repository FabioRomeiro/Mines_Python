class Mine:
    def __init__(self):
        self.__it_exploded = False
        self.__all_flagged = False

    def spread_mines(self,field):
        import random
        fieldSize = field.field_size
        maxMines = (fieldSize[0]*fieldSize[1])//4
        minesLocation = [(0,0),(1,1),(2,2)]
        for i in range(maxMines):
            x,y = random.randint(0,fieldSize[0]), random.randint(0,fieldSize[1])
            if (x,y) not in minesLocation: minesLocation.append((x,y))
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
        self.__all_flagged = ans
