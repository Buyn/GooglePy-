from oauth2client.service_account import ServiceAccountCredentials
import gspread
from model.globalsvar import *
class GSTodo(object):
    
    
    def __init__(self, credfile = GS_CRED_FILE):
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(credfile, scope)
        client = gspread.authorize(creds)
        self.file = client.open(GS_FILE)
        self.sheet_main = self.file.worksheet(TD_MAINSHEET)
        self.sheet_calc = self.file.worksheet(TD_CALCSHEET)

    
    def getTimeStump(self, address = TD_TIMESTUMP):
        return self.sheet_main.acell(address).value

    
    def getProgressTo100Sum(self, address = TD_SUMPROGRESS100):
        return self.sheet_calc.acell(address).value
    
    
    
    
    
    



