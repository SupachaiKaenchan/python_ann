
import numpy as np
import time
import matplotlib
matplotlib.use('GTKAgg')
from matplotlib import pyplot as plt



def run(niter=1000, doblit=True):
    alpha = 0.1
    input_dim = 2
    hidden_dim = 16
    output_dim = 1
    
    
    # initialize neural network weights
    synapse_0 = 2*np.random.random((input_dim,hidden_dim)) - 1
    print synapse_0
    
    """
    Display the simulation using matplotlib, optionally using blit for speed
    """

    fig, ax = plt.subplots(1, 1)
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.hold(True)
    

    plt.show(False)
    plt.draw()

    if doblit:
        # cache the background
        background = fig.canvas.copy_from_bbox(ax.bbox)

    print ("curGraph config " + str(input_dim) + " , " + str(hidden_dim) )
    points = ax.plot(input_dim, hidden_dim, 'o')[0]
    tic = time.time()

    for ii in xrange(niter):

        # update the xy data
        synapse_0 = 2*np.random.random((input_dim,hidden_dim)) - 1
        points.set_data(synapse_0)

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
    run(doblit=False)
    #run(doblit=True)