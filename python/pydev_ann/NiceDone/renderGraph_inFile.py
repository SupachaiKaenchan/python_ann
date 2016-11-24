
import numpy as np
import time
import matplotlib
matplotlib.use('GTKAgg')
from matplotlib import pyplot as plt


def randomwalk(dims=(256, 256), n=20, sigma=5, alpha=0.95, seed=1):
    """ A simple random walk with memory """

    r, c = dims
    gen = np.random.RandomState(seed)
    pos = gen.rand(2, n) * ((r,), (c,))
    old_delta = gen.randn(2, n) * sigma

    while True:
        delta = (1. - alpha) * gen.randn(2, n) * sigma + alpha * old_delta
        pos += delta
        for ii in xrange(n):
            if not (0. <= pos[0, ii] < r):
                pos[0, ii] = abs(pos[0, ii] % r)
            if not (0. <= pos[1, ii] < c):
                pos[1, ii] = abs(pos[1, ii] % c)
        old_delta = delta
        yield pos
        
def readFileToArray(path):
    synapse_0_history = np.load("/ram/synapse_0.txt.npy")
    print synapse_0_history
    
        
    for i in range(0, len(synapse_0_history)):
        tmp = synapse_0_history[i]
        
        #print (str(i) + " / " + str(len(synapse_0_history)))
        #print (str(tmp))
        
        nope = []
        
        
        slot = []
        for j in range(0,len(tmp)):
            slot.append( j)
        
        nope.append(slot)
        nope.append (10*tmp);
        
        
        yield nope


def run(niter=1000, doblit=True):
    """
    Display the simulation using matplotlib, optionally using blit for speed
    """

    graphFilePath = "/ram/synapse.txt"

    fig, ax = plt.subplots(1, 1)
    ax.set_aspect('equal')
    
    rw = readFileToArray(graphFilePath)
    curGraph = rw.next()
    
    ax.set_xlim(-10, 50)
    ax.set_ylim(-20, 20)
    ax.hold(True)
    
    

    plt.show(False)
    plt.draw()

    if doblit:
        # cache the background
        background = fig.canvas.copy_from_bbox(ax.bbox)
        
    a1 = len(curGraph[0])
    a2 = len(curGraph)
    
    print ("graph config " + str(a1) + "," + str(a2))
    points = ax.plot(len(curGraph[0]),len(curGraph),  'o')[0]
    tic = time.time()

    for ii in xrange(niter):

        # update the xy data
        curGraph = rw.next()
        x = curGraph
        #print ("curGraph in loop " + str(curGraph))
        
        points.set_data(x)
            

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
    print "Blit = %s, average FPS: %.2f" % (
        str(doblit), niter / (time.time() - tic))

if __name__ == '__main__':
    #run(doblit=False)
    run(doblit=True)