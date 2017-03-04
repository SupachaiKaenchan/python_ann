# dewtx29@gmail.com
# md5
import os
import os.path
import copy
import re
from random import randint
import pickle

import threading
from multiprocessing import cpu_count


def readFileMD5Sha1Style(filePath):
    tmp = open(filePath,"r")

    lines = tmp.readlines()
    beColumn = columnTo2Column(lines)
    
    tmp.close()

    return beColumn




def compare2File(big_list , small_list):
    
    wUpload = open("/ram2/compare2File.sh" , "w")

    big = readFileMD5Sha1Style(big_list)

    small = readFileMD5Sha1Style(small_list)


    

    print (str(len(big)) + " / " + str(len(small)) )

    # loop everything in small list


    # concat with sha1 column

    thirdColumn = []

    readMode3 = True

    if (readMode3 == True):

        
        for a in range (0, len(small)):
            # loop md5

            if (a % 100 == 0):
                print str(a) + " / " + str(len(small))

            tmpMD5 = small[a][0]

            for b in range(0,len(big)):
                tmpMD52 = big[b][0]
            
                
                if (tmpMD5 == tmpMD52):
                    #print big[b]
                    thirdColumn.append(big[b][1])



        print str(len(thirdColumn))

    mode = 2
    if (mode == 1):
        for b in range (0, len(thirdColumn)):
            xxx = thirdColumn[b].replace("\n","")
            wUpload.write("mv '/d/d/another2/g/randomized/" + xxx + "' '/d/d/another2/g/why/" + xxx + "'\n" )
    elif (mode == 2):
        for b in range (0, len(thirdColumn)):
            xxx = thirdColumn[b].replace("\n","")
            wUpload.write("./rclone copy 'google_tx:pc/" + xxx + "' '/d/d/xx/" + xxx + "'\n" )
    wUpload.close()

class threadComparing (threading.Thread):
    def __init__(self, threadID, name, thirdColumn , google_pat , google_dd,
                 one_pat, one_dew , one_dd):

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.thirdColumn = thirdColumn
        self.google_pat = google_pat
        self.google_dd = google_dd
        self.one_pat = one_pat
        self.one_dew = one_dew
        self.one_dd = one_dd

        self.ret = None
        print str(len(self.thirdColumn))

    def run(self):

        nmd5 = []
        
        for a in range (0,len(self.thirdColumn)):
            if (a % 100 == 0):
                print(str(self.threadID) + " /// " +  str( a) + " % " + (str( a * 100 / (len(self.thirdColumn)))))
            
            t1 = self.thirdColumn[a][0]
            tsha = self.thirdColumn[a][2]

            isFound = False
            
            #check them on the list
            for b in range(0,len(self.google_pat)):
                t2 = self.google_pat[b][0]

                #print (t1 + " / " + t2)
                
                if (t2 == t1):
                    isFound = True
                    break

            if (isFound == True):
                continue
            
            #check them on the list
            for b in range(0,len(self.google_dd)):
                t2 = self.google_dd[b][0]

                #print (t1 + " / " + t2)
                
                if (t2 == t1):
                    isFound = True
                    break

            if (isFound == True):
                continue


            #check them on the list
            for b in range(0,len(self.one_pat)):
                t2 = self.one_pat[b][0]

                #print (t1 + " / " + t2)
                
                if (t2 == tsha):
                    isFound = True
                    break

            if (isFound == True):
                continue


            #check them on the list
            for b in range(0,len(self.one_dew)):
                t2 = self.one_dew[b][0]

                #print (t1 + " / " + t2)
                
                if (t2 == tsha):
                    isFound = True
                    break

            if (isFound == True):
                continue

            #check them on the list
            for b in range(0,len(self.one_dd)):
                t2 = self.one_dd[b][0]

                #print (t1 + " / " + t2)
                
                if (t2 == tsha):
                    isFound = True
                    break

            if (isFound == True):
                continue
            
                
            nmd5.append(self.thirdColumn[a])

        self.ret = nmd5
        #return nmd5
    
    def join(self):
        threading.Thread.join(self)
        return self.ret

        
def uploadOnlyNotOnCloud_thread(local_md5, local_sha1):
    
    wUpload = open("/ram2/uploadOnlyNotOnCloud.sh" , "w")

    md5 = readFileMD5Sha1Style(local_md5)

    sha1 = readFileMD5Sha1Style(local_sha1)

    one_pat = readFileMD5Sha1Style("/ram2/one_pat_sha1.txt")
    one_dew = readFileMD5Sha1Style("/ram2/one_dew_sha1.txt")
    one_dd = readFileMD5Sha1Style("/ram2/one_dd_sha1.txt")
    google_pat = readFileMD5Sha1Style("/ram2/google_pat_md5.txt")
    google_dd = readFileMD5Sha1Style("/ram2/google_dd_md5.txt")
    

    print (str(len(md5)) + " / " + str(len(sha1)) )

    print (str(len(one_pat)))
    print (str(len(one_dew)))
    print (str(len(one_dd)))
    print (str(len(google_pat)))
    print (str(len(google_dd)))


    # concat with sha1 column

    thirdColumn = []

    readMode3 = False

    if (readMode3 == True):
        for a in range (0, len(md5)):
            if (a % 100 == 0):
                print( str( a) + " % " + (str( a * 100 / (len(md5)))))
            # loop all file name

            tmpFileName = md5[a][1]

            for b in range(0,len(sha1)):
                tmpFileName2 = sha1[b][1]

                if (tmpFileName == tmpFileName2):
                    tmpG = []
                    tmpG.append(md5[a][0])
                    tmpG.append(md5[a][1])
                    tmpG.append(sha1[b][0])
                    thirdColumn.append(tmpG)
                    #print thirdColumn[0]




        with open("/ram2/thirdColumn.txt", 'wb') as fp:
            pickle.dump(thirdColumn, fp)

        fp.close()
        
    else:
        with open ("/ram2/thirdColumn.txt", 'rb') as fp:
            thirdColumn = pickle.load(fp)
        print str(len(thirdColumn))
        print thirdColumn[0]


    #*******************************
    # compare them which file are not in Cloud

    compareMode = True

    nmd5 = []
    
    if (compareMode == True):

        print str(len(thirdColumn))

        increStep = len(thirdColumn)/4
        increCur = 0
        increMax = increCur + increStep

        print ">>>>>>>>>>>>"

        #threadLock = threading.Lock()
        threads = []
        threadsPre= []

        slotCount = 0
        while (increCur < len(thirdColumn)):
            print str(increCur) + " / " + str(increMax) + " / " + str(len(thirdColumn))
            
            
            if (increMax >= len(thirdColumn)):
                increMax = len(thirdColumn)

                
                
            subThird = []
            
            for i in range (increCur, increMax):
                subThird.append(thirdColumn[i])

            increCur = increCur + increStep
            increMax = increMax + increStep

            
            
            print str(len(subThird))
            slotCount = slotCount  + 1

            threadX = threadComparing(slotCount , str(increMax), subThird,  google_pat , google_dd,
                 one_pat, one_dew , one_dd)
            threadsPre.append(threadX)

        counter = 0
        print "threadsPre .size " + str(len(threadsPre))

        print "thread core com : " + str(cpu_count())
 
        
        
        for threadX in threadsPre:
            counter = counter + 1
            print "running " + str(counter)
            threadX.start()
            threads.append(threadX)

        out = []
        for t in threads:
            gx = t.join()
            out.append(gx)
            print "ret ret " + str(t.threadID)
            #print gx

        with open("/ram2/thirdColumnNotInCloud.txt", 'wb') as fp:
            pickle.dump(nmd5, fp)
        fp.close()
            
    else:
        with open ("/ram2/thirdColumnNotInCloud.txt", 'rb') as fp:
            nmd5 = pickle.load(fp)

        for a in range(0, len(nmd5)):

            xxx = nmd5[a][1].replace("\n","")
            wUpload.write("ln -s '/d/d/another2/g/randomized/" +   xxx + "' '/d/d/another2/o/" + xxx + "'\n")
            

    print ("n md5 " + str(len(nmd5)))

    
        

    wUpload.close()   
    
def uploadOnlyNotOnCloud(local_md5, local_sha1):
    
    wUpload = open("/ram2/uploadOnlyNotOnCloud.sh" , "w")

    md5 = readFileMD5Sha1Style(local_md5)

    sha1 = readFileMD5Sha1Style(local_sha1)

    one_pat = readFileMD5Sha1Style("/ram2/one_pat_sha1.txt")
    one_dew = readFileMD5Sha1Style("/ram2/one_dew_sha1.txt")
    one_dd = readFileMD5Sha1Style("/ram2/one_dd_sha1.txt")
    google_pat = readFileMD5Sha1Style("/ram2/google_pat_md5.txt")
    google_dd = readFileMD5Sha1Style("/ram2/google_dd_md5.txt")
    

    print (str(len(md5)) + " / " + str(len(sha1)) )

    print (str(len(one_pat)))
    print (str(len(one_dew)))
    print (str(len(one_dd)))
    print (str(len(google_pat)))
    print (str(len(google_dd)))


    # concat with sha1 column

    thirdColumn = []

    readMode3 = True

    if (readMode3 == True):
        for a in range (0, len(md5)):
            if (a % 100 == 0):
                print( str( a) + " % " + (str( a * 100 / (len(md5)))))
            # loop all file name

            tmpFileName = md5[a][1]

            for b in range(0,len(sha1)):
                tmpFileName2 = sha1[b][1]

                if (tmpFileName == tmpFileName2):
                    tmpG = []
                    tmpG.append(md5[a][0])
                    tmpG.append(md5[a][1])
                    tmpG.append(sha1[b][0])
                    thirdColumn.append(tmpG)
                    #print thirdColumn[0]


        print str(len(thirdColumn))


        with open("/ram2/thirdColumn.txt", 'wb') as fp:
            pickle.dump(thirdColumn, fp)

        fp.close()
        
    else:
        with open ("/ram2/thirdColumn.txt", 'rb') as fp:
            thirdColumn = pickle.load(fp)
        print str(len(thirdColumn))
        print thirdColumn[0]


    #*******************************
    # compare them which file are not in Cloud

    compareMode = True

    nmd5 = []
    
    if (compareMode == True):

        for a in range (0,len(thirdColumn)):
            if (a % 100 == 0):
                print( str( a) + " % " + (str( a * 100 / (len(thirdColumn)))))
            
            t1 = thirdColumn[a][0]
            tsha = thirdColumn[a][2]

            isFound = False
            
            #check them on the list
            for b in range(0,len(google_pat)):
                t2 = google_pat[b][0]

                #print (t1 + " / " + t2)
                
                if (t2 == t1):
                    isFound = True
                    break

            if (isFound == True):
                continue
            
            #check them on the list
            for b in range(0,len(google_dd)):
                t2 = google_dd[b][0]

                #print (t1 + " / " + t2)
                
                if (t2 == t1):
                    isFound = True
                    break

            if (isFound == True):
                continue


            #check them on the list
            for b in range(0,len(one_pat)):
                t2 = one_pat[b][0]

                #print (t1 + " / " + t2)
                
                if (t2 == tsha):
                    isFound = True
                    break

            if (isFound == True):
                continue


            #check them on the list
            for b in range(0,len(one_dew)):
                t2 = one_dew[b][0]

                #print (t1 + " / " + t2)
                
                if (t2 == tsha):
                    isFound = True
                    break

            if (isFound == True):
                continue

            #check them on the list
            for b in range(0,len(one_dd)):
                t2 = one_dd[b][0]

                #print (t1 + " / " + t2)
                
                if (t2 == tsha):
                    isFound = True
                    break

            if (isFound == True):
                continue
            
                
            nmd5.append(thirdColumn[a])
            with open("/ram2/thirdColumnNotInCloud.txt", 'wb') as fp:
                pickle.dump(nmd5, fp)

            fp.close()
            
    else:
        with open ("/ram2/thirdColumnNotInCloud.txt", 'rb') as fp:
            nmd5 = pickle.load(fp)

        for a in range(0, len(nmd5)):

            xxx = nmd5[a][1].replace("\n","")
            wUpload.write("ln -s '/d/d/another2/g/randomized/" +   xxx + "' '/d/d/another2/o/" + xxx + "'\n")
            

    print ("n md5 " + str(len(nmd5)))

    
        

    wUpload.close()

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


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


def loadTheseFileToLocal(notSeemPath):
    fcloud = open(notSeemPath, "r")

    wNotSeem = open("/ram2/loadTheseFileToLocal.sh" , "w")

    linesC = fcloud.readlines()




    xyz = columnTo2Column(linesC)


    for i in range (0,len(linesC)):
        oriName = xyz[i][1].replace("\n" , " ")
        a = xyz[i]
        #print ">>>"
        #print a
        #print str(len(a))
        
        tmp = a[1].split(".")

        tmp2 = str(random_with_N_digits(6)) + "." + tmp[1]

        print oriName
        
        wNotSeem.write("./rclone copy 'google_pat:Google รูปภาพ/" + oriName + "' " + "/d/d/" + tmp2 )
        

    fcloud.close()
    wNotSeem.close()


def diffOfMD5(cloudPath , localPath):
    fcloud = open(cloudPath, "r")
    flocal = open(localPath, "r")

    wNotSeem = open("/ram2/notSeem.sh" , "w")
    wSeem = open("/ram2/Seem.sh" , "w")
    

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
        
        tmpSeem = isMD5Seem(md5C , i , md5L)
        if (tmpSeem == True):
            seemCount = seemCount + 1
            wSeem.write(md5C[i][0] + " " + md5C[i][1] + "\n" )
        else:
            notSeemCount = notSeemCount + 1
            wNotSeem.write(md5C[i][0] + " " + md5C[i][1] + "\n" )
        #print tmpM


    print str(seemCount) + " / " + str(notSeemCount)
    
    
    print (str(len(md5C)) + " / " + str(len(md5L)))

    print (str(len(linesC)) + " / " + str(len(linesL)))

    flocal.close()
    fcloud.close()
    wNotSeem.close()
    wSeem.close()


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
    
#diffOfMD5("/ram2/google_tx.txt" , "/ram2/local_md5.txt")
#loadTheseFileToLocal("/ram2/notSeem.sh")
uploadOnlyNotOnCloud_thread("/ram2/local_md5.txt" , "/ram2/local_sha1.txt")
#compare2File( "/ram2/local_md5.txt","/ram2/google_tx.txt" )
#compare2File( "/ram2/google_tx_uniq.txt","/ram2/notSeem.sh" )
                
                     
          
          

