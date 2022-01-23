
import os
from dotenv import load_dotenv
from notion_database.database import Database
from models.note.note_model import Note
import csv
load_dotenv()
DATABASE_ID = os.environ['DATABASE_ID']
NOTION_URL = os.environ['NOTION_URL']
INTEGRATION_TOKEN = os.environ['INTEGRATION_TOKEN']
FILE_NAME = os.environ['FILE_NAME']
database = Database(integrations_token=os.environ['INTEGRATION_TOKEN'])
database.run_query_database(DATABASE_ID)
notes = []
for r in database.result['results']:
    n = Note(r['properties'])
    notes.append(n)

def fun(note):
    if ('TimeTracking' in note.notetype):
        return True
    else:
        return False
# writing to csv file 
def export_csv(tracking_notes):
    with open('./test.csv', 'w') as csvfile:  
        # for i in tracking_notes:
        #     print(i) 
        csvwriter = csv.writer(csvfile) 
        headers = list(Note(getParams=True).__dict__.keys())
        csvwriter.writerow(headers)
        for n in tracking_notes:
            csvwriter.writerow([getattr(n,h) for h in headers])

if __name__ == "__main__":
    tracking_notes = filter(fun,notes)
    export_csv(tracking_notes)