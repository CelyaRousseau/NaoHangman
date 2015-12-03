# -*- coding: utf-8 -*-
import sys
import random
from NaoBrain import NaoBrain

class NaoGenius:

	def __init__(self):
		self._brain = NaoBrain()
		self._brain.load_file("resources/dictionary.txt")
		
	def pick_up_a_word(self):
		if sys.version_info[0] > 2 :
			return random.choice(list(self.brain.dictionary.keys()))
		else :
			return random.choice(self.brain.dictionary.keys())

	def _get_brain(self) :
		return self._brain
	def _set_brain(self, value) :
		self._brain = value

	brain = property(_get_brain, _set_brain)