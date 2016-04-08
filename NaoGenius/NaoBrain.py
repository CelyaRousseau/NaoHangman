# -*- coding: utf-8 -*-
import sys
from FileAccess import FileAccess

class NaoBrain():
	"""
	NaoBrain class.
	"""

	def __init__(self) :
		"""
		NaoBrain constuctor
		"""
		self._dictionary = {}
		self._letters = {}

	def add_word(self, word) :
		if sys.version_info[0] > 2 :
			from unidecode import unidecode
			temp = unidecode(word)
		else : 
			temp = word

		self.dictionary[temp] = temp

	def most_common_letters(self, array={}, excluded=[]) :
		letters = {}
		for word in array :
			for letter in word.lower() :
				if letter in excluded : 
					continue
				if letter in letters :
					letters[letter] = letters[letter] + 1
				else :
					letters[letter] = 1

		from collections import OrderedDict
		from operator import itemgetter
		letters = OrderedDict(sorted(letters.items(), key=itemgetter(1), reverse=True))

		return letters

	def load_file(self, file) :
		words = FileAccess.load_file(file)
		i = int(0)
		for word in words :
			self.add_word(word)
			i = i + 1

	def save_file(self, file) :
		file_content = ""
		for word in self.dictionary :
			file_content += word + "\n"
		FileAccess.save_file(file_content)

	def matching_words(self, word) :
		import re;
		match = re.compile('^' + word + '$')
		matches = []
		for word in self.dictionary :
			if match.match(word) :
				matches.append(word)

		return matches

	def _get_dictionary(self) :
		return self._dictionary
	def _set_dictionary(self, value) :
		self._dictionary = value

	def _get_letters(self) :
		return self._letters
	def _set_letters(self, value) :
		self._letters = value

	dictionary = property(_get_dictionary, _set_dictionary)
	letters = property(_get_letters, _set_letters)