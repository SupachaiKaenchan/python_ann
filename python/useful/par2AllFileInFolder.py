# dewtx29@gmail.com
# Program Move file script maker (100 files for 1 folder)

import os
import os.path

lst = [];

count = 0

sourcePath = "/ram2/2"
desPath = "/ram2/3"


for dirpath, dirnames, filenames in os.walk(sourcePath):
    for filename in [f for f in filenames]:
        count = count + 1;
        lst.append(os.path.join(dirpath, filename))
        #print os.path.join(dirpath, filename);
        #print count;


print count

lst = sorted(lst, key=str.lower)

print len(lst)


txt = open ("/home/d/2.sh","w")



curPath = ""

print "start"

for i in range(0,count):
 
    a = lst[i]
   # print i
   # print a
    

   # print b

   # print c
   # print d

   
    e = "par2 c '" + a + "'"
    #e = "mv '" + a + "'
    #print e
    txt.write(e + "\n")

txt.close()

print "done"
