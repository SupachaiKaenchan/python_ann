# dewtx29@gmail.com
# md5
import os
import os.path
import copy
import re

def special_match(strg, search=re.compile(r'[^a-z0-9.]').search):
    return not bool(search(strg))

def be2column(pureString): 
    words = []

    for b in pureString:
        if (b != ""):
            words.append(b)
            
        if (len(words) > 3):
            #print "..."
            #print words
            
            newname = ""
            for c in range (1,len(words)):
                #print c
                newname = newname + words[c]
                
                if (c < len(words)-1):
                    newname = newname + " "
                
            #print pureString
            #print newname
            #print words

            word2 = []
            word2.append(words[0])
            word2.append(newname)
            #print "after !@#"

            
            #print word2
            return word2
        
            #words = copy.copy(word2)

    return words

def columnTo2Column(pureColumn):
    ret = []

    for a in pureColumn:
        tmp1 = a.split(" ");

        
        words = be2column(tmp1)
        
        ret.append(words)

    return ret

def isMD5Seem (md5C , slotC , md5L):
    ret = False

    tmpM = md5C[slotC][0]
    
    for j in range(0,len(md5L)):
        tmpM2 = md5L[j][0]

        if (tmpM == tmpM2):
            ret = True
            #print ("seem " + tmpM)

    return ret

def diffOfMD5(cloudPath , localPath):
    fcloud = open(cloudPath, "r")
    flocal = open(localPath, "r")

    wNotSeem = open("/ram2/notSeem.sh" , "w")

    linesC = fcloud.readlines()
    linesL = flocal.readlines()

    print linesC[0]
    print linesL[0]

    md5C = columnTo2Column(linesC)
    md5L = columnTo2Column(linesL)

    print md5C[1]

    seemCount = 0;
    notSeemCount = 0;
    for i in range(0, len(md5C)):
        if (i > 1000 ):
            break
        
        tmpSeem = isMD5Seem(md5C , i , md5L)
        if (tmpSeem == True):
            seemCount = seemCount + 1
        else:
            notSeemCount = notSeemCount + 1
            wNotSeem.write(md5C[i][0] + " " + md5C[i][1] + "\n")
        #print tmpM


    print str(seemCount) + " / " + str(notSeemCount)
    
    
    print (str(len(md5C)) + " / " + str(len(md5L)))

    print (str(len(linesC)) + " / " + str(len(linesL)))

    flocal.close()
    fcloud.close()
    wNotSeem.close()


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


#checkNonUnicode("/ram2/g_dd.txt")
#renameSpaceToUnderscore("/ram2/one_dew.txt")
    
diffOfMD5("/ram2/x.txt" , "/ram2/local.txt")
          
          

