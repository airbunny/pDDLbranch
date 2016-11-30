#!/usr/bin/python
# -*- coding: utf-8 -*-

import telnetlib
import time
import getpass
import sys
import os
import tkinter as tk

class CInputbox(tk.Frame):
    def __init__(cib, master=None):
        super().__init__(master)
        cib.pack()
        cib.create_widgets()

    def create_widgets(cib):
        cib.setid = tk.Button(cib)
        cib.setid["text"] = "set networkid"
        cib.setid["command"] = cib.destroy
        cib.setid.pack(side="top")

def tester():
    print("这都是些个啥？")
    inputer = tk.Tk()
    inputer.title =("输入NetworkID")
    inputer.geometry("200x100")
    ipp = CInputbox(master=root)
    ipp.mainloop()
    return

#########################################
#     windows class
#########################################
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.airset = tk.Button(self)
        self.airset["text"] = "set pddl air side"
        self.airset["command"] = self.telnetair
        self.airset.pack(side="top")

        self.grset = tk.Button(self)
        self.grset["text"] = "set pddl ground side"
        self.grset["command"] = self.telnetground
        self.grset.pack(side="top")
        
        self.quit = tk.Button(self, text="QUIT",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def telnetair(self):
        print("pddl")
        self.quit["state"] = "disable"
        
    def telnetground(self):
        print("ap01")
        self.quit["state"] = "active"


###########################################
#       main process
###########################################
root = tk.Tk()
root.title("猞猁饲养指南") #title
root.geometry("640x480")
#root.resizable(width=False, height=False)
app = Application(master=root)
app.mainloop()
