
import os, requests
from dotenv import load_dotenv
from notion_database.database import Database
from notion_models.note.note_model import Note
from tempo_model.task_model import Task



import csv
load_dotenv()
DATABASE_ID = os.environ['DATABASE_ID']
NOTION_URL = os.environ['NOTION_URL']
NOTION_INTEGRATION_TOKEN = os.environ['NOTION_INTEGRATION_TOKEN']
FILE_NAME = os.environ['FILE_NAME']


def fun(note):
    if ('TimeTracking' in note.notetype):
        return True
    else:
        return False



def export_to_tempo(tracking_notes):
    for n in tracking_notes:
        t = Task(n)
        print(t .__dict__)

        # r = requests.post("https://api.tempo.io/core/3/worklogs",
        #                 headers=headers,
        #                 json=body)
        # if not r.status_code in [200]:
        #     print(json.dumps(results))
        #     print(r.text, file=sys.stderr)
        #     print('request failed with code {}'.format(r.status_code), file=sys.stderr)
        #     sys.exit(1)
        # results.append(r.json())



if __name__ == "__main__":
    database = Database(integrations_token=NOTION_INTEGRATION_TOKEN)
    database.run_query_database(DATABASE_ID)
    notes = []
    for r in database.result['results']:
        n = Note(r['properties'])
        notes.append(n)
        # print(n)
    tracking_notes = filter(fun,notes)
    export_to_tempo(tracking_notes)
