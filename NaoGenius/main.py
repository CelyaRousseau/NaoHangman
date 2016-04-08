# -*- coding: utf-8 -*-
import sys
from HumanNovice import HumanNovice
from HumanGenius import HumanGenius
from ArtificialNovice import ArtificialNovice
from ArtificialGenius import ArtificialGenius
from HangmanGame import HangmanGame


def main():
	novice = ArtificialNovice()
	genius = ArtificialGenius()

	game = HangmanGame(genius, novice)

	while (True):
		game.launch()

if __name__ == "__main__":
	main()