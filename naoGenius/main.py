import naoGenius
import hangmanGame
import sys
from drawn.DrawHangman import DrawHangman

def main():
    nao  = naoGenius.naoGenius()
    word = nao.pickUpAword()
    game = hangmanGame.hangmanGame(word)
    drawHangman = DrawHangman()

    while not (game.isWinner()) and not (game.isOver()):
        letter = raw_input("Donne moi une lettre : ")

        if letter in word and letter not in game.letterChecked:
            print "Cette lettre appartient bien au mot"
            game.completeWord(letter)
            game.letterChecked.append(letter)

        else:
        	game.errors += 1
        	drawHangman.drawn_hangman(game.errors)
        	print "Cette Lettre n'est pas bonne ou a deja ete donnee"

        game.displayIncompleteWord()

    if game.isWinner() :
        print "Tu as gagne"
    else :
        print "Tu es pendu : le mot etait %s" %(word)

if __name__ == "__main__":
    main()
