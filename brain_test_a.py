import re
def cc(ag): # casual conversation
    i=''
    while i!='x':
        i=input('human: ')
        ag.ex(i) # exchange ideas

class br:
    def __init__(self):
        self.m=[] # working memory
        self.k={} # knowledge
        self.s=0  # score

    def ex(self,i): # exchange ideas
        i=re.split('/(d+)$',i)+['0']
        i,s=i[:2] # idea, score
        self.m.append(i) # append idea to working memory
        self.plan_a(i)

    def plan_a(self,i):
        if i in self.k.keys(): # if idea is a knowledge then repeat it
            self.rsp(i)
        else: # else response ...
            if self.m.count(i)>=3: # if learn idea more than 3 times
                self.k[i]=1 # make it knowledge
        self.rsp('...')

    def rsp(self,i): # chief response
        print('chief: '+i)

cf=br()
cc(cf)
     
