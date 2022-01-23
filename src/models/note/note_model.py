from notion_orm.base.base_model import BaseNotionModel
class Note(BaseNotionModel):
    def __init__(self, properties=None, getParams=False):
        self.name  = None
        self.status = None
        self.ticketnumber = None    
        self.notetype = None
        self.datecreated = None
        self.hourspan = None
        self.hours = None
        if(not getParams):
            super(Note, self).parse_result(properties)
       
    def __str__ (self):
        return f'''  
        =================
        Name: {self.name}
        Status: {self.status}
        Ticket Number: {self.ticketnumber}    
        Notes Type: {self.notetype}
        Date Created: {self.datecreated} 
        Hour Span: {self.hourspan}
        Hours: {self.hours}
        =================
        '''
    
