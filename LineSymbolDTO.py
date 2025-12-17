from SymbolDTO import SymbolDTO

class LineSymbolDTO(SymbolDTO):

    def __init__(self, id, Stype, color, list_points):
        super().__init__(id, Stype, color)
        self.list_points = list_points

    def set_list_points(self, list_points):
        self.list_points = list_points

    def get_list_points(self):
        return self.list_points