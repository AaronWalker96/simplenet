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
    global inputNode, w0, w1, output
    output = inputNode * w0 * w1

#Backward propagation
def backward():
    global w0, w1, r, output, desiredOut, inputNode, hiddenNode
    #Adjust the weight for w0
    w0 = w0 - (r*(hiddenNode*(2*(output - desiredOut))))
    #Adjust the weight for w0
    w1 = w1 - (r*(inputNode*(w0*(2*(output - desiredOut)))))

#Train the network once
def train():
    backward()
    forward()
    loss()

#Construct the network and populate nodes and weight,
#do one forward propagation to initialize the output node
desiredOut = 6
r = 0.1
inputNode = 1.5
hiddenNode = 0 
w0 = randomNum()
w1 = randomNum()

output = 0
forward() 

print("Weight 0: " + str(w0))
print("Weight 1: " + str(w1))

for x in range(10000): #Train the network 100 times
    train()
    print(x)
    print("Weight 0: " + str(w0))
    print("Weight 1: " + str(w1))
    print("Output:   " + str(output))
    print("Loss:     " + str(C))
    print("-------------------------")
