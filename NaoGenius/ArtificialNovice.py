# -*- coding: utf-8 -*-
import sys
import random

from NovicePlayer import NovicePlayer
from NaoBrain import NaoBrain

class ArtificialNovice(NovicePlayer):
	LETTERS = list("abcdefghijklmnopqrstuvwxyz-")

	def __init__(self):
		self._brain = NaoBrain()
		self._brain.load_file("resources/dictionary.txt")
		self._regexp = ""

	def get_letter(self, game):
		current = ''.join(game.word_to_complete)

		# Si nous n'avons aucune informations concernant le mot à trouver
		if (len(current.replace('_', '')) == 0) :
			# Si notre dictionnaire n'est pas renseigné
			if (len(self.brain.dictionary) == 0) :			
				import random
				letter = ''
				while (letter == '' or letter in game.letters_checked) :
					letter = random.sample(ArtificialNovice.LETTERS, 1)
				return letter[0]
			else : 
				self.letters = self.brain.most_common_letters(self.brain.dictionary, []).keys()
				return self.letters.pop(0)
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

			if (len(self.letters) != 0) :
				return self.letters.pop(0)
			else :
				return 'oifjosdkdspd'

	def _get_brain(self) :
		return self._brain
	def _set_brain(self, value) :
		self._brain = value

	def _get_regexp(self) :
		return self._regexp
	def _set_regexp(self, value) :
		self._regexp = value

	brain = property(_get_brain, _set_brain)
	regexp = property(_get_regexp, _set_regexp)

	