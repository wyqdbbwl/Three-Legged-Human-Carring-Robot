# encoding: utf-8
import urllib.request, re, time

def sv(c,fn):
    f=open(fn,'wb')
    f.write(c)
    f.close()

def op(fn):
    return open(fn,'r', encoding='utf-8')
    
def dl(u,p):
    fn=u.split('/')[-1]
    c=urllib.request.urlopen(u).read()
    sv(c,p+fn)

def gt(r,u):
    t=urllib.request.urlopen(u).read().decode('utf-8')
    return re.findall(r,t)

r0=r'href="(jair\S+)">JAIR'
u0="http://www.aaai.org/Library/JAIR/jair-library.php"
c0=gt(r0,u0)

for i in c0:
    u1='http://www.aaai.org/Library/JAIR/'+i
    print(u1)    
    dl(u1,'E:\\')
