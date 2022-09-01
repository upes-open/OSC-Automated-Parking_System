from curses import echo #code by akanksha
from logging import exception #code by akanksha
import speech_recognition as sr 
import gspread #code by akanksha
from oauth2client.service_account import ServiceAccountCredentials #code by akanksha
import datetime
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"] #code by akanksha
creds = ServiceAccountCredentials.from_json_keyfile_name("Speech_to_Text/gs_credentials.json",scope) #code by akanksha
client = gspread.authorize(creds) #code by akanksha
r = sr.Recognizer()
worksheet = client.open("Parking Sheet").sheet1 #code by akanksha
cells = worksheet.col_values(col=1)
s_no = len(cells)
time = datetime.datetime.now()
with sr.Microphone() as source:
    print("SPEAK")
    audio = r.listen(source)
    try: 
        text = r.recognize_google(audio)
        insertRow = list(text.split("and"))
        for i in range(0,len(insertRow)):
            insertRow[i] = insertRow[i].replace(" ", "")
        if (len(insertRow) > 1):
            insertRow = [(s_no)] + insertRow + [str(time)]
            worksheet.insert_row(insertRow,(s_no + 1))
            print('you said {}'.format(insertRow))
        else:
            raise exception
    except:
        print("sorry but couldn't hear.")
