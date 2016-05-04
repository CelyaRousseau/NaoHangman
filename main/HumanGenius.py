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

	def game_won(self, game):
		print("Félicitations! Vous avez gagné la partie.")
		
	def game_lost(self, game):
		print("Dommage... Vous avez perdu la partie.")