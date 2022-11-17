import smtplib
from login import Login
import json


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
