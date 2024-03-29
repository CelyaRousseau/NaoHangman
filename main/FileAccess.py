# -*- coding: utf-8 -*-
import sys
import io
import unicodedata

class FileAccess():

	@staticmethod
	def load_file(file) :
		if sys.version_info[0] > 2 :
			with open(file, 'r', encoding='ISO-8859-1') as file_stream :
				lines = []
				for line in file_stream :
					lines.append(line[:-1])
		else :
			with io.open(file, 'r', encoding='ISO-8859-1') as file_stream :
				lines = []
				for line in file_stream :
					lines.append(line[:-1].encode('utf-8'))
		return lines

	@staticmethod
	def save_file(file, text) :
		with open(file, "w+") as file_stream :
			file_stream.write(text)
			file_stream.close()

	@staticmethod
	def append_line(file, text) :
		with open(file, "a+") as file_stream :
			file_stream.write(text + "\n")
			file_stream.close()