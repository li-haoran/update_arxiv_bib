import re
import copy
import pprint
import os
import json
import argparse
from collections import defaultdict
import jieba
import jieba.posseg as posseg
from ltp import LTP
DEFAULT='ltp'
if DEFAULT=='ltp':
    ltp = LTP("LTP/base") 

def is_chinese(string):
    """
    Check if a string contains Chinese characters
    """
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    return bool(pattern.search(string))
def is_none_chinese(string):
    """
    Check if a string contains Chinese characters
    """
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    return bool(pattern.search(string))

def replace_de_di(file):
    f = open(file, "r",encoding='UTF-8')
    verbs=defaultdict(int)
    newfiles=[]
    # jieba.enable_paddle() 
    for line in f:  
        new_linew=line
        # print(line)
        if line.strip().startswith('%') or line.strip()=='':
            newfiles.append(new_linew)
            continue
        # print(line)
        if DEFAULT=='jieba':
            results=posseg.lcut(line)#,use_paddle=True)
            dep={}
        elif DEFAULT=='ltp': 
            # print(line)
            cws,pos,dep= ltp.pipeline([line], tasks=['cws','pos','dep']).to_tuple()
            dep=dep[0]
            results=list(zip(cws[0],pos[0]))
            # print(results,len(results),dep)
            # break
        else:
            print('error')

        # print(results)
        for ik,wf in enumerate(results):
            word,flag=wf

            if flag != 'v':
                continue  
            if is_none_chinese(word):
                continue
            if len(dep)==0:
                continue
            head=dep['head']
            label=dep['label']
            true_verb=False
            for index,ih in enumerate(head):
                if ih==ik+1:
                    if label[index]=='ADV':
                        true_verb=True
                        break
            if not true_verb: 
                continue
            # print(word)
            verbs[word]+=1
            keep='地'+word
            abort='的'+word
            new_linew = re.sub(abort,keep,new_linew)
            # print(keep,abort,new_linew)
        newfiles.append(new_linew)
        
    f.close()
    nf = open('new_'+file, "w",encoding='UTF-8')
    nf.writelines(newfiles)
    nf.close()

    with open('verbs.json','a',encoding='UTF-8') as f:
        json.dump({'file':verbs},f, ensure_ascii=False)
 

if __name__=='__main__':
    aug=argparse.ArgumentParser()
    aug.add_argument('--files',type=str,nargs='+',help='tex file to replace')

    opt=aug.parse_args()
    for file in opt.files:
        replace_de_di(file)

