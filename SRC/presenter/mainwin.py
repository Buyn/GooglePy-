from view.creatwin import initwindow
from view.creatwin import *
from model.globalsvar import *
from model.tkinterstruct import TKgeovalues
from view.progress3pi import Progres3pi
from view.todolinecar import ToDolinebar



class mainwindow(object):
    """Initilaze and Creat Main window For App"""

    def reloadfile(self):
        print("button:")


    def __init__(self, title):
#         super(mainwindow, self).__init__()
        self.mainwin = initwindow(title)

    
    def mainloop(self):
        self.mainwin.mainloop()

    
    def addButtonsFrame(self):
        #    File path field
        self.mainwin.sticky = (N, W)
        self.mainwin.row = 3
        self.mainwin.column = 2
        self.mainwin.width = 123

    
    
    def addButtons(self):
        self.mainwin.text="Reload XML File"
        #    Open Button
        self.mainwin.addne_button( self.reloadfile)
    
    
    def addPiFrame(self):
        self.mainwin.row = 6
        self.mainwin.sticky = S
        self.piList = self.mainwin.add_frame()
    
    
    def addtodoListsFrame(self):
        # Name Frame with scroll bar list 
        self.mainwin.row = 5
        self.mainwin.column = 2
        self.mainwin.sticky = S
        self.mainwin.width = 120
        self.mainwin.height = 20
        self.valueList = self.mainwin.add_frame()    

    
    def addPis(self):
        tkg = TKgeovalues(self.piList)
        tkg.column = 4
        tkg.row = 1
        self.pi01 = Progres3pi(tkg, "Test")
    
    
    def addTodoBars(self):
        tkg = TKgeovalues(self.valueList)
        tkg.column = 1
        tkg.row = 0
        self.todo01 = ToDolinebar(tkg, 'Test')
    
    
    def creatMainWin(self, ):
        self.addButtonsFrame()
        self.addButtons()
        self.addtodoListsFrame()
        self.addPiFrame()
        self.addPis()
        self.addTodoBars()
        # end of init
        self.todo01.value.set(42)
        self.todo01.title_name.set("All work")
        
        
        
        
        