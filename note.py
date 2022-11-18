import json
from login import Login


class Note:
    """This class is for the note"""

    def __init__(self, login_class: Login):
        self.__user = login_class.information[0]

    @property
    def user(self):
        """Return the username"""
        return self.__user

    def add_note(self, deadline, note):
        """Add note to the user's note list"""
        with open('user.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
            if self.user in users:
                try:
                    users[self.user]['Note'][deadline] = note
                except KeyError:
                    users[self.user]['Note'] = {}
                    users[self.user]['Note'][deadline] = note
        with open('user.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4)

    def show_note(self):
        """Show the note list of the user"""
        _list = []
        with open('user.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
            if self.user in users:
                try:
                    for date, note in users[self.user]['Note'].items():
                        _list.append(f"{date}: {note}")
                except KeyError:
                    return "You don't have any note."
        return sorted(_list, key=lambda x: int(
            x.split(":")[0].split("/")[-1]) * 100 + int(
            x.split(":")[0].split("/")[1]) * 10 + int(
            x.split(":")[0].split("/")[0]), reverse=False)

    def delete_note(self, deadline):
        """Delete the note from the user's note list"""
        with open('user.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
            if self.user in users:
                if deadline in users[self.user]['Note']:
                    del users[self.user]['Note'][deadline]
                else:
                    return False
        with open('user.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4)
        return True
