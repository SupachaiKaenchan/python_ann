import os
for fn in os.listdir('./jpg'):
     if os.path.isfile(fn):
        print fn