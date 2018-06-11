class Field:
    def __init__(self,fieldFile='DefaultField.txt'):
        self.fieldFile = fieldFile

    def load_field(self):
        file = open(self.fieldFile,'r')
        terrain = file.readlines()
        file.close()
        field = []
        for line in terrain:
            line = line.split('|')
            del line[-1], line[0:1]
            field.append(line)
        del field[0:1]
        return field
