from view.creatwin import initwindow
from view.creatwin import *
from model.globalsvar import *
from model.tkinterstruct import TKgeovalues
from view.progress3pi import Progres3pi
from view.todolinecar import ToDolinebar
from presenter.gstodo import GSTodo
from fileinput import filename



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
    
    
    def addtodoListsFrame(self):
        # Name Frame with scroll bar list 
        self.mainwin.row = 5
        self.mainwin.column = 2
        self.mainwin.sticky = S
        self.mainwin.width = 120
        self.mainwin.height = 20
        self.valueList = self.mainwin.add_frame()    

    
    def addTodoBars(self):
        tkg = TKgeovalues(self.valueList)
        tkg.column = 1
        self.todo = []
        for j in range(WI_TODOPROGRESBARLINE -1):
            tkg.row = j+1
            self.todo.append( ToDolinebar(tkg, 'empty0' +str(j+1)))
    
    
    def loadTodoList(self):
        namelist = self.gsFile.getNameList()
        for j in range(WI_TODOPROGRESBARLINE -1):
            self.todo[j].set_name(namelist[j].value)
            name = "G" + str(3 +j)
#             print(self.gsFile.getCellFromMain(name)) 
#             print(self.gsFile.getListOfProgressForCell(
#                      self.gsFile.getCellFromMain(name))) 
            self.todo[j].setProgressLine(
                self.gsFile.getListOfProgressForCell(
                     self.gsFile.getCellFromMain(name))) 
#         vaibls = [10,20,30,40,50]
#         self.todo[0].setProgressLine(vaibls) 
#        self.todo[0].setProgressLine(getListOfProgressForCell(self.gsFile.sheet_main.acell('J3'))) 
    
    def addPiFrame(self):
        self.mainwin.row = 6
        self.mainwin.sticky = S
        self.piList = self.mainwin.add_frame()
    
    
    def addPis(self):
        tkg = TKgeovalues(self.piList)
        tkg.column = 1
        tkg.row = 1
        self.pi100 = Progres3pi(tkg, "К 100%")
        tkg = TKgeovalues(self.piList)
        tkg.column = 2
        tkg.row = 1
        self.pi24h = Progres3pi(tkg, "24 Часа")
        tkg = TKgeovalues(self.piList)
        tkg.column = 3
        tkg.row = 1
        self.piTuday = Progres3pi(tkg, "Сегодня")
    
    
    def fillPi(self, pi, value):
        pi.pi1.set_value(value[0])
        pi.pi2.set_value(value[1])
        pi.pi3.set_value(value[2])
    
    
    def loadPisData(self):
        self.fillPi(self.pi100, self.gsFile.getPiListOfProgressBarForCell(TD_PISUM))
        self.fillPi(self.pi24h, self.gsFile.getPiListOfProgressBarForCell(TD_PI24H))
        self.fillPi(self.piTuday, self.gsFile.getPiListOfProgressBarForCell(TD_PITUDAY))

    
    def openGoogleSheet(self, file_name, crade_name):
        self.gsFile = GSTodo(filename = file_name, credfile = crade_name)

    
    
    
    
    
    
    

    
    
        
        
        
        
        