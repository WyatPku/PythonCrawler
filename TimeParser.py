#-*- coding:utf-8 -*-
import re

def parse(s):
    p=r'(\d+~\d+周)|(每周)|(单周)|(双周)|(?P<compound>周[一二三四五六七日天1234567]\d+~\d+节)|(周[一二三四五六七日天1234567])|(\d+~\d+节)'
    p2=re.compile(r'(周[一二三四五六七日天1234567])|(\d+~\d+节)')
    it=re.finditer(p,s)
    ans=[]
    for g in it:
        ans.append(g.group(0))
        for gg in p2.finditer(g.group(0)):
            if (gg.group(0)!=g.group(0)):
                ans.append(gg.group(0))
        #print(g.group(0))
    t=re.sub(p,' ',s)
    #print(t)
    #print(ans)
    return (ans,t.split())

if __name__=="__main__":
    s=input()
    print(parse(s))
