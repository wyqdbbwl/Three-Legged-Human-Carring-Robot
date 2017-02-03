from tkinter import *
import numpy as np

class pigeon(Frame):
  def createWidgets(self,master):
    self.c=Canvas(master,height=600,width=600)
    self.p=np.array([100,100],[100,200],[200,100]])
    self.w=np.array([1,1,1])
    for t,i in enumerate(self.p):
      self.createNode(i,10,'#eeaadd',t+1)
      self.bind_event(t+1)
    self.createNode(self.cg(self.p,self.w),5,'white','cg')
    self.c.pack()
    
  def createNode(self,p,r,c,t):
    x,y=p
    self.c.create_oval(x-r,y-r,x+r,y+r,fill=c,tags=t,width=0)
    
  def bind_event(self,t):
    self.c.tag_bind(t,'<ButtonPress-1>',lambda x:self.prs(x,t))
    self.c.tag_bind(t,'<ButtonRelease-1>',lambda x:self.rls(x,t))
    
  def move(self,event,t,d): # move node to new position
    self.c.coords(t,event.x+d[0]+1,event.y+d[1]+1,event.x+d[2]-1,event.y+d[3]-1)
    self.p[t-1]=sum(np.array(self.c.bbox(t)).reshape(2,2))/2
    self.renew()
    
  def renew(self): # renew center of gravity
    x,y=self.cg(self.p,self.w)
    self.c.coords('cg',x-5,y-5,x+5,y+5)
    
  def prs(self,event,t): # bind motion func after press
    d=np.array(self.c.bbox(t))-[event.x,event.y]*2
    self.c.tag_bind(t,'<Motion>', lambda x:self.move(x,t,d))
    
  def prs(self,event,t): # unbind motion func after release
    self.c.tag_unbind(t,'<Motion>')
    
  def cg(self,p,w): # position, weight
    return w.dot(p)/sum(w)
    
  def __init__(self, master=None):
    Frame.__init__(self,master)
    self.pack()
    self.createWidgets(master)

app=pigeon()
app.master.title('three ledgged pegion')
app.mainloop()
