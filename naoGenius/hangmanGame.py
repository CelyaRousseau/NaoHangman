
class hangmanGame:
	HANGMAN_ERROR_MAX = 10

	def __init__(self, word):
		self.errors = 0
		self.letterChecked = []
		self.wordToFind = word
		self.wordToComplete = ['_'] * len(self.wordToFind)

	def isOver(self):
		return self.errors == self.HANGMAN_ERROR_MAX

	def isWinner(self):
		return self.wordToFind == ''.join(self.wordToComplete)

	def completeWord(self, letter):
		if letter in self.wordToFind :
			indexes = self.getIndexes(letter)
		
			for index in indexes:
				self.wordToComplete[index] = letter


	def displayIncompleteWord(self):
		for letter in self.wordToComplete :
			print " %s " %(letter),

		print ""

	def getIndexes(self, letter):
		indexes = []
		for i in range(0, len(self.wordToFind)):
			if self.wordToFind[i] == letter:
				indexes.append(i)

		return indexes