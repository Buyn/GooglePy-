#import block {{{
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from model.globalsvar import *
from model.typsconvert import *
import time
# }}}

class SheetGSpread(object):# {{{

    def __init__(self, gfile, sheetname):# {{{
        self.gfile = gfile
        self.sheetname = sheetname
        self.sheet = self.gfile.worksheet(
            self.sheetname).get_all_values()
        # }}}
    
    class GCell(object):# {{{
        def __init__(self):# {{{
            self.value = None
            self.name = None
            self.col = None
            self.row = None
            self.sheet = None
            # }}}
        def getCoord(self):# {{{
            return [self.row, self.col]
            # }}}
    # }}}

    def update_acell(self, cellname, value):# {{{
        self.gfile.worksheet(
            self.sheetname).update_acell(
                cellname, value)
        # }}}

    def atoarrint(self, cellname):# {{{
        if len(cellname) ==2:
            return [self.atoint(cellname[0]),
                       self.isInt(cellname[1])]
        result =[0,0]
        for i in range(len(cellname)): 
            if self.isInt(cellname[i]) == -1:
                result[0] += self.atoint(cellname[0])*(10**i)
            else:
                result[1] += self.isInt(cellname[i])*(10**(len(cellname) -1 - i))
        return result
        # }}}
    
    def isInt(self, var):# {{{
        if isinstance(var, int):
            return var
        if isinstance(var, list) and len(var) == 1:
            return var[0]
        try:
            return int(var)
        except ValueError:
            return -1
        # }}}

    def atoint(self, a):# {{{
        return ord( a.lower() ) - 96
        # }}}

    def acell(self, cellname):# {{{
        cell = self.GCell()
        cell.sheet = self
        cell.name = cellname
        cell.col, cell.row = self.atoarrint(cellname)
#         print(cell.row, " , ", cell.col)
        cell.value = self.sheet[cell.row -1][cell.col -1]
        return cell 
        # }}}
    
    def cell(self, row, col):# {{{
        cell = self.GCell()
        cell.sheet = self
        cell.col, cell.row = col, row
        cell.value = self.sheet[cell.row -1][cell.col -1]
        return cell 
        # }}}

    def range(self, rangestring):# {{{
        result =[]
        split = rangestring.split( ":")
        begin   = self.acell(split[0]).getCoord()
        end     = self.acell(split[1]).getCoord()
        for col in range(*( begin[0], end[0] +1 ) if begin[0]<end[0] else (end[0], begin[0]+1)):
            for row in range(*( begin[1], end[1] +1 ) if begin[1]<end[1] else (end[1], begin[1]+1 )):
                result.append(self.cell(col, row))
        return result
        # }}}

    
    def reload(self):# {{{
        self.sheet = self.gfile.worksheet(
            self.sheetname).get_all_values()
        # }}}
    
    # }}}
    
class GSTodo(object):# {{{
    
    def __init__(self, filename = GS_FILE, credfile = GS_CRED_FILE):# {{{
        # use creds to create begin client to interact with the Google Drive API
        self.filename = filename
        self.credfile = credfile
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(credfile, scope)
        self.client = gspread.authorize(creds)
        self.file = self.client.open(self.filename)
        self.sheet_main = SheetGSpread (self.file, TD_MAINSHEET)
        self.sheet_calc = SheetGSpread(self.file, TD_CALCSHEET)
        self.credtimeuot = time.time() + GS_TIMEOUTLOGIN
        # }}}
    
    def getTimeStump(self, address = TD_TIMESTUMP):# {{{
        return self.sheet_main.acell(address).value
        # }}}
    
    def getProgressTo100Sum(self, address = TD_SUMPROGRESS100):# {{{
        return self.sheet_calc.acell(address).value
        # }}}
    
    def getNameList(self):# {{{
        return self.sheet_main.range(TD_NAMERANGE) 
        # }}}
    
    def getListOfProgressForCell(self, cell):# {{{
        result = []
        result.append(self.sheet_main.cell(cell.row, cell.col - 1).value)
        result.append(self.sheet_main.cell(cell.row, cell.col + 3).value)
        result.append(self.sheet_main.cell(cell.row, cell.col + 4).value)
        result.append(self.sheet_main.cell(cell.row, cell.col + 5).value)
        result.append(self.sheet_main.cell(cell.row, cell.col + 6).value)
        result.append(self.sheet_main.cell(cell.row, cell.col + 7).value)
        return result
        # }}}
    
    def getPiListOfProgressBarForCell(self, cell_adress):# {{{
        cell = self.sheet_calc.acell(cell_adress) 
        result = []
        for i in range(3):
            value = int(
                        self.sheet_calc.cell( cell.row + i,
                                            cell.col).value.strip('%')
                        )
            if (value < 0):
                value = 0
            value = value * 3
            result.append(value)
        return result
        # }}}
    
    def getCellFromMain(self, name):# {{{
#         print(self.sheet_main.acell(name))
        return self.sheet_main.acell(name)
        # }}}

    def checkCred(self):# {{{
        if time.time() < self.credtimeuot: 
            self.credtimeuot = time.time() + GS_TIMEOUTLOGIN
            return
        self.client = None
        self.file = None
        print("Credet Timeout")
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.credfile, scope)
        print("clent was = ", self.client)
        self.client = gspread.authorize(creds)
        print("clent is = ", self.client)
        print("file was = ", self.file)
        self.file = self.client.open(self.filename)
        print("file is = ", self.file)
        self.credtimeuot = time.time() + GS_TIMEOUTLOGIN
        # }}}
    
    def setBingo(self):# {{{
        self.checkCred()
        self.sheet_main.update_acell('A1', 'Bingo!')    
        # }}}

    def insertNewLogLine(self, newLine):# {{{
        self.file.worksheet(
            TD_LOG).insert_row(
                self.compileNewLogString(
                    name = newLine[0], time = newLine[1])
                ,index = TD_NEWLOGLINEINDEX 
                ,value_input_option= "USER_ENTERED")
        # }}}
    
    def reloadsheets(self):# {{{
        self.checkCred()
        self.sheet_main.reload()
        self.sheet_calc.reload()
        # }}}
    
    def sendNewLogLine(self, newLine):# {{{
        print(newLine)
        self.setBingo()
        self.reloadsheets()
        self.insertNewLogLine(newLine)
        self.reloadsheets()
        # }}}

    def addEmptyString(self, result, counter):# {{{
        for i in range(counter):
            result.append("")
    # }}}
    
    def getSumProgresto100(self, address = TD_SUMPROGRESS100 ):# {{{
        return p2f(self.sheet_calc.acell(address).value)
    # }}}
    
    def compileNewLogString(self, name, time):# {{{
        result = [self.getTimeStump()]
        self.addEmptyString(result, counter = 2)
        result.append(time)
        result.append(name)
        self.addEmptyString(result, counter = 5)
        result.append("=NOW() - A21")
        result.append("=A21-Blans!$O$1")
        result.append(self.getSumProgresto100())
        self.addEmptyString(result, counter = 2)
        result.append("=INT(A21)")
        return result
        # }}}
    # }}}
    
    
    
    
    

    
    
    
    
    
    
    
    
    



