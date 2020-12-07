class Note:
    def __init__(self, note, name):
        if type(name) == str:
            if name != "":
                self.name = name
            else:
                raise ValueError
        else:
            raise TypeError
        if type(note) == float:
            if 2 <= note <= 6:
                self.note = note
            else:
                raise ValueError
        else:
            raise TypeError

    def getName(self):
        return self.name

    def getNote(self):
        return self.note
