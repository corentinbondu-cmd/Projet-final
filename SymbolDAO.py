from NATOSymbolDTO import NATOSymbolDTO
from LineSymbolDTO import LineSymbolDTO
from AreaSymbolDTO import AreaSymbolDTO

class SymbolDAO:
    def __init__(self, bdd):
        self.bdd = bdd

    def add_symbol(self, Stype, datas):
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
                newSymbol = NATOSymbolDTO(newId, Stype, datas['color'], datas['pos_x'], datas['pos_y'])
                db.symbols.insert_one(newSymbol.__dict__)
                return newSymbol
            case 'line':
                newSymbol = LineSymbolDTO(newId, Stype, datas['color'], datas['list_points'])
                db.symbols.insert_one(newSymbol.__dict__)
                return newSymbol
            case 'area':
                newSymbol = AreaSymbolDTO(newId, Stype, datas['color'], datas['origin'], datas['radius'])
                db.symbols.insert_one(newSymbol.__dict__)
                return newSymbol
            case _:
                return 'not a symbol'
        return 'already exist'