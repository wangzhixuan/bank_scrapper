"""
by Zhixuan Wang
2019-01-21
"""

from tkinter import *

bank_choices = {'Chase', 'Wells Fargo', 'Bank of America', 'American Express', 'Discover'}



class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.tkvar=StringVar(master)
        self.tkvar.set(list(bank_choices)[0])
        self.bank_choices_checkbox = {bank: IntVar() for bank in bank_choices}

        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("Welcome to Bank Scrapper")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        #popupMenu = OptionMenu(self, self.tkvar, *bank_choices)
        #popupMenu.place(x=130, y=100)
        for i, bank in enumerate(bank_choices):
            Checkbutton(self.master, text=bank, variable=self.bank_choices_checkbox[bank]).place(x=130, y=100+i*30)

        # creating a button instance
        quitButton = Button(self, text="Quit", height=2, width=10, command=self.master.destroy)
        quitButton.place(x=550, y=500)

        # next button
        nextButton = Button(self, text="Next", height=2, width=10, command=self.process)
        nextButton.place(x=250, y=500)

    def process(self):
        print(self.bank_choices_checkbox)
        for bank in self.bank_choices_checkbox:
            if self.bank_choices_checkbox[bank].get() == 1:
                print(bank)
                self.authenticate(bank)

    def authenticate(self, bank):
        new_window=Toplevel()
        new_window.title('Authentication')

        msg=Message(new_window, text='Please enter your username and password for %s'%bank)
        msg.pack()

        btn=Button(new_window, text="hello")
        btn.pack()


