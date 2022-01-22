from notion_orm.base.base_model import BaseNotionModel
class Note(BaseNotionModel):
    def __init__(self, properties=None, getParams=False):
        self.name  = None
        self.status = None
        self.ticket_number = None    
        self.notes_type = None
        self.date_created = None
        self.hour_span = None
        self.hours = None
        if(not getParams):
            super(Note, self).parse_result(properties)
       
    def __str__ (self):
        return f'''  
        =================
        Name: {self.name}
        Status: {self.status}
        Ticket Number: {self.ticket_number}    
        Notes Type: {self.note_type}
        Date Created: {self.date_created} 
        Hour Span: {self.hour_span}
        Hours: {self.hours}
        =================
        '''
    
