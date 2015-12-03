import random
from naoGeniusDictionary import dictionary

class naoGenius:

    def __init__(self):
        pass

    def pickUpAword(self):
        wordSelected = random.choice(dictionary)
        return wordSelected