import dblp
import re
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
        rmatch = re.match(r"\@(\w+)\{(.+),", line)
        if rmatch:
            type=rmatch.group(1)
            key=rmatch.group(2)
            item[key]=[]
            types[key]=type
        else:
            item[key].append(line)

    infos={}
    for k,v in item.items():
        infos[k]={'type':types[k],}
        for line in v:
            rmatch=re.match(r"\s*(\w+)\s*=\s*(.+)[,]*",line)
            if rmatch:
                nk=rmatch.group(1)
                nv=rmatch.group(2)
                nv=nv.strip(',\t\n\r\f\v')
                infos[k][nk]=nv
        
    # print(infos)
    return infos

def write_bib(file,key,items):
    f = open(file, "a+",encoding='UTF-8')

    type=items.pop('type')

    source=items.pop('matches',None)
    strings='\n'
    strings+='@'+f'{type}'+'{'+f'{key},\n'
    for k,v in items.items():
        strings+=f'{k} = {v},\n'
    strings+='}\n'
    strings+='>'*20+'\n'
    for s in source:
        strings+=s['source']

    strings+='\n'
    f.write(strings)
    f.close()

def update_arxiv(db,out_file):
    
    for k,idb in db.items():
        # print(idb)
        journal=idb.get('journal',None)
        publisher=idb.get('publisher',None)
        download=True
        # if journal is not None and  journal.lower().find('arxiv')>-1:
        #     # print(journal)
        #     download=True
        # if publisher is not None and publisher.lower().find('arxiv')>-1:
        #     # print(publisher)
        #     download=True

        if download:
            title=idb.get('title',None)
            # print(title)
            if title is not None:
                ntitle=title.replace('\{','').replace('\}','')
                matchlist = dblp.searchP(ntitle)
                final_list=[]
                for im in matchlist:
                    ftitle=im.get('title',None)
                    new_title=re.sub(r"[^a-zA-Z0-9]","",title)
                    new_ftitle=re.sub(r"[^a-zA-Z0-9]","",ftitle)
                    # print(new_ftitle,new_title,im)
                    if new_title.lower() == new_ftitle.lower():
                        final_list.append(im)
                        break
                idb.update({'matches': final_list})

                write_bib(out_file,k,idb)
                
        

if __name__=='__main__':
    aug=argparse.ArgumentParser()
    aug.add_argument('--path',type=str,help='path to parser')
    aug.add_argument('--out',type=str,help='path to save')

    opt=aug.parse_args()
    db=parser_bib(opt.path)
    update_arxiv(db,opt.out)
