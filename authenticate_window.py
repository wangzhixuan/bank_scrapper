"""
by Zhixuan Wang
2019-01-21
"""

from tkinter import *



class Authenticate_Window(Frame):

    def __init__(self, bank, master=None):
        Frame.__init__(self, master)
        self.bank = bank
        self.init_window()

    def init_window(self):
        self.master.title("Please Enter Username and Password")
