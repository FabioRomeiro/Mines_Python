class Field:
    def __init__(self,fieldFile='DefaultField.txt'):
        self.__fieldFile = fieldFile
        self.__field = []
        self.__map = []
        self.__minesCoord = []

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
