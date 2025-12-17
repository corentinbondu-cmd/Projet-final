class UserDTO:

    def __init__(self, id, firstname, lastname, rank, grade, token, login, password):
        self._id = id
        self.firstname = firstname
        self.lastname = lastname
        self.rank = rank
        self.grade = grade
        self.token = token
        self.login = login
        self.password = password
    
    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id
    
    def set_firstname(self, firstname):
        self.firstname = firstname
    
    def get_firstname(self):
        return self.firstname

    def set_lastname(self, lastname):
        self.lastname = lastname
    
    def get_lastname(self):
        return self.lastname

    def set_rank(self, rank):
        self.rank = rank

    def get_rank(self):
        return self.rank

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def get_token(self):
        return self.token

    def set_token(self, token):
        self.token = token
    
    def set_login(self, login):
        self.login = login

    def get_login(self):
        return self.login

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password