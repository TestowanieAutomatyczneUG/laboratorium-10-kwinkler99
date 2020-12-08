from src.sample.notes_storage import NotesStorage


class NotesService:
    def __init__(self):
        self.notesStorage = NotesStorage()

    def add(self, note):
        return self.notesStorage.add(note)

    def clear(self):
        return self.notesStorage.clear()

    def averageOf(self, name):
        notes = self.notesStorage.getAllNotesOf(name)
        if len(notes) > 0:
            return sum(map(lambda student: student.note, notes))/len(self.notesStorage.getAllNotesOf(name))
        else:
            raise ValueError
