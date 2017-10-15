# use mouse wheel or control-mouse wheel to generate and preview a color code, then append it to clipboard
import re, copy
from tkinter import *
class color:
    def __init__(self, master):
        self.el=[Entry(master) for i in range(5)]
        for n in range(5):
            self.el[n].grid(row=0, padx=0, column=n)
            self.el[n].config(justify='center', bd=0, width=[2,5,5,5,10][n],insertbackground='white')
        self.reset(0)
        for n in [1,2,3]:
            self.el[n].bind('<MouseWheel>',lambda e,n=n: self.mw(e,n,10))
            self.el[n].bind('<Control-MouseWheel>', lambda e,n=n:self.mw(e,n,1))
        self.el[4].bind('<Button-3>', self.reset)
    def mw(self,event,n,d):
        v=eval(self.el[n].get())
        v=v+[-1*d,1*d][event.delta>0]
        self.el[n].delete(0,'end')
        self.el[n].insert(0,str(v%256))
        self.set_color()
    def set_color(self):
        v=[self.el[i].get() for i in range(1,4)]
        v=[hex(eval(i))[2:] for i in v]
        v=[('00'+i)[-2:] for i in v]
        v='#'+''.join(v)
        self.el[4].delete(0,'end')
        self.el[4].insert(0,v)
        self.el[4].clipboard_clear()
        self.el[4].clipboard_append(v)
        self.el[0].config(bg=v,insertbackground=v)
    def reset(self,event):
        for n in [1,2,3]:
            self.el[n].delete(0, 'end')
            self.el[n].insert(0, '255')
        self.set_color()
r=Tk()
c=color(r)
r.title('color')
r.mainloop()
