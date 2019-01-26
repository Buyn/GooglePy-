'''
Created on 29 окт. 2017 г.

@author: BuYn
'''
from model.globalsvar import *
from presenter.mainwin import *
from presenter.xmler import xmler


def main():
    parser.loadXML(START_FILE)
    mainwin.creatMainWin(parser)
    mainwin.mainloop()
    


if __name__ == '__main__':
    mainwin = mainwindow(APP_TITLE)
    parser  = xmler()
    main()
   




