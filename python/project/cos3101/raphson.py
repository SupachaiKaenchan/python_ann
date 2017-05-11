def f(x):
    a = pow(x,3)+ (3*(pow(x,2)) * x ) -  10
    return a

def df(x):
    b = (3*pow(x,2))+(6*x)+1;
    return b

flag = 1
inx = 0
x0 = 6.0
print("inx","          ","x1","                ","f(x1)")
while flag:
    inx=inx+1
    x1 = x0-(f(x0)/df(x0))
    if abs(f(x1)) <= 0.0000000001:
        print("found root.")
        flag = 0
    else:
        x0=x1
    print(inx,"   ",x1,"    ",f(x1))
    
print("Root if equation is: ",x1 , " f(x1) = " , f(x1))
print("Iterative all: ",inx)

    #print(inx)

    #print(index+"   "+ x1 +"    "+f(x1))
#print("root if equation is "+ x1)
#print("Iterative all "+inx)
