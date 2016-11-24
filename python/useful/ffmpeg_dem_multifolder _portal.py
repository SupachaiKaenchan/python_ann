# dewtx29@gmail.com
# ffmpeg dem

import os
import os.path

lst = [];

count = 0

sourcePath = "/home/dewtx29/Videos/dem_time"  #"/raid0/dem_year"
desPath = "/raid0/bmp"


for dirpath, dirnames, filenames in os.walk(sourcePath):
    for filename in [f for f in filenames]:
        count = count + 1;

        tmpa = os.path.join(dirpath, filename)
        tmpc = tmpa.rfind("/" )
        tmpb = tmpa[tmpc+1:len(tmpa)]
        tmpc = tmpb.replace(".dem","")
        
        lst.append(tmpc)
        #print os.path.join(dirpath, filename);
        #print count;


print count

lst = sorted(lst, key=str.lower)

print len(lst)


txt = open ("/raid0/3.sh","w")



curPath = ""

print "start"

for folderloop in range (1,10):
    txt.write("cd " + desPath + str(folderloop) + "\n")
    
    for i in range(0,count):
     
        a = lst[i]
       # print i
       # print a
        

       # print b

       # print c
       # print d

        #ffmpeg -framerate 60 -i g1_%5d.bmp -c:v libx264 ~/g1.mp4
       
        e = "ffmpeg -framerate 60 -i " + a + "%4d.tga -c:v libx264 /raid0/"+ a + ".mp4"
        
        
        #e = "mv '" + a + "'
        #print e
        txt.write(e + "\n")

        #txt.write("find . -name '" + a + "*' -delete\n")

txt.close()

print "done"
