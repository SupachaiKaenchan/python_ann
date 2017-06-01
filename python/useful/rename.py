# dewtx29@gmail.com
# ffmpeg dem

import os
import os.path

lst = [];

count = 0

sourcePath = "/d/d/fean/fern/fearn3"  #"/raid0/dem_year"
desPath = "/d/d/fean/fern/fearn4"

lst2 = []

for dirpath, dirnames, filenames in os.walk(sourcePath):
    for filename in [f for f in filenames]:
        count = count + 1;

        tmpa = os.path.join(dirpath, filename)
        tmpc = tmpa.rfind("/" )
        tmpb = tmpa[tmpc+1:len(tmpa)]

        tmpName = tmpb[0:tmpb.find(".")]
        
        
        lst2.append(tmpb)
        lst.append(tmpName + ".jpg")
        #print os.path.join(dirpath, filename);
        #print count;


print count

lst = sorted(lst, key=str.lower)

print len(lst)


txt = open ("/ram/1.sh","w")



curPath = ""

print "start"

for folderloop in range (0,1):
    #txt.write("cd " + desPath + str(folderloop) + "\n")
    
    for i in range(0,count):
     
        a = lst[i]
       # print i
       # print a
        

       # print b

       # print c
       # print d

        #ffmpeg -framerate 60 -i g1_%5d.bmp -c:v libx264 ~/g1.mp4
       
        #e = "ffmpeg -framerate 60 -i " + a + "_%5d.bmp -c:v libx264 /raid0/"+ a + ".mp4"
        
        
        #e = "mv '" + a + "'
        #print e
        #txt.write(e + "\n")

        txt.write("cp '" + lst2[i] + "' '/d/d/fean/fern/fearn4/" + a + "'\n")

txt.close()

print "done"
