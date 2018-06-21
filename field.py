class Field:
    def __init__(self,fieldFile='DefaultField.txt'):
        self.__fieldFile = fieldFile
        self.__field = []
        self.__map = []
        self.__minesCoord = []
        self.__flags_location = []
        self.__flagged_mines = 0
        self.__dig_location = []

    def __load_file(self,txtfile):
        file = open(txtfile,'r')
        content = file.readlines()
        file.close()
        return content

    def minesCoord(self,coords):
        self.__minesCoord = coords

    @property
    def load_field(self):
        terrain = self.__load_file(self.__fieldFile)
        field = []
        for row in terrain:
            row = row.split('|')
            del row[-1], row[0:1]
            field.append(row)
        del field[0:1]
        self.__field = field

    @property
    def field_size(self):
        return [len(self.__field),len(self.__field)]

    @property
    def map(self):
        terrain =self.__load_file(self.__fieldFile)

        fieldLetters = []
        for row in terrain:
            fieldLetters.append(row.split('|')[0])
        del fieldLetters[0]

        self.__map = ''
        for i in range(len(self.__field)):
            for item in ([fieldLetters[i]] + self.__field[i]):
                self.__map += item + '|'
            self.__map += '\n'

        fieldNumbers = ''.join(terrain[0])
        self.__map =  fieldNumbers + self.__map
        return self.__map

    def __process_flag(self,coords,mine):
        self.__flags_location.append(coords)

        if coords in self.__minesCoord:
            self.__flagged_mines += 1

        if set(self.__minesCoord) <= set(self.__flags_location):
            mine.all_flagged = True

        self.__field[coords[0]][coords[1]] = ' FF '

    def __minesAround(self,coord):
        numberOfMinesAround = 0
        quadrant = [(coord[0]+1,coord[1]-1),(coord[0]+1,coord[1]),(coord[0]+1,coord[1]+1),
                    (coord[0],coord[1]-1),(coord[0],coord[1]),(coord[0],coord[1]+1),
                    (coord[0]-1,coord[1]-1),(coord[0]-1,coord[1]),(coord[0]-1,coord[1]+1)]
        for coord in quadrant:
            if coord in self.__minesCoord: numberOfMinesAround += 1
        return numberOfMinesAround

    def __process_dig(self, coords, mine):
        self.__dig_location.append(coords)

        if coords in self.__minesCoord:
            self.__explode_field()
            mine.it_exploded = True
        else:
            numberOfMinesAround = self.__minesAround(coords)
            if numberOfMinesAround == 0:
                self.__field[coords[0]][coords[1]] = '    '
            else:
                self.__field[coords[0]][coords[1]] = ' 0'+str(numberOfMinesAround)+' '

    def __explode_field(self):
        field = self.__field
        for x in range(len(field)):
            for y in range(len(field[x])):
                if (x,y) in self.__minesCoord:
                    field[x][y] = ' MM '
                else:
                    field[x][y] = '    '



    def processAction(self, data, mine):
        move = data[0]
        coords = data[1]

        if move == 'F': self.__process_flag(coords,mine)
        if move == 'D': self.__process_dig(coords,mine)

    @property
    def flags_location(self):
        return self.__flags_location

    @property
    def flagged_mines(self):
        return self.__flagged_mines
