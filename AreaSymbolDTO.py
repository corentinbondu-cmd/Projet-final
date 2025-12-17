from SymbolDTO import SymbolDTO

class AreaSymbolDTO(SymbolDTO):

    def __init__(self, id, Stype, color, origin, radius):
        super().__init__(id, Stype, color)
        self.origin = origin
        self.radius = radius

    def set_origin(self, origin):
        self.origin = origin
    
    def get_origin(self):
        return self.origin
    
    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius