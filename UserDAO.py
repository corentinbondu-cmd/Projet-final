from UserDTO import UserDTO

class UserDAO:

    def __init__(self, bdd):
        self.bdd = bdd

    def get_users(self):
        db = self.bdd['Project']
        result =  list(db.users.find({}))
        userDTOs = []
        for x in result:
            dto = UserDTO(x['_id'], x['firstname'], x['lastname'], x['rank'], x['grade'], x['token'], x['login'], x['lastname'])
            userDTOs.append(dto)
        return userDTOs
    
    def get_one_user_by_login(self, login):
        db = self.bdd['Project']
        result =  list(db.users.find({'login' : login}))
        return result

    def add_user(self, firstname, lastname, rank, grade, token, login, password):
        db = self.bdd['Project']
        if 'users' not in db.list_collection_names():
            db.create_collection('users')
        if db.users.count_documents({}) == 0:
            newId = 0
        else:
            newId = list(db.users.aggregate([
                {'$sort' : {'_id' : -1}},
                {'$limit' : 1}
            ]))[0]['_id'] + 1
        if not list(db.users.find({'login' : login})):
            newUser = UserDTO(newId, firstname, lastname, rank, grade, token, login, password)
            db.users.insert_one(newUser.__dict__)
            return newUser
        return 'already exist'
    
    def upadte_user(self, login, pw):
        db = self.bdd['Project']
        db.users.update_one({'login' : login}, {'$set' : {
            'password' : pw}
        })

    def get_mission(self, login):
        db = self.bdd['Project']
        missions = list(db.users.aggregate([{
            '$lookup' : {
                'from' : 'missions',
                'localField' : 'login',
                'foreignField' : 'chef',
                'as' : 'user_mission'
            }},
            {
                '$match' : {
                    'login' : login
                }
            }]))
        return missions