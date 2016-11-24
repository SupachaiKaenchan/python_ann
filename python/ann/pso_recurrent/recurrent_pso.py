from pso import *
from recurrent import *

class Recurrent (recurrent):
    def hello():
        print "hello"

class Pso(ParticleSwarmOptimizer):
    dimension = 304
    swarmSize = 10
    
    #def __init__(self):
    #    super(Pso, self).__init__()
    def f(self, solution):
        # 304

        re = Recurrent()
        fitness = re.rnn(solution)
        return fitness
        

def main():
    pso = Pso()
    pso.optimize()
 
if  __name__ =='__main__':
    main()
