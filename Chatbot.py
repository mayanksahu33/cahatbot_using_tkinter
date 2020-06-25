from tkinter import *
import json
root=Tk()
def send():
    with open('F:\Chatbot\entry.json', 'r') as c:
        params = json.load(c)
    send="You => "+e.get()
    txt.insert(END,"\n"+send)
    if e.get() in params:
        txt.insert(END,"\n"+"Sys => "+params[e.get()])
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2 )
e=Entry(root,width=100)
send=Button(root,text="OK",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Chatbot")
root.mainloop()