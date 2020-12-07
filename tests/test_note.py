import unittest
from src.sample.note import Note


class TestNote(unittest.TestCase):
    def test_name(self):
        note = Note(3.5,  'testOne')
        self.assertEqual(note.getName(), 'testOne')

    def test_note(self):
        note = Note(3.5, 'testTwo')
        self.assertEqual(note.getNote(), 3.5)

    def test_note_equal_2(self):
        note = Note(2.0, 'testTwo')
        self.assertEqual(note.getNote(), 2)

    def test_note_equal_6(self):
        note = Note(6.0, 'testTwo')
        self.assertEqual(note.getNote(), 6)

    def test_name_null(self):
        with self.assertRaises(TypeError):
            Note(3.5)

    def test_name_None(self):
        with self.assertRaises(TypeError):
            Note(3.5, None)

    def test_name_empty(self):
        with self.assertRaises(ValueError):
            Note(3.5, '')

    def test_note_smaller_than_2(self):
        with self.assertRaises(ValueError):
            Note(1.3, 'test')

    def test_note_greater_than_6(self):
        with self.assertRaises(ValueError):
            Note(6.1, 'test')

