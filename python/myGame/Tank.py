class Tank:


    def __init__(self, x,y):
        self.x = x
        self.y = y


    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y
    
    def setXY(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


g = Tank
g.setX(10)

print g.getX()
