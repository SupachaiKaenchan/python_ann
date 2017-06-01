class Tank:


    def __init__(self):
        self.x = 0
        self.y = 0


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


g = Tank()

print g
g.setX(10)


print g.getX()
