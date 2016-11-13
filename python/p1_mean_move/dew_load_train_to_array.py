
#load training file to array
def dew_load_train_file(fname):
    #fname = './txt/training.txt'

    with open(fname) as f:
        content = f.read().splitlines()

    #print content

    t1 = []
    t2 = []
    t3 = []
    t4 = []

    for i1 in range(0,len(content)):
        if content[i1] == '[new]':
            #print "..."
            t1 = []
            t2 = []

            for i2 in range(i1+1,i1+68):
                t1.append(float(content[i2]))
                #print "t1 " + content[i2] + ", %d" %(len(t1))

              #for i2 in range(i1+68,i1+71):

            for i2 in range(i1+68,i1+71):
                t2.append(float(content[i2]))
                #print "t2 " + content[i2] + ", %d" %(len(t2))

            t3 = (t1, t2)
            t4.append(t3)

    return t4
    #for i in range(1,4):