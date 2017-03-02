# dewtx29@gmail.com
# md5
import os
import os.path
import copy
import re

def special_match(strg, search=re.compile(r'[^a-z0-9.]').search):
    return not bool(search(strg))

def checkNonUnicode(filePath):
    f = open(filePath, "r")

    ## use readlines to read all lines in the file
    ## The variable "lines" is a list containing all lines
    lines = f.readlines()

    ## close the file after reading the lines.
    f.close()

    #print lines[0]

    tmp_ = copy.copy(lines)
    #tmp_[0] = "nope..."

    #print tmp_[0]
    #print lines[0]

    tmp_b = []

    maxArg = 0


    for a in tmp_:
        if (special_match(a) == True):
            print a        
        
        b = copy.copy(a)
        
        words = b.split()
        tmpArg = len(words)
        
        if (tmpArg > maxArg):
            maxArg = tmpArg

        if (tmpArg == 11):
            print a
            print str(words)
        
        #print len(words)
        #print words[0]

        tmp_rename = a.replace(" ", "_")
        tmp_b.append(tmp_rename)

    print maxArg    
    print tmp_b[0]

def renameSpaceToUnderscore(filePath):
    f = open(filePath, "r")
    output = open("/ram2/run3.sh" , "w")

    ## use readlines to read all lines in the file
    ## The variable "lines" is a list containing all lines
    lines = f.readlines()

    ## close the file after reading the lines.
    f.close()

    #print lines[0]

    tmp_ = copy.copy(lines)
    #tmp_[0] = "nope..."

    #print tmp_[0]
    #print lines[0]

    tmp_b = []

    maxArg = 0


    for a in tmp_:
        
        b = copy.copy(a)
        
        words = b.split()
        tmpArg = len(words)
        
        if (tmpArg > maxArg):
            maxArg = tmpArg

        if (tmpArg > 2):
            #print a
            newname = ""
            for c in range (1,len(words)):
                #print c
                newname = newname + words[c]
                
                if (c < len(words)-1):
                    newname = newname + " "

            #print newname
            after_ = newname.replace(" ","_")
            #print after_

            output.write("echo " + str(len(tmp_b)) + "\n")
            output.write( "./rclone copy 'one_dew:" + newname + "' 'one_dew:" + after_ + "' -v \n")
            output.write( "./rclone delete 'one_dew:" + newname + "' -v \n")
            
        
        #print len(words)
        #print words[0]

        tmp_rename = a.replace(" ", "_")
        tmp_b.append(tmp_rename)

    output.close();
    f.close();
    #print maxArg    
    #print tmp_b[0]



    #f = open('/ram2/g_pat.txt', "r")
    #f = open('/ram2/one_pat.txt', "r")
    #f = open('/ram2/one_dew.txt', "r")
    #f = open('/ram2/one_dd.txt', "r")
    #f = open('/ram2/g_pat_photo.txt', "r")
#checkNonUnicode("/ram2/g_dd.txt")
renameSpaceToUnderscore("/ram2/one_dew.txt")


