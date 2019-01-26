from view.creatwin import initwindow
from view.creatwin import *
from presenter import xmler
from model.globalsvar import *


class mainwindow(object):
    """Initilaze and Creat Main window For App"""

    def reloadfile(self):
        print("file path :", self.filepath.get())
        self.xmlparser.path = self.filepath.get()
        self.xmlparser.reload_xml()
        self.mainwin.fill_list_by_arrey(
            self.hublist,
            self.xmlparser.formatedstringlist_from_hubsetings()
        )
        self.mainwin.fill_list_by_arrey(
            self.telemetrilist,
            self.xmlparser.formatedstringlist_from_telemetry()
        )

    def __init__(self, title):
        super(mainwindow, self).__init__()
        self.mainwin = initwindow(title)

    
    def mainloop(self):
        self.mainwin.mainloop()

    
    def creatMainWin(self, xmlparser):
        self.xmlparser = xmlparser
        #    Win Title
        self.mainwin.text="Reload XML File"
        #    Open Button
        self.mainwin.addne_button( self.reloadfile)
        #    File path field
        self.filepath = StringVar()
        self.mainwin.sticky = (N, W)
        self.mainwin.row = 3
        self.mainwin.column = 2
        self.mainwin.width = 123
        self.filepath.set(START_FILE)
        self.mainwin.addne_entry( self.filepath)
        # Name Frame with scroll bar list 
        self.mainwin.row = 5
        self.mainwin.column = 2
        self.mainwin.sticky = S
        self.mainwin.width = 120
        self.mainwin.height = 20
        self.hublist = self.mainwin.addne_framelist("Hub Setings")
        # Name Frame with scroll bar list 
        self.mainwin.row = 6
        self.mainwin.sticky = S
        self.telemetrilist = self.mainwin.addne_framelist("Telemetry Date")
