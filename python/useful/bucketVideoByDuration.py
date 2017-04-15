# dewtx29@gmail.com
# Program Move file script maker (100 files for 1 folder)

import os
import os.path

lst = [];

count = 0

sourcePath = "/d/d/videos/be/timelapse/timelapse/1/2"
desPath = "/d/d/videos/be/timelapse/timelapse/1/dura"


txt = open ("/ram/1.txt","r")
lines = txt.readlines()
txt.close()

print str(len(lines))

maxDura = 60*60
tmpDura = 0

tmpGroup = 1

txt = open ("/ram/2.sh","w")

listInGroup = []

for tmp in lines:

    ss = tmp.split(' ')
    #print ss
    #print ss[1].replace("\n","")

    dura = float(ss[1].replace("\n",""))
    tmpDura = tmpDura + dura


    if (tmpDura > maxDura):
        print tmpDura
        tmpDura = 0


        fName = str(tmpGroup) + "_list.txt"
        saveL = open ("/ram/tmp/" + fName,"w")

        print ("listInGroup " + str(len(listInGroup)))
        for gg in listInGroup:
            saveL.write("file '" + gg + "'\n")
            
        saveL.close()




        saveL2 = open ("/ram/tmp/" + str(tmpGroup) + "_bash.sh","w")
        saveL2.write("ffmpeg -f concat -i " + fName + " -c copy /ram/tmp/" + str(listInGroup[0]) )
        
        saveL2.close()
        
        tmpGroup = tmpGroup + 1
        listInGroup = []

    listInGroup.append(ss[0])
    

    txt.write ("mkdir " + desPath + "/" + str(tmpGroup) +"\n")
    txt.write ("mv " + sourcePath + "/" + ss[0] + " " + desPath + "/" + str(tmpGroup) + "/"  + ss[0] + "\n")



#txt.write(e + "\n")

txt.close()

print "done"
