class Field:
    def __init__(self,fieldFile='DefaultField.txt'):
        self.__fieldFile = fieldFile

        self.__terrain = self.__load_file(self.__fieldFile)
        self.__field = []
        self.__map = ''

        self.__field_X_size = 0
        self.__field_Y_size = 0

        self.__minesCoord = []
        self.__numbers_of_mines = 0

        self.__flags_location = []
        self.__flagged_mines = []
        self.__dig_location = []

    def __load_file(self,txtfile):
        file = open(txtfile,'r')
        content = file.readlines()
        file.close()

        return content

    @property
    def load_field(self):
        terrain = self.__terrain
        field = []
        for row in terrain:
            row = row.split('|')
            del row[-1], row[0:1]
            field.append(row)
        del field[0:1]
        self.__field = field
        self.__field_X_size = len(field[0])
        self.__field_Y_size = len(field)

    @property
    def field_size(self):
        return [self.__field_X_size,self.__field_Y_size]


    def minesCoord(self,coords):
        self.__minesCoord = coords
        self.__numbers_of_mines = len(coords)

    @property
    def minesLocation(self):
        return self.__minesCoord

    @property
    def numbers_of_mines(self):
        return self.__numbers_of_mines


    @property
    def map(self):
        terrain = self.__terrain

        fieldLetters = [row.split('|')[0] for row in terrain]
        del fieldLetters[0]

        self.__map = ''
        for i in range(len(self.__field)):
            for item in ([fieldLetters[i]] + self.__field[i]):
                self.__map += item + '|'
            self.__map += '\n'

        fieldNumbers = ''.join(terrain[0])
        self.__map =  fieldNumbers + self.__map

        return self.__map

    def __define_quadrant(self, coord):
        return [(coord[0]+1,coord[1]-1),(coord[0]+1,coord[1]),(coord[0]+1,coord[1]+1),
        (coord[0],coord[1]-1),(coord[0],coord[1]),(coord[0],coord[1]+1),
        (coord[0]-1,coord[1]-1),(coord[0]-1,coord[1]),(coord[0]-1,coord[1]+1)]

    def __minesAround(self,coord):
        numberOfMinesAround = 0
        quadrant = self.__define_quadrant(coord)

        for coord in quadrant:
            if coord in self.__minesCoord: numberOfMinesAround += 1

        return numberOfMinesAround

    def processAction(self, data, mine, system):
        move = data[0]
        if len(data)<=1:
            if move == 'I': system.show_mine_coords = True
            if move == 'H': system.show_mine_coords = False
            return
        coords = data[1]
        if coords[0] <= self.field_size[0] and coords[1] <= self.field_size[1]:
            if move == 'F': self.__process_flag(coords,mine)
            if move == 'D': self.__process_dig(coords,mine)


    def __process_flag(self,coords,mine):

        if set(self.__minesCoord) <= set(self.__flags_location):
            mine.all_flagged = True

        if self.__field[coords[1]][coords[0]] == ' FF ':
            self.__field[coords[1]][coords[0]] = ' XX '
            if coords in self.minesLocation: self.__flagged_mines.remove(coords)
            self.__flags_location.remove(coords)
        else:
            self.__field[coords[1]][coords[0]] = ' FF '
            if coords in self.minesLocation: self.__flagged_mines.append(coords)
            self.__flags_location.append(coords)
            if len(self.flags_location) >= self.__numbers_of_mines : mine.all_flagged = True


    def __process_dig(self, coords, mine):
        self.__dig_location.append(coords)
        if coords in self.__flags_location: return
        if coords in self.__minesCoord and coords:
            self.__explode_field()
            mine.it_exploded = True
        else:
            numberOfMinesAround = self.__minesAround(coords)
            if numberOfMinesAround == 0:
                self.__field[coords[1]][coords[0]] = '    '
            else:
                self.__field[coords[1]][coords[0]] = ' 0'+str(numberOfMinesAround)+' '


    def __explode_field(self):
        for x in range(self.__field_X_size):
            for y in range(self.__field_Y_size):
                if (x,y) in self.__minesCoord:
                    if (x,y) in self.__flags_location: self.__field[y][x] = ' FF '
                    else: self.__field[y][x] = ' MM '
                else:
                    self.__field[y][x] = '    '


    @property
    def flags_location(self):
        return self.__flags_location

    @property
    def flagged_mines(self):
        return self.__flagged_mines
