import copy, numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib
from gi.overrides.Gdk import Color


matplotlib.use('GTKAgg')


np.random.seed(0)


class recurrent:

    # input variables
    alpha = 0.1
    input_dim = 2
    hidden_dim = 16
    output_dim = 1

    # initialize neural network weights
    synapse_0 = 2*np.random.random((input_dim,hidden_dim)) - 1
    synapse_1 = 2*np.random.random((hidden_dim,output_dim)) - 1
    synapse_h = 2*np.random.random((hidden_dim,hidden_dim)) - 1

    # compute sigmoid nonlinearity
    def sigmoid(self,x):
        output = 1/(1+np.exp(-x))
        return output

    # convert output of sigmoid function to its derivative
    def sigmoid_output_to_derivative(self,output):
        return output*(1-output)

    def linearArray(self,arr):
        x = []
        
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                x.append(arr[i][j])
            
        return x

    def linearArray2(self,arr,arr2 , arr3):
        x = []
        
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                x.append(arr[i][j])
            
        for i in range(len(arr2)):
            for j in range(len(arr2[i])):
                x.append(arr2[i][j])
        
        for i in range(len(arr3)):
            for j in range(len(arr3[i])):
                x.append(arr3[i][j])
        
            
        return x

    def getWeight(self):

        va = []
        
        for i in range(input_dim):
            for j in range(hidden_dim):
                va.append(synapse_0[i][j])    

        for i in range(hidden_dim):
            for j in range(output_dim):
                va.append(synapse_1[i][j])    

        for i in range(hidden_dim):
            for j in range(hidden_dim):
                va.append(synapse_h[i][j])

        return va


    def setWeight(self,va):
        counter = 0
        
        for i in range(self.input_dim):
            for j in range(self.hidden_dim):
                self.synapse_0[i][j] = va[counter]

        for i in range(self.hidden_dim):
            for j in range(self.output_dim):
                self.synapse_1[i][j] = va[counter]

        for i in range(self.hidden_dim):
            for j in range(self.hidden_dim):
                self.synapse_h[i][j] = va[counter]

        return




    def rnn(self,va, graph=True,doblit=True):
        """
        Display the simulation using matplotlib, optionally using blit for speed
        """
        

        
        # training dataset generation
        int2binary = {}
        binary_dim = 8
        
        largest_number = pow(2,binary_dim)
        binary = np.unpackbits(
            np.array([range(largest_number)],dtype=np.uint8).T,axis=1)
        for i in range(largest_number):
            int2binary[i] = binary[i]
        
        

        #print ("" + str(input_dim * hidden_dim) + " + " + str(hidden_dim * output_dim) + " + " + str(hidden_dim * hidden_dim))
        


        self.setWeight(va)
 

        maxLop = 100
        
        #txt = open ("/ram/synapse.txt","w")

        fitness = 0
        
        # training logic
        for j in range(0,maxLop):
            
            linArr = self.linearArray2(self.synapse_0 , self.synapse_1 , self.synapse_h)
            #print ("synapse_0 " + str(synapse_0))
            #print("lin " + str(linArr))
            
           
            
            
            #txt.write(str(linArr) + "\n")
            #for gg in range (0,len(linArr)):
            #    txt.write(str(linArr[gg]) + ",")
            
            
            
            # generate a simple addition problem (a + b = c)
            a_int = np.random.randint(largest_number/2) # int version
            a = int2binary[a_int] # binary encoding
        
            b_int = np.random.randint(largest_number/2) # int version
            b = int2binary[b_int] # binary encoding
        
            # true answer
            c_int = a_int + b_int
            c = int2binary[c_int]
            
            # where we'll store our best guess (binary encoded)
            d = np.zeros_like(c)
        
            overallError = 0
        
            #these list keep 8 bit state
            layer_2_deltas = list()
            layer_1_values = list()
            layer_1_values.append(np.zeros(self.hidden_dim))
            
            # moving along the positions in the binary encoding
            for position in range(binary_dim):
                
                # generate input and output
                X = np.array([[a[binary_dim - position - 1],b[binary_dim - position - 1]]])
                y = np.array([[c[binary_dim - position - 1]]]).T
        
                # hidden layer (input ~+ prev_hidden)
                layer_1 = self.sigmoid(np.dot(X,self.synapse_0) + np.dot(layer_1_values[-1],self.synapse_h))
        
                # output layer (new binary representation)
                layer_2 = self.sigmoid(np.dot(layer_1,self.synapse_1))
        
                # did we miss?... if so, by how much?
                layer_2_error = y - layer_2
                layer_2_deltas.append((layer_2_error)*self.sigmoid_output_to_derivative(layer_2))
                overallError += np.abs(layer_2_error[0])
            
                # decode estimate so we can print it out
                d[binary_dim - position - 1] = np.round(layer_2[0][0])
                
                # store hidden layer so we can use it in the next timestep
                layer_1_values.append(copy.deepcopy(layer_1))
            
            future_layer_1_delta = np.zeros(self.hidden_dim)
            fitness += overallError
            
            # print out progress
            #print j
            if(j % 100000 == 9999):
                print "Error:" + str(overallError)
                print "Pred:" + str(d)
                print "True:" + str(c)
                out = 0
                for index,x in enumerate(reversed(d)):
                    out += x*pow(2,index)
                print str(a_int) + " + " + str(b_int) + " = " + str(out)
                print "------------"
                
                #plt.show()
                #plt.pause(0.0001) #Note this correction

                #time.sleep(0.1)
                #plt.pause(0.0001)   

            #print ("dataGraph " + str(dataGraph))
            
        #print ("fitness " + str(fitness))
        return fitness
        
    
def main():
    ree = recurrent()
    
    weight = ree.getWeight()    
    
    ree.rnn(weight)
 
if  __name__ =='__main__':
    main()
