import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("gs_credentials.json",scope)
client = gspread.authorize(creds)
sheet = client.open("Parking Sheet").sheet1
insertRow = ["1","2","3"]
sheet.insert_row(insertRow,7)

