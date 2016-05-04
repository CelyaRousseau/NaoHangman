# -*- coding: utf-8 -*-
import sys
import random

from NovicePlayer import NovicePlayer
from NaoBrain import NaoBrain

class ArtificialNovice(NovicePlayer):
	ALPHABET = list("abcdefghijklmnopqrstuvwxyz-")

	def __init__(self):
		self._brain = NaoBrain("resources/novice_dictionary.txt")
		self.brain.load()
		self._regexp = ""
		self._letters = []

	def get_letter(self, game):
		current = ''.join(game.word_to_complete)
		print(current)
		# Si nous n'avons auc une informations concernant le mot à trouver
		if len(current.replace('_', '')) == 0 :
			# Si notre dictionnaire n'est pas renseigné
			if len(self.brain.dictionary) == 0 :	
				return self.random_letter(game)
			else :
				if len(self.letters) == 0 :
					self.letters = self.brain.most_common_letters(self.brain.dictionary, []).keys()
				letter = self.letters.pop(0)
				return letter
		else :
			# Création des patterns d'expression régulière
			checked = ''.join(game.letters_checked)
			x = '[^' + checked + ']'
			r = current.replace('_', x)

			# Vérification existence mot
			if self.regexp != r :
				self.regexp = r

				# Récupération de la liste des mots possibles
				matching_words = self.brain.matching_words(self.regexp)

				# Récupération des lettres les plus présentes dans les mots trouvés
				self.letters = self.brain.most_common_letters(matching_words, list(checked)).keys()
			
			if len(self.letters) == 0 :
				self.letters = self.brain.most_common_letters(self.brain.dictionary, list(checked)).keys()
			if len(self.letters) != 0 :
				return self.letters.pop(0)
			else :
				return self.random_letter(game)

	def game_won(self, game):
		print("Félicitations! Vous avez gagné la partie.")

	def game_lost(self, game):
		print("Dommage... Vous avez perdu la partie. " + game.word_to_find)
		self.brain.add_word(game.word_to_find, False)
	
	def random_letter(self, game) :
		import random
		letter = ''
		while letter == '' or letter in game.letters_checked :
			letter = random.sample(ArtificialNovice.ALPHABET, 1)
		return letter[0]

	def _get_brain(self) :
		return self._brain
	def _set_brain(self, value) :
		self._brain = value

	def _get_regexp(self) :
		return self._regexp
	def _set_regexp(self, value) :
		self._regexp = value

	def _get_letters(self) :
		return self._letters
	def _set_letters(self, value) :
		self._letters = value

	brain = property(_get_brain, _set_brain)
	regexp = property(_get_regexp, _set_regexp)
	letters = property(_get_letters, _set_letters)

	