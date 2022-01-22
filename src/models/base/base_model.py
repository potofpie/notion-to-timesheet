from notion_database.database import Database

class BaseNotionModel:
    def parse_start_date_end_date_field(self, prop, name):
        return [prop['date']['start'], prop['date']['end']]
    def parse_date_field(self, prop, name):
        pass
        # todo
    def parse_select_field(self, prop, name):
        select = prop['select']
        if(not select):
            return None
        else:
            return prop['select']['name']
    def parse_multi_select_field(self, prop, name):
        return [select['name'] for select in prop['multi_select'] ]
    def parse_formula_field(self, prop, name):
        return self.parse_field(prop['formula'], name)
    def parse_title_field(self, prop, name):
        if(len(prop['title'])):
            return prop['title'][0]['text']['content']
        else:
            return  None
    def parse_rich_text_field(self, prop, name):
        if(len(prop['rich_text'])):
            return prop['rich_text'][0]['text']['content']
        else:
            return  None

    def parse_field(self, prop, name):

        try:
            if(prop['type'] == 'date'):
                if(prop['date'] == None):
                    return None
                double = len(prop['date'].keys()) > 2
                if(double):
                    self.parse_start_date_end_date_field(prop, name)
                else:
                    self.parse_date_field(prop, name)
            elif(prop['type'] == 'title'):
                return self.parse_title_field(prop, name)
            elif(prop['type'] == 'rich_text'):
                return self.parse_rich_text_field(prop, name)
            elif(prop['type'] == 'formula'):
                return self.parse_formula_field(prop, name)
            elif(prop['type'] == 'multi_select'):
                return self.parse_multi_select_field(prop, name)
            elif(prop['type'] == 'select'):
                return self.parse_select_field(prop, name)
            else:
                return prop[prop['type']]
        except:
            print(f"Field type: '{prop['type'] }'") 
            print(f"Name: '{name}' could not be parsed: ")
            print(f"Data: \n {prop}" )
            return None

    def parse_result(self, properties):
        for p in properties:        
            setattr(self, p.lower().replace(' ','_'), self.parse_field(properties[p], p ))
