import random

#Generate a random number between 0 and 1 for our starting weight
def randomNum():
    return random.uniform(0.0, 1.0)

#Calculate the cost of the network
def loss(actualOut, desiredOut):
    global C
    C = (actualOut - desiredOut)**2

#Forward propagate through the network
def forward():
    global w0, w1, out0, out1, out2, out3
    out0 = (inputNode00* w0) + (inputNode10 * w1)
    out1 = (inputNode01* w0) + (inputNode11 * w1)
    out2 = (inputNode02* w0) + (inputNode12 * w1)
    out3 = (inputNode03* w0) + (inputNode13 * w1)

#Forward propagate through the network
def predict(in1, in2):
    global w0, w1, outp
    outp = (in1* w0) + (in2 * w1)

#Backward propagation
def backward():
    global w0, w1, r, out0, out1, out2, out3, desiredOut0, inputNode00, inputNode10
    #Adjust the weight for w0
    w0 = w0 - (r*(inputNode00*(2*(out0 - desiredOut0))))
    #Adjust the weight for w1
    w1 = w1 - (r*(inputNode10*(2*(out0 - desiredOut0))))
    loss(out0, desiredOut0)

    #Adjust the weight for w0
    w0 = w0 - (r*(inputNode01*(2*(out1 - desiredOut1))))
    #Adjust the weight for w1
    w1 = w1 - (r*(inputNode11*(2*(out1 - desiredOut1))))
    loss(out1, desiredOut1)

    #Adjust the weight for w0
    w0 = w0 - (r*(inputNode02*(2*(out2 - desiredOut2))))
    #Adjust the weight for w1
    w1 = w1 - (r*(inputNode12*(2*(out2 - desiredOut2))))
    loss(out2, desiredOut2)

    #Adjust the weight for w0
    w0 = w0 - (r*(inputNode03*(2*(out3 - desiredOut3))))
    #Adjust the weight for w1
    w1 = w1 - (r*(inputNode13*(2*(out3 - desiredOut3))))
    loss(out3, desiredOut3)

#Train the network once
def train():
    backward()
    forward()

#Construct the network and populate nodes and weight,
#do one forward propagation to initialize the output node
r = 0.1
inputNode00 = 0.09
inputNode10 = 1.05
desiredOut0 = 0.037
out0 = 0

inputNode01 = 0.14
inputNode11 = 1.14
desiredOut1 = 0.022
out1 = 0

inputNode02 = 0.10
inputNode12 = 1.14
desiredOut2 = 0.025
out2 = 0

inputNode03 = 0.12
inputNode13 = 1.30
desiredOut3 = 0.026
out3 = 0

w0 = randomNum()
w1 = randomNum()

forward() 

print("Weight 0: " + str(w0))
print("Weight 1: " + str(w1))

for x in range(100000): #Train the network 1000 times
    train()
    print(x)
    print("Weight 0: " + str(w0))
    print("Weight 1: " + str(w1))
    print("Output:   " + str(out0))
    print("Loss:     " + str(C))
    print("-------------------------")

predict(0.12, 1.30)

predicted = outp*100

print("-------------------------")
print("Predicted value:   " + str(round(predicted, 3)))
print("-------------------------")
