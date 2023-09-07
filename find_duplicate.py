import re
import copy
import pprint
import os
import json
import argparse

def parser_bib(file):
    f = open(file, "r",encoding='UTF-8')

    item={}
    key='error'
    types={}
    for line in f:
        if line.startswith('%'):
            continue
        if line.strip()=='':
            continue
        rmatch = re.match(r"\s*\@(\w+)\{(.+),", line)
        if rmatch:
            type=rmatch.group(1)
            key=rmatch.group(2)
            if key in item:
                key+='_same'
            item[key]=[line]
            types[key]=type
        else:
            item[key].append(line)

    infos={}
    for k,v in item.items():
        infos[k]={'type':types[k],'source':v}
        for line in v:
            rmatch=re.match(r"\s*(\w+)\s*=\s*(.+)[,]*",line)
            if rmatch:
                nk=rmatch.group(1)
                nv=rmatch.group(2)
                nv=nv.strip('\{\},\t\n\r\f\v')
                infos[k][nk]=nv
        
    # print(infos)
    f.close()
    return infos


def find_duplicate(db):
    matches={}
    fakedb=copy.deepcopy(db)
    for k,idb in db.items():
        # print(idb)
        
        title=idb.get('title',None)
        new_title = re.sub(r"[^a-zA-Z0-9]","",title)
        if k in fakedb:
            _=fakedb.pop(k)
        for fk in list(fakedb.keys()):
            fidb=fakedb[fk]
            ftitle=fidb.get('title',None)
            new_ftitle=re.sub(r"[^a-zA-Z0-9]","",ftitle)
            # print(new_title)
            if new_ftitle.lower() == new_title.lower():
                if new_ftitle in matches:
                    new_ftitle+='_1'
                matches[new_ftitle]=(k,fk)
                fakedb.pop(fk)
                # break

    # pprint.pprint(matches)
    with open('duplicate.json','w') as f:
        json.dump(matches,f)

    # write new bib
    if os.path.exists('new.bib'):
        os.remove('new.bib')
    f=open('new.bib','a',encoding='UTF-8')

    dname=[dv[1] for _,dv in matches.items()]
    for k,idb in db.items():
            if k in dname:
                continue
            if k.endswith('_same'):
                print(idb)
                continue
            f.writelines(idb['source'])
            f.write('\n')
    f.close()  
    return matches
        
                
        

if __name__=='__main__':
    aug=argparse.ArgumentParser()
    aug.add_argument('--path',type=str,help='path to parser')

    opt=aug.parse_args()
    db=parser_bib(opt.path)
    find_duplicate(db)
