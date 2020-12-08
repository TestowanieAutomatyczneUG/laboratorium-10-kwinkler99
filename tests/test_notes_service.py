import unittest
from src.sample.notes_service import NotesService
from src.sample.notes_storage import NotesStorage
from src.sample.note import Note
from unittest.mock import *


class TestNote(unittest.TestCase):
    @patch.object(NotesStorage, 'add')
    def test_add(self, mock_method):
        # prepare mock
        mock_method.return_value = Note(5.0, "Kasia")
        # testing
        test_object = NotesService()
        result = test_object.add(Note(5.0, "Kasia"))
        self.assertEqual(Note(5.0, "Kasia").name, result.getName())

    @patch.object(NotesStorage, 'clear')
    def test_clear(self, mock_method):
        # prepare mock
        mock_method.return_value = []
        # testing
        test_object = NotesService()
        result = test_object.clear()
        self.assertEqual([], result)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_get_all_notes_off(self, mock_method):
        # prepare mock
        mock_method.return_value = [Note(5.0, "Marlena"), Note(3.5, "Marlena"), Note(2.0, "Marlena"), Note(4.5, "Marlena")]
        # testing
        test_object = NotesService()
        result = test_object.averageOf("Marlena")
        self.assertEqual(3.75, result)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_get_all_notes_off_error(self, mock_method):
        # prepare mock
        mock_method.return_value = []
        # testing
        test_object = NotesService()
        result = test_object.averageOf
        self.assertRaises(ValueError, result, "Marlena")
