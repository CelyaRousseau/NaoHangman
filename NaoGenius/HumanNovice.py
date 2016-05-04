# -*- coding: utf-8 -*-
import sys
import random

from NovicePlayer import NovicePlayer

class HumanNovice(NovicePlayer):

	def get_letter(self, game):
		if sys.version_info[0] > 2 :
			letter = input("Veuillez saisir une lettre :")
		else : 
			letter = raw_input("Veuillez saisir une lettre : ")
		return letter