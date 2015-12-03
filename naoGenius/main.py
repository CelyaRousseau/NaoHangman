import naoGenius
import hangmanGame
import sys

def main():
    nao  = naoGenius.naoGenius()
    word = nao.pickUpAword()
    game = hangmanGame.hangmanGame(word)

    while not (game.isWinner()) and not (game.isOver()):
        letter = raw_input("Donne moi une lettre : ")

        if letter in word and letter not in game.letterChecked:
            print "Cette lettre appartient bien au mot"
            game.completeWord(letter)
            game.letterChecked.append(letter)

        else:
            print "Cette Lettre n'est pas bonne ou a deja ete donnee"

        game.displayIncompleteWord()
        game.turn += 1

    if game.isWinner() :
        print "Tu as gagne"
    else :
        print "Tu es pendu"

if __name__ == "__main__":
    main()
