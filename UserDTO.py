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

    def __str__(self):
        return f"""
                Nom : {self.lastname}
                Prenom : {self.firstname}
                Grade : {self.grade}
                Login : {self.login}
                """
    
    def get_id(self):
        return self._id