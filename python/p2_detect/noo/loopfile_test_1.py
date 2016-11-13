import os, sys

path = "./jpg"
dirs = os.listdir(path)
#print dirs

fou = 0

for file in dirs:
    str1 = file;
    str2 = ".txt";

    fou = str1.find(str2);

    if (fou > -1):
        print file

#<type 'str'>