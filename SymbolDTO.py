class SymbolDTO:

    def __init__(self, id, Stype, color):
        self._id = id
        self.Stype = Stype
        self.color = color

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id
    
    def set_Stype(self, Stype):
        self.Stype = Stype

    def get_Stype(self):
        return self.Stype
    
    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color