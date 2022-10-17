import sys
import unittest

sys.path.append("..") 
from translator import *

class tranlatorTester(unittest.TestCase):

    def tests(self):
        sententence1 = "I need to find my car before my wife finds out"
        #print(sententence1," ==> ",englishtofrench(sententence1)['translations'][0]['translation'],"\n")
        translation=englishtofrench(sententence1)['translations'][0]['translation']
        self.assertEqual(translation,"J'ai besoin de trouver ma voiture avant que ma femme ne découvre")
        
        sententence2 = "where is the library?"
        #print(sententence2," ==> ",englishtofrench(sententence2)['translations'][0]['translation'],"\n")
        translation=englishtofrench(sententence2)['translations'][0]['translation']
        self.assertEqual(translation,"Où est la bibliothèque?")

        sententence3 = "J’ai trouvé une très bonne application pour pratiquer mon français."
        #print(sententence3," ==> ",frenchtoenglish(sententence3)['translations'][0]['translation'],"\n")
        translation=frenchtoenglish(sententence3)['translations'][0]['translation']
        self.assertEqual(translation,"I found a very good application to practice my French.")

        sententence4 = "Oh là là, ce n’est pas la mer à boire"
        #print(sententence4," ==> ",frenchtoenglish(sententence4)['translations'][0]['translation'],"\n")
        translation=frenchtoenglish(sententence4)['translations'][0]['translation']
        self.assertEqual(translation,"Oh there, it's not the sea to drink")

        sententence5 = None
        #print(sententence5," ==> ",frenchtoenglish(sententence5)['translations'][0]['translation'],"\n")
        #ERROR: text must be provided
        with self.assertRaises(ValueError) as cm:
            self.assertEqual(englishtofrench(sententence5)['translations'][0]['translation'],None)
        
        print("Error with Imput being 'None': ",str(cm.exception))

        #sententence5 = ""
        #print(sententence5," ==> ",frenchtoenglish(sententence5)['translations'][0]['translation'],"\n")
        #ERROR: text can't be empty

        sententence5 = "hello"
        translation=englishtofrench(sententence5)['translations'][0]['translation']
        #print(sententence5," ==> ",englishtofrench(sententence5)['translations'][0]['translation'],"\n")
        self.assertEqual(translation,"Bonjour")

        sententence6 = "Bonjour"
        translation=frenchtoenglish(sententence6)['translations'][0]['translation']
        #print(sententence6," ==> ",englishtofrench(sententence6)['translations'][0]['translation'],"\n")
        self.assertEqual(translation,"Hello")
        
    


if __name__=='__main__':
    unittest.main()