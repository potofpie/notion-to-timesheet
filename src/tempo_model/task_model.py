import os
import arrow
from notion_models.note.note_model import Note
class Task:
    def __init__(self, notion_obj: Note ):
        self.issueKey = notion_obj.ticketnumber
        self.timeSpentSeconds = notion_obj.hours * 3600
        self.billableSeconds = notion_obj.hours * 3600
        self.startDate = arrow.get(notion_obj.time[0]).format('YYYY-MM-DD')
        self.startTime = "00:00:00"
        self.description = "None"
        self.attributes = [{"key": "_WorkLevel_", "value": "NA"}],
        self.authorAccountId = os.environ['TEMPO_INTEGRATION_USER_ID']
