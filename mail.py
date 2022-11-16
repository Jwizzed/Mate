import smtplib
from login import Login


class Mail:
    """This class is for sending mails.
    :parameter login_class: Login class
    """
    def __init__(self, login_class: Login) -> None:
        self.__mymail = login_class.information[2]
        self.__mail = "maillingformid@gmail.com"
        self.__password = "ncttzegkwvcgliog"

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
    def password(self) -> str:
        """Return the password of the mail."""
        return self.__password

    @password.setter
    def password(self, new_password) -> None:
        """Change the password of the mail."""
        self.__password = new_password

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
            