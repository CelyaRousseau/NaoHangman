# -*- coding: utf-8 -*-
import sys
from NaoGenius import NaoGenius
from HangmanGame import HangmanGame
from drawn.DrawHangman import DrawHangman

def main():
    nao  = NaoGenius()
    word = nao.pick_up_a_word()
    game = HangmanGame(word)
    drawHangman = DrawHangman()

    while not (game.is_winner()) and not (game.is_over()):
        if sys.version_info[0] > 2 :
            letter = input("Donne moi une lettre :")
        else : 
            letter = raw_input("Donne moi une lettre : ")

        if letter in word and letter not in game.letter_checked:
            print("Cette lettre appartient bien au mot")
            game.complete_word(letter)
            game.letter_checked.append(letter)

        else:
        	game.errors += 1
        	drawHangman.drawn_hangman(game.errors)
        	print("Cette lettre n'est pas bonne ou a deja ete donnee")

        game.display_incomplete_word()

    if game.is_winner() :
        print("Tu as gagne")
    else :
        print("Tu es pendu : le mot etait {0}".format(word))

if __name__ == "__main__":
    main()