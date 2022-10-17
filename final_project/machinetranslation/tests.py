from translator import *

sententence1 = "I need to find my car before my wife finds out"
print(sententence1," ==> ",englishtofrench(sententence1)['translations'][0]['translation'],"\n")

sententence2 = "where is the library?"
print(sententence2," ==> ",englishtofrench(sententence2)['translations'][0]['translation'],"\n")\

sententence3 = "J’ai trouvé une très bonne application pour pratiquer mon français."
print(sententence3," ==> ",frenchtoenglish(sententence3)['translations'][0]['translation'],"\n")

sententence4 = "Oh là là, ce n’est pas la mer à boire"
print(sententence4," ==> ",frenchtoenglish(sententence4)['translations'][0]['translation'],"\n")

#sententence5 = None
#print(sententence5," ==> ",frenchtoenglish(sententence5)['translations'][0]['translation'],"\n")
#ERROR: text must be provided

#sententence5 = ""
#print(sententence5," ==> ",frenchtoenglish(sententence5)['translations'][0]['translation'],"\n")
#ERROR: text can't be empty

sententence5 = "hello"
print(sententence5," ==> ",englishtofrench(sententence5)['translations'][0]['translation'],"\n")

sententence6 = "Bonjour"
print(sententence6," ==> ",frenchtoenglish(sententence6)['translations'][0]['translation'],"\n")
