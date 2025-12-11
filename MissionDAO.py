from MissionDTO import MissionDTO

class MissionDAO:
    def __init__(self, bdd):
        self.bdd = bdd

    def get_all_mission(self):
        db = self.bdd['Project']
        result =  list(db.missions.find({}))
        missionDTOs = []
        for x in result:
            dto = MissionDTO(x['_id'], x['nom'], x['pays'], x['chef'], [], [])
            missionDTOs.append(dto)
        return missionDTOs
    
    def add_mission(self, nom, pays, chef, users, branchMissions):
        db = self.bdd['Project']
        if 'missions' not in db.list_collection_names():
            db.create_collection('missions')
        newId = db.missions.count_documents({}) + 1
        if not list(db.missions.find({'nom' : nom})):
            newMission = MissionDTO(newId, nom, pays, chef, users, branchMissions)
            db.missions.insert_one(newMission.__dict__)
            return newMission
        return 'already exist'