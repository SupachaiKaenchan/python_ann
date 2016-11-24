import math
import random
import sys

INPUT_NEURONS = 4
HIDDEN_NEURONS = 6
OUTPUT_NEURONS = 14

LEARN_RATE = 0.2 # Rho.
NOISE_FACTOR = 0.58
TRAINING_REPS = 10000
MAX_SAMPLES = 14

TRAINING_INPUTS = [[1, 1, 1, 0], 
                   [1, 1, 0, 0], 
                   [0, 1, 1, 0], 
                   [1, 0, 1, 0], 
                   [1, 0, 0, 0], 
                   [0, 1, 0, 0], 
                   [0, 0, 1, 0], 
                   [1, 1, 1, 1], 
                   [1, 1, 0, 1], 
                   [0, 1, 1, 1], 
                   [1, 0, 1, 1], 
                   [1, 0, 0, 1], 
                   [0, 1, 0, 1], 
                   [0, 0, 1, 1]]

TRAINING_OUTPUTS = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]


class Example_4x6x16:
    def __init__(self, numInputs, numHidden, numOutput, learningRate, noise, epochs, numSamples, inputArray, outputArray):
        self.mInputs = numInputs
        self.mHiddens = numHidden
        self.mOutputs = numOutput
        self.mLearningRate = learningRate
        self.mNoiseFactor = noise
        self.mEpochs = epochs
        self.mSamples = numSamples
        self.mInputArray = inputArray
        self.mOutputArray = outputArray

        self.wih = [] # Input to Hidden Weights
        self.who = [] # Hidden to Output Weights
        inputs = []
        hidden = []
        target = []
        actual = []
        erro = []
        errh = []
        return

    def initialize_arrays(self):
        for i in range(self.mInputs + 1): # The extra element represents bias node.
            self.wih.append([0.0] * self.mHiddens)
            for j in range(self.mHiddens):
                # Assign a random weight value between -0.5 and 0.5
                self.wih[i][j] = random.random() - 0.5

        for i in range(self.mHiddens + 1): # The extra element represents bias node.
            self.who.append([0.0] * self.mOutputs)
            for j in range(self.mOutputs):
                self.who[i][j] = random.random() - 0.5

        self.inputs = [0.0] * self.mInputs
        self.hidden = [0.0] * self.mHiddens
        self.target = [0.0] * self.mOutputs
        self.actual = [0.0] * self.mOutputs
        self.erro = [0.0] * self.mOutputs
        self.errh = [0.0] * self.mHiddens

        return

    def get_maximum(self, vector):
        # This function returns an array index of the maximum.
        index = 0
        maximum = vector[0]
        length = len(vector)

        for i in range(length):
            if vector[i] > maximum:
                maximum = vector[i]
                index = i

        return index

    def sigmoid(self, value):
        return 1.0 / (1.0 + math.exp(-value))

    def sigmoid_derivative(self, value):
        return value * (1.0 - value)

    def feed_forward(self):
        total = 0.0

        # Calculate input to hidden layer.
        for j in range(self.mHiddens):
            total = 0.0
            for i in range(self.mInputs):
                total += self.inputs[i] * self.wih[i][j]

            # Add in bias.
            total += self.wih[self.mInputs][j]
            self.hidden[j] = self.sigmoid(total)

        # Calculate the hidden to output layer.
        for j in range(self.mOutputs):
            total = 0.0
            for i in range(self.mHiddens):
                total += self.hidden[i] * self.who[i][j]

            # Add in bias.
            total += self.who[self.mHiddens][j]
            self.actual[j] = self.sigmoid(total)

        return

    def back_propagate(self):
        # Calculate the output layer error (step 3 for output cell).
        for j in range(self.mOutputs):
            self.erro[j] = (self.target[j] - self.actual[j]) * self.sigmoid_derivative(self.actual[j])

        # Calculate the hidden layer error (step 3 for hidden cell).
        for i in range(self.mHiddens):
            self.errh[i] = 0.0
            for j in range(self.mOutputs):
                self.errh[i] += self.erro[j] * self.who[i][j]

            self.errh[i] *= self.sigmoid_derivative(self.hidden[i])

        # Update the weights for the output layer (step 4).
        for j in range(self.mOutputs):
            for i in range(self.mHiddens):
                self.who[i][j] += (self.mLearningRate * self.erro[j] * self.hidden[i])

            # Update the bias.
            self.who[self.mHiddens][j] += (self.mLearningRate * self.erro[j])

        # Update the weights for the hidden layer (step 4).
        for j in range(self.mHiddens):
            for i in range(self.mInputs):
                self.wih[i][j] += (self.mLearningRate * self.errh[j] * self.inputs[i])

            # Update the bias.
            self.wih[self.mInputs][j] += (self.mLearningRate * self.errh[j])

        return

    def print_training_stats(self):
        sum = 0.0

        for i in range(self.mSamples):
            for j in range(self.mInputs):
                self.inputs[j] = self.mInputArray[i][j]

            for j in range(self.mOutputs):
                self.target[j] = self.mOutputArray[i][j]

            self.feed_forward()

            if self.get_maximum(self.actual) == self.get_maximum(self.target):
                sum += 1
            else:
                sys.stdout.write(str(self.inputs[0]) + "\t" + str(self.inputs[1]) + "\t" + str(self.inputs[2]) + "\t" + str(self.inputs[3]) + "\n")
                sys.stdout.write(str(self.get_maximum(self.actual)) + "\t" + str(self.get_maximum(self.target)) + "\n")
        
        sys.stdout.write("Network is " + str((float(sum) / float(MAX_SAMPLES)) * 100.0) + "% correct.\n")

        return

    def train_network(self):
        sample = 0

        for i in range(self.mEpochs):
            sample += 1
            if sample == self.mSamples:
                sample = 0

            for j in range(self.mInputs):
                self.inputs[j] = self.mInputArray[sample][j]

            for j in range(self.mOutputs):
                self.target[j] = self.mOutputArray[sample][j]

            self.feed_forward()

            self.back_propagate()
        
        return
    
    def test_network(self):
        for i in range(self.mSamples):
            for j in range(self.mInputs):
                self.inputs[j] = self.mInputArray[i][j]
            
            self.feed_forward()
            
            for j in range(self.mInputs):
                sys.stdout.write(str(self.inputs[j]) + "\t")
            
            sys.stdout.write("Output: " + str(self.get_maximum(self.actual)) + "\n")
        
        return
    
    def test_network_with_noise(self):
        # This function adds a random fractional value to all the training inputs greater than zero.
        for i in range(self.mSamples):
            for j in range(self.mInputs):
                self.inputs[j] = self.mInputArray[i][j] + (random.random() * NOISE_FACTOR)
            
            self.feed_forward()
            
            for j in range(self.mInputs):
                sys.stdout.write("{:03.3f}".format(((self.inputs[j] * 1000.0) / 1000.0)) + "\t")
            
            sys.stdout.write("Output: " + str(self.get_maximum(self.actual)) + "\n")
        
        return

if __name__ == '__main__':
    ex = Example_4x6x16(INPUT_NEURONS, HIDDEN_NEURONS, OUTPUT_NEURONS, LEARN_RATE, NOISE_FACTOR, TRAINING_REPS, MAX_SAMPLES, TRAINING_INPUTS, TRAINING_OUTPUTS)
    ex.initialize_arrays()
    ex.train_network()
    ex.print_training_stats()
    sys.stdout.write("\nTest network against original input:\n")
    ex.test_network()
    sys.stdout.write("\nTest network against noisy input:\n")
    ex.test_network_with_noise()
    
