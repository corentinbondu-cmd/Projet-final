from UserDTO import UserDTO

class UserDAO:

    def __init__(self, bdd):
        self.bdd = bdd

    def get_users(self):
        db = self.bdd['Project']
        result =  list(db.users.find({}))
        userDTOs = []
        for x in result:
            dto = UserDTO(x['_id'], x['firstname'], x['lastname'], '', '', '', '', '')
            userDTOs.append(dto)
        return userDTOs
    
    def add_user(self):
        db = self.bdd['Project']
        lastId = list(db.users.aggregate([
            {'$sort' : {'_id' : -1}},
            {'$limit' : 1}]))
        newUser = UserDTO(lastId[0]['_id'] + 1, 'Andre', 'Mifasol', '', '', '', '', '')
        print(newUser)
        db.users.insert_one(newUser.__dict__)
        return newUser