from NATOSymbolDTO import NATOSymbolDTO

class SymbolDAO:
    def __init__(self, bdd):
        self.bdd = bdd

    def add_symbol(self, Stype):
        db = self.bdd['Project']
        if 'symbols' not in db.list_collection_names():
            db.create_collection('symbols')
        if db.symbols.count_documents({}) == 0:
            newId = 0
        else:
            newId = list(db.symbols.aggregate([
                {'$sort' : {'_id' : -1}},
                {'$limit' : 1}
            ]))[0]['_id'] + 1
        match Stype:
            case "otan":
                newSymbol = NATOSymbolDTO(newId, 10, 12, '#FF0000')
                db.symbols.insert_one(newSymbol.__dict__)
                return newSymbol
            case _:
                return 'pas un symbol'
        return 'already exist'