from oauth2client.service_account import ServiceAccountCredentials
import gspread
from model.globalsvar import *
class GSTodo(object):
    
    
    def __init__(self, filename = GS_FILE, credfile = GS_CRED_FILE):
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(credfile, scope)
        client = gspread.authorize(creds)
        self.file = client.open(filename)
        self.sheet_main = self.file.worksheet(TD_MAINSHEET)
        self.sheet_calc = self.file.worksheet(TD_CALCSHEET)

    
    def getTimeStump(self, address = TD_TIMESTUMP):
        return self.sheet_main.acell(address).value

    
    def getProgressTo100Sum(self, address = TD_SUMPROGRESS100):
        return self.sheet_calc.acell(address).value

    
    def getNameList(self):
        return self.sheet_main.range(TD_NAMERANGE) 

    
    def getListOfProgressForCell(self, cell):
        result = []
        result.append(self.sheet_main.cell(cell.row, cell.col - 1).value)
        result.append(self.sheet_main.cell(cell.row, cell.col + 3).value)
        result.append(self.sheet_main.cell(cell.row, cell.col + 4).value)
        result.append(self.sheet_main.cell(cell.row, cell.col + 5).value)
        result.append(self.sheet_main.cell(cell.row, cell.col + 6).value)
        result.append(self.sheet_main.cell(cell.row, cell.col + 7).value)
        return result

    
    def getPiListOfProgressBarForCell(self, cell_adress):
        cell = self.sheet_calc.acell(cell_adress) 
        result = []
        for i in range(3):
            value = int(
                        self.sheet_calc.cell( cell.row + i,
                                            cell.col).value.strip('%')
                        )
            if (value < 0):
                value = 0
            result.append(value)
        return result
    
    
    
    
    

    
    
    
    
    
    
    
    
    



