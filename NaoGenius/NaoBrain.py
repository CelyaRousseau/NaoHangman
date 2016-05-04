# -*- coding: utf-8 -*-
import sys
from FileAccess import FileAccess

class NaoBrain():
	"""
	NaoBrain class.
	"""

	def __init__(self, file=None) :
		"""
		NaoBrain constuctor
		"""
		self._dictionary = {}
		self._letters = {}
		self._file = file

	
	def add_word(self, word, loading=True) :
		if sys.version_info[0] > 2 :
			from unidecode import unidecode
			temp = unidecode(word)
		else : 
			temp = word
		
		if not loading :
			try:
				self.dictionary[temp] != None
				already_exists = True
			except KeyError:
				already_exists = False

			if not already_exists :
				self.append_word_to_file("resources/novice_dictionary.txt", temp)
		
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

	def load(self) :
		self.load_file(self.file)

	def save_file(self, file) :
		file_content = ""
		for word in self.dictionary :
			file_content += word + "\n"
		FileAccess.save_file(file_content)

	def append_word_to_file(self, file, word) :
		FileAccess.append_line(file, word)

	def matching_words(self, word) :
		import re;

		matches = []
		word = word.replace('-','')		
		match = re.compile('^' + word + '$')
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

	def _get_file(self) :
		return self._file
	def _set_file(self, value) :
		self._file = value

	dictionary = property(_get_dictionary, _set_dictionary)
	letters = property(_get_letters, _set_letters)
	file = property(_get_file, _set_file)