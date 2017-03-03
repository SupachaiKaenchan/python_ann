# dewtx29@gmail.com
# md5
import os
import os.path
import copy
import re

def vmtouchResort(filePath):
    f = open(filePath, "r")
    output = open("/ram2/vm.sh" , "w")

    ## use readlines to read all lines in the file
    ## The variable "lines" is a list containing all lines
    lines = f.readlines()


    ## close the file after reading the lines.
    f.close()

    print (str(len(lines)))

    listVM = []
    listAllFile = []


    xFileName = ""
    xScore = 0
        
    for tmp1 in range (0,len(lines)):
        #print str(tmp1 %  3)
    

        xValue = []
        
        if (tmp1 % 4 == 0):
            xFileName = (lines[tmp1])
            listAllFile.append(xFileName)
            #print xFileName
        if (tmp1 % 4 == 2):
            xScore = (lines[tmp1].split()[1])
            xValue = xScore.split("/")
        
            #print xValue[0]
            #print xValue[1]
            if (len(xValue) == 2):
                if (xValue[0] == xValue[1]):
                    #print xFileName
                    #print xScore
                    listVM.append(xFileName)
            

    print (str(len(listVM)) + "/" + str(len(listAllFile)))

    writePls = []

    tmpRemain = set(listAllFile) -  set(listVM)
    print str(len(tmpRemain))
    
    writePls = listVM + list(set(tmpRemain))
    
    print(str(len(writePls)))

    for tmp in writePls:
        output.write(str(tmp) )
    
    output.close();
    f.close();
   



    #f = open('/ram2/g_pat.txt', "r")
    #f = open('/ram2/one_pat.txt', "r")
    #f = open('/ram2/one_dew.txt', "r")
    #f = open('/ram2/one_dd.txt', "r")
    #f = open('/ram2/g_pat_photo.txt', "r")
#checkNonUnicode("/ram2/g_dd.txt")
vmtouchResort("/ram2/tmpvmtouch.txt")


