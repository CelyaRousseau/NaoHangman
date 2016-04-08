from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from jeu_essais import learningData

def main():
	# Training
	net = buildNetwork(3, 4, 1, hiddenclass=SigmoidLayer)
	ds = SupervisedDataSet(3, 1)

	for x in learningData :
		ds.addSample(x[0], x[1])
	

	print ds
	trainer = BackpropTrainer(net, ds)
	print trainer.train()



	# n = FeedForwardNetwork()
	# inLayer = LinearLayer(2)
	# hiddenLayer = SigmoidLayer(3)
	# outLayer = LinearLayer(1)

	# n.addInputModule(inLayer)
	# n.addModule(hiddenLayer)
	# n.addOutputModule(outLayer)


if __name__ == "__main__":
	main()