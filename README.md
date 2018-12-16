# simplenet
Quite possibly the simplest neural network you can build...

## Structure - With Hidden Layer
The network has 1 node in the input layer, 1 node in the hidden layer and 1 node in the ouput layer. All connected by edges as shown here:

![Neural Network Diagram](/img/simplenetWHL.png "Neural Network Diagram")

## Goal 
The goal of this network is to recognise and calculate the required function of an input based on the provided output. For example, when provided with variables A and B, the network will calculate w0 and w1 when B = Aw0w1. The network is currently set up to calculate w0 and w1 when provided with A = 1.5 and B = 6. These variables map to the nodes in the network where A is the input node, B is the output node and w0 and w1 are the weights of the conecting edges.

## Usage
Run the network using `python simplenet.py` The network will train 1000 times and the output for each run will be displayed in the terminal with the values for w0 and w1.
