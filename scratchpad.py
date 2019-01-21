import random

#Forward propagate through the network
def forwardOld():
    global w0, w1, out
    out0 = (inputNode00* w0) + (inputNode10 * w1)
    out1 = (inputNode01* w0) + (inputNode11 * w1)
    out2 = (inputNode02* w0) + (inputNode12 * w1)
    out3 = (inputNode03* w0) + (inputNode13 * w1)

#Forward propagate through the network
def forwardNew():
    global w0, w1, out, inputNode0, inputNode1
    for x in range(0, len(inputNode0)):
        print(inputNode0[x])
        print(inputNode1[x])
        print("--------")

#Generate a random number between 0 and 1 for our starting weight
def randomNum():
    return random.uniform(0.0, 1.0)

inputNode0 = [0.1, 0.15, 0.11, 0.13, 0.14, 0.13]
inputNode1 = [1.05, 1.14, 1.14, 1.30, 1.24, 0.99]
desiredOut = [0.037, 0.022, 0.025, 0.026, 0.023, 0.023]
out = [0, 0, 0, 0, 0]

w0 = randomNum()
w1 = randomNum()

forwardNew()

