import os.path
import sys

keywords = {"reading","comprehension","digital","strategies","ability"}
filename = input("Please input the file name:").strip()
if not os.path.isfile(filename):
    print("%filename檔案不存在"%(filename))
    sys.exit()
pfile = open(filename,"r")
ptext = pfile.read().split()
for keyword in keywords:
    pcount = 0
    for word in ptext:
        if keyword in word:
            pcount +=1
    print("The keyword %s appear %d times"%(keyword, pcount)) 