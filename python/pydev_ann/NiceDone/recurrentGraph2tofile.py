import copy, numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib
from gi.overrides.Gdk import Color


matplotlib.use('GTKAgg')


np.random.seed(0)

# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)

def linearArray(arr):
    x = []
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            x.append(arr[i][j])
        
    return x

def getWeight(synapse_0, synapse_1, synapse_h , input_dim , hidden_dim , output_dim):

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

def linearArray2(arr,arr2 , arr3):
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

def rnn(graph=True,doblit=True):
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
    
    
    # input variables
    alpha = 0.1
    input_dim = 2
    hidden_dim = 16
    output_dim = 1
    
    
    # initialize neural network weights
    synapse_0 = 2*np.random.random((input_dim,hidden_dim)) - 1
    synapse_1 = 2*np.random.random((hidden_dim,output_dim)) - 1
    synapse_h = 2*np.random.random((hidden_dim,hidden_dim)) - 1
    
    
    
    synapse_0_update = np.zeros_like(synapse_0)
    synapse_1_update = np.zeros_like(synapse_1)
    synapse_h_update = np.zeros_like(synapse_h)
     
         
   
     
#graph
    fig, ax = plt.subplots(1, 1)
    
    ax.set_aspect('equal')
    ax.set_xlim(-10, 350)
    ax.set_ylim(-100, 100)
    ax.hold(True)


    plt.show(False)
    plt.draw()


    if doblit:
        # cache the background
        background = fig.canvas.copy_from_bbox(ax.bbox)
    
    
    
    points = ax.plot(1, 1, 'o')[0]

        
    tic = time.time()

    maxLop = 10000
    
    #txt = open ("/ram/synapse.txt","w")

    fileWeight = []
    
    # training logic
    for j in range(0,maxLop):
        
        linArr = linearArray2(synapse_0 , synapse_1 , synapse_h)
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
        layer_1_values.append(np.zeros(hidden_dim))
        
        # moving along the positions in the binary encoding
        for position in range(binary_dim):
            
            # generate input and output
            X = np.array([[a[binary_dim - position - 1],b[binary_dim - position - 1]]])
            y = np.array([[c[binary_dim - position - 1]]]).T
    
            # hidden layer (input ~+ prev_hidden)
            layer_1 = sigmoid(np.dot(X,synapse_0) + np.dot(layer_1_values[-1],synapse_h))
    
            # output layer (new binary representation)
            layer_2 = sigmoid(np.dot(layer_1,synapse_1))
    
            # did we miss?... if so, by how much?
            layer_2_error = y - layer_2
            layer_2_deltas.append((layer_2_error)*sigmoid_output_to_derivative(layer_2))
            overallError += np.abs(layer_2_error[0])
        
            # decode estimate so we can print it out
            d[binary_dim - position - 1] = np.round(layer_2[0][0])
            
            # store hidden layer so we can use it in the next timestep
            layer_1_values.append(copy.deepcopy(layer_1))
        
        future_layer_1_delta = np.zeros(hidden_dim)
    
        # learning
        for position in range(binary_dim):
            
            X = np.array([[a[position],b[position]]])
            # grab layer1 current and prev layer
            layer_1 = layer_1_values[-position-1]
            prev_layer_1 = layer_1_values[-position-2]
            
            # error at output layer
            layer_2_delta = layer_2_deltas[-position-1]
            # error at hidden layer
            layer_1_delta = (future_layer_1_delta.dot(synapse_h.T) + layer_2_delta.dot(synapse_1.T)) * sigmoid_output_to_derivative(layer_1)
    
            # let's update all our weights so we can try again
            synapse_1_update += np.atleast_2d(layer_1).T.dot(layer_2_delta)
            synapse_h_update += np.atleast_2d(prev_layer_1).T.dot(layer_1_delta)
            synapse_0_update += X.T.dot(layer_1_delta)
            
            future_layer_1_delta = layer_1_delta
        
    
        synapse_0 += synapse_0_update * alpha
        synapse_1 += synapse_1_update * alpha
        synapse_h += synapse_h_update * alpha    
    
        synapse_0_update *= 0
        synapse_1_update *= 0
        synapse_h_update *= 0

        fileWeight.append(getWeight(synapse_0,synapse_1,synapse_h , input_dim , hidden_dim , output_dim))
        
        # print out progress
        #print j
        if(j % 1000 == 0):
            
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
        
        if (j % 100 == 0 ):
            dataGraph = []
       
            slot = []
            for jj in range(0,len(linArr)):
                slot.append( jj)
            
            dataGraph.append(slot)
            dataGraph.append(np.dot(linArr,10));
            
        
            points.set_data(dataGraph )
            
            
            
            if doblit:
                # restore background
                fig.canvas.restore_region(background)
    
                # redraw just the points
                ax.draw_artist(points)
    
                # fill in the axes rectangle
                fig.canvas.blit(ax.bbox)
    
            else:
                # redraw everything
                fig.canvas.draw()

    plt.close(fig)
    
    text_file = open("/ram/output.txt", "w")
    for oo in range (len(fileWeight)):
        yap = fileWeight[oo]
        for ee in range ((input_dim * hidden_dim) + (hidden_dim * output_dim) + (hidden_dim * hidden_dim)):
            text_file.write(str(yap[ee]) + " ")

        text_file.write("\n")
    text_file.close()
    
    print "Blit = %s, average FPS: %.2f" % (
        str(doblit), maxLop / (time.time() - tic))
    
def run(graph=True , doblit=True):
    a = rnn(graph,doblit);
    
if __name__ == '__main__':
    run(graph=True,doblit=True)
    #run(doblit=True) 
