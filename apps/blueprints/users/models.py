class User:
    def __init__(self, id=None, name=None, email=None, gender=None, status=None):
        self.id = id
        self.name = name
        self.email = email
        self.gender = gender
        self.status = status

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
