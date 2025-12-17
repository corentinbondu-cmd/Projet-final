from SymbolDTO import SymbolDTO

class NATOSymbolDTO(SymbolDTO):

    def __init__(self, id, Stype, color, pos_x, pos_y):
        super().__init__(id, Stype, color)
        self.pos_x = pos_x
        self.pos_y = pos_y

    def set_pos_x(self, pos_x):
        self.pos_x = pos_x

    def get_pos_x(self):
        return self.pos_x
    
    def set_pos_y(self, pos_y):
        self.pos_y = pos_y

    def get_pos_y(self):
        return self.pos_y