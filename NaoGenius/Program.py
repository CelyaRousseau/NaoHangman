# -*- coding: utf-8 -*-

import sys

version = (2,7)
if sys.version_info < version :
    print("Python >= {0}.{1} is required to launch this program".format(version[0], version[1]))
    sys.exit(1)

import random
LETTERS = list("abcdefghijklmnopqrstuvwxyz-")
print(random.sample(LETTERS, 1))