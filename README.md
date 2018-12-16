# simplenet
Quite possibly the simplest neural network you can build...

## Structure
The network has 1 input node, 1 output node and 1 connection between the two, like so:

![Neural Network Diagram](/img/simplenetWHL.png "Neural Network Diagram")

* To see this network with a hidden layer, see the `withHiddenLayer` branch.
* To see this network used to predict the value of a car, see the `predictCarValue` branch.

## Goal 
The goal of this network is to recognise and calculate the required function of an input based on the provided output. For example, when provided with variables A and B, the network will calculate X when B = AX. The network is currently set up to calculate X when provided with A = 1.5 and B = 0.5. These variables map to the nodes in the network where A is the input node, B is the output node and X is the weight of the edge connecting them.

## Usage
Run the network using `python simplenet.py` The network will train 100 times and the output for each run will be displayed in the terminal.
