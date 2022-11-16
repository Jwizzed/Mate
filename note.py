from login import Login
import json
from datetime import date


class Note:
    def __init__(self, login_class: Login):
        self.__user = login_class.information[0]

    @property
    def user(self):
        return self.__user

    def add_note(self):
        """Add note to the user's note list"""

        while True:
            deadline = input("Enter the deadline date (day/month/year): ")
            if deadline.count("/") != 2:
                print("Wrong format. Try again.")
                continue
            else:
                break
        note = input("Enter the note: ")
        with open('user.json', 'r') as file:
            users = json.load(file)
            for user in users:
                if user.get(self.user):
                    try:
                        user[self.user]['Note'][deadline] = note
                    except KeyError:
                        user[self.user]['Note'] = {}
                        user[self.user]['Note'][deadline] = note
        with open('user.json', 'w') as file:
            json.dump(users, file)

    def show_note(self):
        """Show the note list of the user"""

        _list = []
        with open('user.json', 'r') as file:
            users = json.load(file)
            for user in users:
                if user.get(self.user):
                    for date, note in user[self.user]['Note'].items():
                        _list.append(f"{date}: {note}")
        return _list

    def delete_note(self):
        """Delete the note from the user's note list"""

        date = input("Enter the date of the note you want to delete: ")
        with open('user.json', 'r') as file:
            users = json.load(file)
            for user in users:
                if user.get(self.user):
                    user[self.user]['Note'].pop(date)
        with open('user.json', 'w') as file:
            json.dump(users, file)
            