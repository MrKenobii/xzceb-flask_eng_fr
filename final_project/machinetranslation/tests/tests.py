import unittest
from translator import french_to_english, english_to_french

class TestLanguage(unittest.TestCase):
    def testEnglish(self):
        self.assertNotEqual(english_to_french('Hello'), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def testFrench(self):
        self.assertNotEqual(french_to_english('Bonjour'),'')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


unittest.main()