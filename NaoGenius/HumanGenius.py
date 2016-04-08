# -*- coding: utf-8 -*-
import sys
import random

from GeniusPlayer import GeniusPlayer

class HumanGenius(GeniusPlayer):
	def pick_up_a_word(self):
		if sys.version_info[0] > 2 :
			word = input("Veuillez choisir un mot :")
		else : 
			word = raw_input("Veuillez choisir un mot : ")

		return word