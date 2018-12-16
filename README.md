# simplenet
Quite possibly the simplest neural network you can build...

## Structure - Predict Car Value
The network has 2 nodes in the input layer and 1 node in the ouput layer. All connected by edges as shown here:

![Neural Network Diagram](/img/simplenet.png "Neural Network Diagram")

## Goal 
The goal of this network is to value a car based on how many years old it is and how many miles it's done. For example, when provided with the inputs 9 (years old) and 80,000 (miles), the network will calculate 'a', the car value in £. The network is currently set up to calculate 'a' when provided with i0 = 12 (years old) and i1 = 130,000 (miles).

## Usage
Run the network using `python simplenet.py` The network will train 10000 times and the output for each run will be displayed in the terminal. The final output will be the predicted value of the car based on the provided inputs. 
