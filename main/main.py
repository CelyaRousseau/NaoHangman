# -*- coding: utf-8 -*-
import sys
import time

from pybrain.structure import SigmoidLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml import NetworkWriter, NetworkReader
from pybrain.datasets import SupervisedDataSet

from pybrain.tools.shortcuts import buildNetwork

from ArtificialNovice import ArtificialNovice
from ArtificialGenius import ArtificialGenius
from HangmanGame import HangmanGame


def main():
    start_time = time.time()
    novice = ArtificialNovice()
    genius = ArtificialGenius()
    game = HangmanGame(genius, novice)

    if __debug__:
        print "------------------- EVALUATION ------------------------"
        network = NetworkReader.readFrom('../perceptron/network_weight1.xml')
        j = 0
        while j < 10:
            game.launch(False, None, network)
            j += 1

        print("--- %s total seconds ---" % (time.time() - start_time))
    else:
        print "------------------- LEARNING ------------------------"
        network = buildNetwork(3, 4, 1, hiddenclass = SigmoidLayer)
        ds = SupervisedDataSet(3, 1)
        i = 0
        while i < 100:
            game.launch(True, ds)
            i += 1

        print " INITIATE trainer : "
        trainer = BackpropTrainer(network, ds)
        print" START trainer : "
        start_time_trainer = time.time()
        trainer.train()
        print("---  END trainer in % seconds ---" % (time.time() - start_time_trainer))
        print " START EXPORT network : "
        NetworkWriter.writeToFile(network, '../perceptron/network_weight2.xml')
        print " END EXPORT network : "


if __name__ == "__main__":
    version = (2, 7)
    if sys.version_info < version:
        print("Python >= {0}.{1} is required to launch this program".format(version[0], version[1]))
        sys.exit(1)

    main()