import json
from json.decoder import JSONDecodeError


class Login:
    """
    This class is for the login and register.
    :parameter user: Username
    :parameter password: Password
    :parameter mymail: Mail
    """

    def __init__(self, username: str, password: str, mail: str) -> None:
        self.__user = username
        self.__password = password
        self.__mymail = mail
        self.__information = [self.user, self.password, self.mymail]

    @property
    def user(self) -> str:
        """Return the username"""
        return self.__user

    @user.setter
    def user(self, new_username) -> None:
        """Change the username"""
        self.__user = new_username

    @property
    def password(self) -> str:
        """Return the password"""
        return self.__password

    @password.setter
    def password(self, new_password) -> None:
        """Change the password"""
        self.__password = new_password

    @property
    def mymail(self) -> str:
        """Return the user's mail."""
        return self.__mymail

    @mymail.setter
    def mymail(self, new_mail) -> None:
        """Change the user's mail."""
        self.__mymail = new_mail

    @property
    def information(self) -> list:
        """Return the information of the user"""
        return self.__information

    @information.setter
    def information(self, new_information) -> None:
        """Change the information of the user"""
        self.__information = new_information

    def login(self) -> bool:
        """Login the user to the json file"""
        with open('user.json', 'r', encoding="utf-8") as file:
            try:
                users = json.load(file)
            except JSONDecodeError:
                with open('user.json', 'w', encoding="utf-8") as writable_file:
                    food = []
                    json.dump(food, writable_file, indent=4)
                    users = json.load(file)
            for user in users:
                try:
                    if user[self.user]['password'] == self.password:
                        return True
                except KeyError:
                    pass
            return False

    def register(self) -> None:
        """Register the user to the json file"""
        with open("user.json", mode='r', encoding='utf-8') as datas:
            try:
                data = json.load(datas)
            except JSONDecodeError:
                data = []
        with open("user.json", "w", encoding="utf-8") as json_file:
            data.append(
                {
                    self.user: {
                        "password": self.password
                    }
                }
            )
            json.dump(data, json_file, indent=4)

    def check_register(self):
        """Check if the user is registered by checking both username and
        password if the username is existed but the password is not the same,
        it will still register"""
        with open("user.json", mode='r', encoding='utf-8') as datas:
            try:
                data = json.load(datas)
            except JSONDecodeError:
                data = []
            for i in data:
                if self.user == list(i.keys())[0] and self.password == \
                        i[self.user]['password']:
                    return False
            return True

    def delete_account(self) -> bool:
        """Delete the account from the json file"""
        with open('user.json', 'r', encoding="utf-8") as file:
            users = json.load(file)
            if self.login():
                for user in users:
                    if user.get(self.user):
                        users.remove(user)
                        with open('user.json', 'w', encoding="utf-8") as _file:
                            json.dump(users, _file, indent=4)
                        return True
            return False
