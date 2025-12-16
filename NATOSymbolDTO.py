class NATOSymbolDTO:

    def __init__(self, id, pos_x, pos_y, color):
        self._id = id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    def get_id(self):
        return self._id
    
    def get_pos_x(self):
        return self.pos_x