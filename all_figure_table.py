import re
import copy
import pprint
import os
import json
import argparse

def figures(file):
    f = open(file, "r",encoding='UTF-8')
    figures=[]
    tables=[]
    for line in f:
        rmatch = re.findall(r'\\includegraphics\[.*\]\{(.*?)\}',line)
        if len(rmatch):
            figures+=rmatch
    print(figures)

if __name__=='__main__':
    aug=argparse.ArgumentParser()
    aug.add_argument('--files',type=str,nargs='+',help='tex file to replace')
    opt=aug.parse_args()
    for file in opt.files:
        figures(file)

