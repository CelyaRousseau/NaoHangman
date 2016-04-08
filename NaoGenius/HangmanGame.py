# -*- coding: utf-8 -*-
from GeniusPlayer import GeniusPlayer
from NovicePlayer import NovicePlayer
from drawn.DrawHangman import DrawHangman

class HangmanGame :
	HANGMAN_ERROR_MAX = 10

	def __init__(self, genius=None, novice=None):
		if (genius == None or not isinstance(genius, GeniusPlayer)):
			raise ValueError("Genius must be a genius player!")
		if (novice == None or not isinstance(novice, NovicePlayer)):
			raise ValueError("Novice must be a novice player!")

		self._genius = genius
		self._novice = novice
		self._errors = 0
		self._letters_checked = []
		self._word_to_find = ""
		self._word_to_complete = ""
		self._draw_hangman = None

	def launch(self):
		self.init()
		self.run()

	def init(self):
		self.errors = 0
		self._letters_checked = []
		self._word_to_find = self.genius.pick_up_a_word()
		self._word_to_complete = ['_'] * len(self.word_to_find)
		self._draw_hangman = DrawHangman()

	def run(self):
		while not self.is_winner() and not self.is_over():
			letter = self.novice.get_letter(self).lower()
			#print("Lettre donnee : " + letter)
			if letter in self.word_to_find and letter not in self.letters_checked:
			#	print("Cette lettre appartient bien au mot")
				self.nominate_letter(letter)
			else:
			#	print("Cette lettre n'est pas bonne ou a deja ete donnee")
				self.errors += 1
				#self.draw_hangman.drawn_hangman(self.errors)

			#self.display_word()

		if self.is_winner() :
			print("Tu as gagne")
		else :
			print("Tu es pendu : le mot etait {0}".format(self.word_to_find))

	def is_over(self) :
		return self.errors == self.HANGMAN_ERROR_MAX

	def is_winner(self) :
		return self.word_to_find == ''.join(self.word_to_complete)

	def nominate_letter(self, letter):
		self.letters_checked.append(letter)
		if letter in self.word_to_find :
			indexes = self.get_indexes(letter)
		
			for index in indexes:
				self.word_to_complete[index] = letter


	def display_word(self):
		for letter in self.word_to_complete :
			print("{0}".format(letter)),

	def get_indexes(self, letter):
		indexes = []
		for i in range(0, len(self.word_to_find)):
			if self.word_to_find[i] == letter:
				indexes.append(i)

		return indexes

	def _get_errors(self) :
		return self._errors
	def _set_errors(self, value) :
		self._errors = value

	def _get_letters_checked(self) :
		return self._letters_checked
	def _set_letters_checked(self, value) :
		self._letters_checked = value

	def _get_word_to_find(self) :
		return self._word_to_find
	def _set_word_to_find(self, value) :
		self._word_to_find = value

	def _get_word_to_complete(self) :
		return self._word_to_complete
	def _set_word_to_complete(self, value) :
		self._word_to_complete = value

	def _get_draw_hangman(self) :
		return self._draw_hangman
	def _set_draw_hangman(self, value) : 
		self._draw_hangman = value

	def _get_genius(self) :
		return self._genius
	def _set_genius(self, value) : 
		self._genius = value

	def _get_novice(self) :
		return self._novice
	def _set_novice(self, value) : 
		self._novice = value

	errors = property(_get_errors, _set_errors)
	letters_checked = property(_get_letters_checked, _set_letters_checked)
	word_to_find = property(_get_word_to_find, _set_word_to_find)
	word_to_complete = property(_get_word_to_complete, _set_word_to_complete)
	draw_hangman = property(_get_draw_hangman, _set_draw_hangman)
	genius = property(_get_genius, _set_genius)
	novice = property(_get_novice, _set_novice)