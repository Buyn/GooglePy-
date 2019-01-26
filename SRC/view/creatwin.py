from tkinter import *
from tkinter import ttk


class initwindow(object):
    """Init Main windows """


    def __init__(self, title):
        super(initwindow, self).__init__()
        self.root = Tk()
        self.root.title(title)
        self.mainframe = self.create_frame( self.root)
        self.init_next_element_parametrs( self.root)

    
    def init_next_element_parametrs(self, parent):
        """docstring for init_next_element_parametrs"""
        self.text   = "None" 
        self.width  = 7
        self.height  = 7
        self.row    = 2  
        self.column = 2  
        self.sticky = N
        self.parent = parent

    
    def create_frame(self, parent):
        frame = ttk.Frame(parent, padding="3 3 12 12")
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        return frame
    
    def mainloop(self):
        self.root.mainloop()

    
    def add_button(self, new_text, new_command, new_row=2, new_column=2, new_sticky=N):
        ttk.Button( self.mainframe, text=new_text, command=new_command).grid(column=new_column, row=new_row, sticky=new_sticky)

    
    def addne_button(self, new_command):
        button = ttk.Button(
                self.parent,
                text= self.text, 
                command= new_command
                )
        button.grid(
                        column  = self.column,
                        row     = self.row,
                        sticky  = self.sticky)
        return button

    
    def addne_entry(self, varible):
        entry = ttk.Entry( 
                self.parent, 
                width = self.width, 
                textvariable = varible
                )
        entry.grid(
                        column  = self.column,
                        row     = self.row,
                        sticky  = self.sticky)
        return entry

    
    def addne_framelist(self, name):
        frame = LabelFrame( self.parent, text=name)
        frame.grid(
                column  = self.column,
                row     = self.row,
                sticky  = self.sticky)

        scrollbar = Scrollbar(frame)
        scrollbar.pack( side = RIGHT, fill = Y )
        mylist = Listbox(
                frame, 
                yscrollcommand = scrollbar.set , 
                height = self.height, 
                width = self.width
        )
        #mylist.insert(END, "This is line number " + str("line"))
        mylist.pack( side = LEFT, fill = BOTH )
        scrollbar.config( command = mylist.yview )
        return mylist

    
    def fill_list_by_arrey(self, list_element, arrey_sorce):
        for text_string in arrey_sorce:
            list_element.insert(END, text_string)
