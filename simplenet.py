import random

#Generate a random number between 0 and 1 for our starting weight
def randomNum():
    return random.uniform(0.0, 1.0)

#Calculate the cost of the network
def loss():
    global C
    C = (output - desiredOut)**2

#Forward propagate through the network
def forward():
    global inputNode, w, output
    output = inputNode * w

#Backward propagation
def backward():
    global w, r, output, desiredOut, inputNode
    #Adjust the weight 
    w = w - (r *(inputNode*(2*(output - desiredOut))))

#Train the network once
def train():
    backward()
    forward()
    loss()

#Construct the network and populate nodes and weight,
#do one forward propagation to initialize the output node
desiredOut = 0.5
r = 0.1
inputNode = 1.5
w = randomNum()
output = 0
forward() 

for x in range(100): #Train the network 100 times
    train()
    print(x)
    print("Weight: " + str(w))
    print("Output: " + str(output))
    print("Loss:   " + str(C))
    print("----------------------")
