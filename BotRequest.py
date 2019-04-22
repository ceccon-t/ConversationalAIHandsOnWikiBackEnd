class BotRequest:

    def __init__(self, payload):
        self.data = payload

    def get_intents_present(self):
        return [intent['slug'] for intent in self.data['nlp']['intents']]

    def get_entities_present(self):
        return [entity for entity in self.data['nlp']['entities'].keys()]

    def get_entity(self, name):
        entity = []
        try:
            entity = self.data['nlp']['entities'][name]
        except:
            pass
        return entity

    def get_all_values_for_entity(self, name):
        return [element['raw'] for element in self.get_entity(name)]