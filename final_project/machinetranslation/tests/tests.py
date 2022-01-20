import unittest
from translator import englishToFrench, frenchToEnglish

class TestNull1(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(None),None)

class TestNull2(unittest.TestCase):
    def test2(self):
        self.assertEqual(englishToFrench(None), None)

class TestenglishToFrench(unittest.TestCase): 
    def test3(self): 
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

class TestFr2En(unittest.TestCase):
    def test4(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
unittest.main()
