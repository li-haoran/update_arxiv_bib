import re
import copy
import pprint
import os
import json
import argparse

def replace_cite_key(file,duplicates):
    f = open(file, "r",encoding='UTF-8')
    newfiles=[]
    for line in f:

        new_linew=line
        for k,v in duplicates.items():
            keep=v[0]
            abort=v[1]
            new_linew = re.sub(abort,keep,new_linew)
            # print(keep,abort,new_linew)
        newfiles.append(new_linew)
    f.close()
    nf = open('new_'+file, "w",encoding='UTF-8')
    nf.writelines(newfiles)
    nf.close()
 

if __name__=='__main__':
    aug=argparse.ArgumentParser()
    aug.add_argument('--duplicate',type=str,default='duplicate.json',help='duplicate file')
    aug.add_argument('--files',type=str,nargs='+',help='tex file to replace')

    opt=aug.parse_args()
    for file in opt.files:
        with open(opt.duplicate,'r') as f:
            duplicates=json.load(f)
            replace_cite_key(file,duplicates)

