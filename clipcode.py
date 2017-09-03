# -*- coding: utf-8 -*-
def load(fn):
    f=open(fn,'r')
    f=f.read().split('<clipcode>')
    f=[i.strip(' \n').split('\n',1) for i in f[1:]]
    return dict(f)

def cpy(event):    
    k=t.get('current linestart', 'current lineend')
    t.clipboard_clear()
    t.clipboard_append(d[k])

def hl(event):
    t.tag_remove("highlight", 1.0, "end")
    t.tag_add("highlight", "current linestart", "current lineend+1c")

import tkinter as tk
r=tk.Tk()
t=tk.Text(r)
d=load('user.txt')
t.insert(0.0, '\n'.join(d.keys()))
t.config(font=('Courier New','10'))
t.config(height=40,width=28)
t.config(state='disabled')
t.tag_config("highlight", background='#f0f3fe')
t.tag_config("highlight", foreground='#333eff')
t.bind('<Button-1>',cpy)
t.bind('<Motion>',hl)
t.grid()
r.title('clipcode')
r.mainloop()
