'''
Created on 29 окт. 2017 г.

@author: BuYn
'''
from model.globalsvar import *
from presenter.mainwin import *


def main():
    mainwin.creatMainWin()
    mainwin.mainloop()
    


if __name__ == '__main__':
    mainwin = mainwindow(APP_TITLE)
    main()
   




