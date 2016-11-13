import numpy as np

#f = file("tmp.bin","wb")
#np.save(f,a)
#np.save(f,b)
#np.save(f,c)
#f.close()

#f = file("tmp.bin","rb")
#aa = np.load(f)
#bb = np.load(f)
#cc = np.load(f)
#f.close()

def dew_write_weight_file(str,pattern):
    f = file(str,"wb")
    np.save(f,pattern)
    f.close()

def dew_read_weight_file(str):
    f = file(str,"rb")
    aa = np.load(f)
    f.close()
    return aa
