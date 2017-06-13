import random

def lagrangSub (inputList , x , index):
    # [xi , yi]
        
    r1 = inputList[index][1]
    r2 = 1

    for i in range( 0, len(inputList) ):
                
        if (i == index):
            continue
        else:
            r2 = r2 * ((x-i)/(r1-i))


    r3 = r2 * r1
        
    return r3

def lagrang (inputList , x ):
    r1 = 0

    for i in range(0,len(inputList)):
        r1 = r1 + lagrangSub(inputList, x , i)
            
    return r1

        
def func(x):
    #j =  + (0.5*pow(x, 3)) - (4*pow(x,2)) + (pow(x,1)) - 1
    j =  + (2*pow(x, 3)) - (3*pow(x,2)) + (0.2*pow(x,1)) - 1
           
    return j

        

def randomInput(amountOfData):
    tmpData = []

    for i in range(amountOfData):
        x = i
        y = (random.random()*10.0)-5.0

        list = [x,y]
        tmpData.append(list)

    return tmpData


tData = randomInput(5)
print tData

testX = 0.0
while (testX < 5.0):
    
    y = lagrang(tData, testX)

    print testX , " = " ,  y
    testX = testX + 0.1
