class MissionDTO:

    def __init__(self, id, nom, pays, chef, users, branch_missions):
        self._id = id
        self.nom = nom
        self.pays = pays
        self.chef = chef
        self.users = users
        self.branch_missions = branch_missions
    
    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id
    
    def set_nom(self, nom):
        self.nom = nom

    def get_nom(self):
        return self.nom

    def set_pays(self, pays):
        self.pays = pays
        
    def get_pays(self):
        return self.pays

    def set_chef(self, chef):
        self.nochefm = chef
        
    def get_chef(self):
        return self.chef

    def set_users(self, users):
        self.users = users
        
    def get_users(self):
        return self.users

    def set_branch_missions(self, branch_missions):
        self.branch_missions = branch_missions
        
    def get_branch_missions(self):
        return self.branch_missions