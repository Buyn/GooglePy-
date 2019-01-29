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
        self.height = 7
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
    
    def add_frame(self):
        frame = ttk.Frame(self.parent, padding="1 1 1 1")
        frame.grid(
                column  = self.column,
                row     = self.row,
                sticky  = self.sticky)
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

    def add_progressbar100(self, varible, orienting = HORIZONTAL):
        bar = ttk.Progressbar( 
                self.parent, 
                orient = orienting,
                mode='determinate',
                length = self.width,
                variable = varible
                )
        bar.grid(
                column  = self.column,
                row     = self.row,
                sticky  = self.sticky)
        return bar
   

    def add_text(self, varible):
        text_label = ttk.Label( 
                self.parent, 
                #length=100,
                width = self.width, 
                text = varible
                )
        text_label.grid(
                column  = self.column,
                row     = self.row,
                sticky  = self.sticky)
        return text_label


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
                yscrollcommand = scrollbar.set_value , 
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

    
    def add_Line(self, name, value, h24, tuday, day3, week, month):
        progress_line = self.add_frame() 
        self.parent = progress_line
        self.row = 1
        self.width = 20
        self.height = 0
        self.column = 1
        self.add_text(name)
        self.column = 2
        self.width = 5
        self.addne_entry(value)
        self.column = 3
        self.width = 50
        self.add_progressbar100(h24)
        self.column = 4
        self.add_progressbar100(tuday)
        self.column = 5
        self.add_progressbar100(day3)
        self.column = 6
        self.add_progressbar100(week)
        self.column = 7
        self.add_progressbar100(month)
    
    
    def add_pi3(self, name, pi1, pi2, pi3):
        pi3_block = self.add_frame() 
        self.parent = pi3_block
        self.width = 10
        self.height = 0
        self.column = 1
        self.row = 1
        self.add_text(name)
        self.row = 2
        self.width = 90
        self.add_progressbar100(pi1)
        self.row = 3
        self.add_progressbar100(pi2)
        self.row = 4
        self.add_progressbar100(pi3)
