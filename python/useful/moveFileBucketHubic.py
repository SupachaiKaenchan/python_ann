# dewtx29@gmail.com
# Program Move file script maker (100 files for 1 folder)

import os
import os.path

lst = [];

count = 0

sourcePath = "/home/d/Cloudxx/hubic/Dem_File/dem_y"
desPath = "/home/d/Cloudxx/hubic/Dem_File/dem_x"

maxSize = 100 #max file for 1 folder

for dirpath, dirnames, filenames in os.walk(sourcePath):
    for filename in [f for f in filenames if f.endswith(".zip")]:
        count = count + 1;
        lst.append(os.path.join(dirpath, filename))
        #print os.path.join(dirpath, filename);
        #print count;


print count

lst = sorted(lst, key=str.lower)

print len(lst)



counter = 100
folderNumber = 0

txt = open ("/home/d/1.sh","w")



curPath = ""

print "start"

for i in range(0,count):
    counter = counter + 1
    
    if (counter >= 100):
        counter = 0
        folderNumber = folderNumber + 1
        curPath = desPath + "/" + str(folderNumber)
        txt.write("mkdir " + curPath + "\n")
    
        
    a = lst[i]
   # print i
   # print a
    
    b = a.replace(".dem.zip" , ".zip")
   # print b

    c = b.rfind("/" )

    d = b[c+1:len(b)]
   # print c
   # print d

   
    e = "mv '" + a + "' '" + curPath + "/" + d + "'"
    #e = "mv '" + a + "' '" +  "" + d + "'"
    #print e
    txt.write(e + "\n")

txt.close()

print "done"
