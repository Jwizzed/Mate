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
        return _list

    def delete_note(self):
        """Delete the note from the user's note list"""

        date = input("Enter the date of the note you want to delete: ")
        with open('user.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
            if self.user in users:
                users[self.user]['Note'].pop(date)
        with open('user.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4)
