'''models for the INCIDENTS'''
# initialize empty list to store our data
INCIDENTS = []


class RedFlagModel():
    '''class to save our data, find by
    specific id, delete any incident and
    get all INCIDENTS
    '''

    def __init__(self):
        '''init(constructor) make sure the id numbers
         follow in order'''
        self.db = INCIDENTS
        if len(INCIDENTS) == 0:
            self.id = 1
        else:
            # last item in the array + 1
            self.id = INCIDENTS[-1]['id'] + 1
        self.id = len(INCIDENTS) + 1

    def save(self, data):
        '''method to save INCIDENTS'''
        data['id'] = self.id

        self.db.append(data)

    def find(self, redflag_id):
        '''method to find all INCIDENTS by id'''
        for incident in self.db:
            if incident['id'] == redflag_id:
                return incident

        return None

    def delete(self, incident):
        '''method to delete all INCIDENTS'''
        self.db.remove(incident)

    def get_all(self):
        '''method to get all INCIDENTS'''
        return self.db
