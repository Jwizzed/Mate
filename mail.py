import json
import smtplib

from interest import Interest
from login import Login
from weather import Weather


class Mail:
    """This class is for sending mails.
    :parameter login_class: Login class
    """

    def __init__(self, login_class: Login) -> None:
        self.__mymail = login_class.information[2]
        self.__mail = "maillingformid@gmail.com"
        self.__password = "ncttzegkwvcgliog"
        self.__user = login_class.information[0]
        self.__topics_to_send = []

    @property
    def mymail(self) -> str:
        """Return the user's mail."""
        return self.__mymail

    @property
    def mail(self) -> str:
        """Return the mail address of the sender."""
        return self.__mail

    @mail.setter
    def mail(self, new_mail) -> None:
        """Change the mail address."""
        self.__mail = new_mail

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
        """Return the password of the mail."""
        return self.__password

    @password.setter
    def password(self, new_password) -> None:
        """Change the password of the mail."""
        self.__password = new_password

    @property
    def topics_to_send(self) -> list:
        """Return the topics to send."""
        with open('user.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
            if self.user in users:
                try:
                    self.topics_to_send = users[self.user]['mail']
                except KeyError:
                    pass
        return self.__topics_to_send

    @topics_to_send.setter
    def topics_to_send(self, new_topics_to_send) -> None:
        """Change the topics to send."""
        self.__topics_to_send = new_topics_to_send

    def change_topics_to_send(self, topics) -> None:
        """Add topics to send."""
        with open('user.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
            if self.user in users:
                try:
                    users[self.user]['mail'] = topics
                    self.__topics_to_send = topics
                except KeyError:
                    users[self.user]['mail'] = []
                    users[self.user]['mail'] = topics
        with open('user.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4)

    def send_mail(self, message) -> None:
        """Send a mail to the user's mail."""
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(self.mail, self.password)
            connection.sendmail(
                from_addr=self.mail,
                to_addrs=self.mymail,
                msg=message
            )

    def create_text(self, interest_class: Interest, weather_class: Weather):
        """Create the text of the mail."""
        text = f"Dear {self.user} Here are the headlines you should read:\n\n"
        for topic in self.__topics_to_send:

            if topic == "Note":
                text += "- Note \n"
                with open("user.json", 'r', encoding='utf-8') as notes:
                    note_list = json.load(notes)[self.user]
                    for date, note in note_list['Note'].items():
                        text += f"\t{date}: {note}\n"
                    text += "\n\n"

            elif topic == "Fortune":
                text += "- Fortune\n"
                text += f"\t{interest_class.show_fortune_telling()}"
                text += "\n\n"

            elif topic == "Food":
                text += "- Food\n"
                text += f"\t{interest_class.show_something_to_eat()}"
                text += "\n\n"

            elif topic == "Song":
                text += "- Songs\n"
                for music in interest_class.show_top_10_songs():
                    text += f"\t{music}\n"
                text += "\n"

            elif topic == "News":
                text += "- News"
                for news in interest_class.show_interest_news():
                    text += "\n"
                    text += "\t" + news[0]
                    text += '\n\t\t' + news[1]
                    try:
                        text += '\n\t\t' + news[2].encode('utf-8'). \
                            decode('utf-8')
                    except IndexError:
                        text += '\n\t\t' + "Link broken"
                text += "\n\n"

            elif topic == "Weather":
                text += "- Weather"
                for hour in weather_class.show_weather():
                    text += f"\n\t{hour}"
                text += "\n\n"
        return text
