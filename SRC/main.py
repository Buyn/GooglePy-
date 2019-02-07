'''
Created on 29 окт. 2017 г.

@author: BuYn
'''
from model.globalsvar import *
from presenter.mainwin import *


def main():
    mainwin.openGoogleSheet(GS_FILE, GS_CRED_FILE)
    mainwin.addButtonsFrame()
    mainwin.addButtons()
    mainwin.addPiFrame()
    mainwin.addPis()
    mainwin.loadPisData()
    mainwin.addtodoListsFrame()
    mainwin.addTodoBars()
    mainwin.mainloop()
    


if __name__ == '__main__':
    mainwin = mainwindow(APP_TITLE)
    main()
   




