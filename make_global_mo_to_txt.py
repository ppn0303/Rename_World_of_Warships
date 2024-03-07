import os
import sys
import polib
import glob
import time

path = os.path.dirname(os.path.realpath(__file__))+"/"

try : 
    # load mo file
    mo_file = polib.mofile(path+'global.mo')
except : 
    print('you need to place global.mo this folder')
    time.sleep(10)
    sys.exit()

print('extract is start')
# extract global.mo to txt file
with open('global_mo.txt', "w") as file:
    for num, line in enumerate(mo_file):
        result = line
        file.write(str(num)+' '+line.msgid+' '+line.msgstr+"\n")
file.close()
print('work End, this window will be close after 10 second')
time.sleep(10)
sys.exit()