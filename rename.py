import os
import sys
import polib
import glob
import time
import pandas as pd

path = os.path.dirname(os.path.realpath(__file__))+"/"

try : 
    # load mo file
    mo_file = polib.mofile(path+'global.mo')
except : 
    print('you need to place global.mo this folder')
    time.sleep(10)
    sys.exit()

try : 
    # load name_list
    names = pd.read_csv(path+'name_list.csv')
except : 
    print('you need to place name_list.csv this folder')
    time.sleep(10)
    sys.exit()

count = 0
print('change name start')
for num, line in enumerate(mo_file):
    if (line.msgid==names.msgid).any():
        list_number = np.where(line.msgid==names.msgid)[0][0]
        print(f'{line.msgstr} -> {names.msgstr_new[list_number]}')
        line.msgstr = names.msgstr_new[list_number]
        count += 1

print(f'change name list : {len(names)}, changed list : {count}')

# save global.mo.
# I recommand other name because sometime we lost original data
mo_file.save(path+'global_changed.mo')
print('work End, this window will be close after 10 second')
time.sleep(10)
sys.exit()