 
import random
import copy
 
w = 0.729844 # Inertia weight to prevent velocities becoming too large
c1 = 1.496180 # Scaling co-efficient on the social component
c2 = 1.496180 # Scaling co-efficient on the cognitive component
dimension = 2 # Size of the problem
iterations = 1000
swarmSize = 10
 
# This class contains the code of the Particles in the swarm
class Particle:
    velocity = []
    pos = []
    pBest = []
 
    def __init__(self):
        self.velocity = []
        self.pos = []
        self.pBest = []
        
        for i in range(dimension):
            self.pos.append(random.random())
            self.velocity.append(0.01 * random.random())
            self.pBest.append(self.pos[i])
        return
 
    def updatePositions(self):
        for i in range(dimension):
            self.pos[i] = self.pos[i] + self.velocity[i]   
        return
 
    def updateVelocities(self, gBest):
        for i in range(dimension):
            r1 = random.random()
            r2 = random.random()
            social = c1 * r1 * (gBest[i] - self.pos[i])
            cognitive = c2 * r2 * (self.pBest[i] - self.pos[i])
            self.velocity[i] = (w * self.velocity[i]) + social + cognitive
        return
 
    def satisfyConstraints(self):
        #This is where constraints are satisfied
        return
 
# This class contains the particle swarm optimization algorithm
class ParticleSwarmOptimizer:
    output = []
    swarm = []
 
    def __init__(self):
        for h in range(swarmSize):
            particle = Particle()
            self.swarm.append(particle)
        return
 
    def optimize(self):
        firstTime = 0
        output = []
        
        for i in range(iterations):
            #print "iteration ", i
            
            #Get the global best particle
            gBest = copy.deepcopy(self.swarm[0].pBest)
            if (firstTime == 0):
                output = copy.deepcopy(gBest)
                firstTime = 1
            
            for j in range(swarmSize):
                pBest = self.swarm[j].pBest
                if self.f(pBest) < self.f(gBest):
                    gBest = pBest

            if (self.f(gBest) < self.f(output)):
                output = copy.deepcopy(gBest)
                
                print "better " , i , " = " , self.f(output)
                #print ("data " + str(output[0]) + " , " + str(output[1]))
            
            #Update position of each paricle
            for k in range(swarmSize):
                self.swarm[k].updateVelocities(gBest)
                self.swarm[k].updatePositions()
                self.swarm[k].satisfyConstraints()
                
            #Update the personal best positions
            for l in range(swarmSize):
                pBest = self.swarm[l].pBest
                if self.f(self.swarm[l].pos) < self.f(pBest):
                    self.swarm[l].pBest = self.swarm[l].pos

        return output


    def f(self, solution):
        #This is where the metaheuristic is defined
        sum = 0
        for i in range(dimension):
            sum = sum + solution[i]
        #return  random.random()

        g = (3*(solution[0]*solution[0])) - (2*(solution[1])) + 7
                                             
        return abs(0- abs(g))
    
def main():
    pso = ParticleSwarmOptimizer()
    pso.optimize()
 
if  __name__ =='__main__':
    main()
