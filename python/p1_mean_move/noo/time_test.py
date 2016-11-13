import time
lasta = 0.1
a = 0.2

#int(round(time.time()) * 1000)

for i in range(0,10000000):
    a = ((time.time() ) )
    if (lasta != a):
        #a  = time.time()
        lasta = a
        print a
