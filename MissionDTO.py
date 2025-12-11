class MissionDTO:

    def __init__(self, id, nom, pays, chef, users, branchMissions):
        self._id = id
        self.nom = nom
        self.pays = pays
        self.chef = chef
        self.users = users
        self.branchMissions = branchMissions

    def __str__(self):
        return f"""
                Nom : {self.nom}
                Pays : {self.pays}
                Chef : {self.chef}
                """
    
    def get_id(self):
        return self._id