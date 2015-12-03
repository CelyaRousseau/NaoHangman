# -*- coding: utf-8 -*-
import sys
from NaoBrain import NaoBrain

version = (2,7)
if sys.version_info < version :
    print("Python >= {0}.{1} is required to launch this program".format(version[0], version[1]))
    sys.exit(1)

brain = NaoBrain()
brain.load_file("resources/dictionary.txt")

brain.most_common_letters()
print(brain.letters)
