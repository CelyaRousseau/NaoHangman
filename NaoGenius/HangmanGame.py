# -*- coding: utf-8 -*-

class HangmanGame :
	HANGMAN_ERROR_MAX = 10

	def __init__(self, word):
		self.errors = 0
		self.letter_checked = []
		self.word_to_find = word
		self.word_to_complete = ['_'] * len(self.word_to_find)

	def is_over(self):
		return self.errors == self.HANGMAN_ERROR_MAX

	def is_winner(self):
		return self.word_to_find == ''.join(self.word_to_complete)

	def complete_word(self, letter):
		if letter in self.word_to_find :
			indexes = self.get_indexes(letter)
		
			for index in indexes:
				self.word_to_complete[index] = letter


	def display_incomplete_word(self):
		for letter in self.word_to_complete :
			print(" {0} ".format(letter), end=""),

		print("")

	def get_indexes(self, letter):
		indexes = []
		for i in range(0, len(self.word_to_find)):
			if self.word_to_find[i] == letter:
				indexes.append(i)

		return indexes