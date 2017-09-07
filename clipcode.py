# -*- coding: utf-8 -*-
def load(fn):
    f=open(fn,'r')
    f=f.read().split('#t=')
    f=[i.strip(' \n').split('\n',1) for i in f[1:]]
    return dict(f)

def rld(event):
    global d
    d=load('user.ctl')
    t.config(state='normal')
    t.delete(0.0,'end')
    t.insert(0.0, '\n'.join(d.keys()))
    t.config(state='disabled')
    
def cpy(event):
    global d
    k=t.get('current linestart', 'current lineend')
    d.setdefault(k)
    t.clipboard_clear()
    t.clipboard_append(d[k])
    
def hl(event):
    t.tag_remove("highlight", 1.0, "end")
    t.tag_add("highlight", "current linestart", "current lineend+1c")

import tkinter as tk
r=tk.Tk()
t=tk.Text(r)
t.insert(0.0, 'right click to update list')
t.config(font=('Courier New','10'))
t.config(height=40,width=28)
t.tag_config("highlight", background='#f7ecf8')
t.tag_config("highlight", foreground='#800000')
t.bind('<Button-1>',cpy)
t.bind('<Button-3>',rld)
t.bind('<Motion>',hl)
t.grid()
r.title('clipcode')
r.mainloop()
