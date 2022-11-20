import json
import random
import time
import turtle

from geopy.geocoders import Nominatim

from interest import Interest
from login import Login
from mail import Mail
from note import Note
from weather import Weather


class Display:
    """This class is for display the whole program."""

    def __init__(self) -> None:
        self.writer = turtle.Pen()
        self.screen = turtle.Screen()
        self.loging = None
        self.mail = None
        self.interesting = None
        self.weather = Weather()

    def login_register_button(self) -> None:
        """This function is for login and register button."""
        # login button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(-150, 0)
        self.writer.goto(150, 0)
        self.writer.goto(150, 50)
        self.writer.goto(-150, 50)
        self.writer.goto(-150, 0)
        self.writer.end_fill()
        self.writer.goto(-18, 15)
        self.writer.color("brown")
        self.writer.write("Login", font=('Arial', 15, 'normal'), align="left")

        # register button
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(-150, -75)
        self.writer.goto(150, -75)
        self.writer.goto(150, -25)
        self.writer.goto(-150, -25)
        self.writer.goto(-150, -75)
        self.writer.end_fill()
        self.writer.goto(-20, -60)
        self.writer.color("brown")
        self.writer.write("Register", font=('Arial', 15, 'normal'),
                          align="left")
        self.screen.onclick(self.login_register_click)

    def menu_button(self) -> None:
        """This function is for menu button."""
        # weather button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(-150, 0)
        self.writer.goto(150, 0)
        self.writer.goto(150, 50)
        self.writer.goto(-150, 50)
        self.writer.goto(-150, 0)
        self.writer.end_fill()
        self.writer.goto(-20, 15)
        self.writer.color("brown")
        self.writer.write("Weather", font=('Arial', 15, 'normal'),
                          align="left")
        # note button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(-150, -75)
        self.writer.goto(150, -75)
        self.writer.goto(150, -25)
        self.writer.goto(-150, -25)
        self.writer.goto(-150, -75)
        self.writer.end_fill()
        self.writer.goto(-13, -60)
        self.writer.color("brown")
        self.writer.write("Note", font=('Arial', 15, 'normal'),
                          align="left")
        # interest button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(-150, 75)
        self.writer.goto(150, 75)
        self.writer.goto(150, 125)
        self.writer.goto(-150, 125)
        self.writer.goto(-150, 75)
        self.writer.end_fill()
        self.writer.goto(-23, 90)
        self.writer.color("brown")
        self.writer.write("Interest", font=('Arial', 15, 'normal'),
                          align="left")
        # mail button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(-150, -145)
        self.writer.goto(150, -145)
        self.writer.goto(150, -95)
        self.writer.goto(-150, -95)
        self.writer.goto(-150, -145)
        self.writer.end_fill()
        self.writer.goto(-10, -130)
        self.writer.color("brown")
        self.writer.write("Mail", font=('Arial', 15, 'normal'),
                          align="left")
        self.screen.onclick(self.menu_click)

    def back_button(self) -> None:
        """This function is for back button."""
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(-416.0, -202.0)
        self.writer.begin_fill()
        self.writer.goto(-316, -202.0)
        self.writer.goto(-316, -252.0)
        self.writer.goto(-416.0, -252.0)
        self.writer.end_fill()
        self.writer.goto(-380.0, -237.0)
        self.writer.color("white")
        self.writer.write("Back", font=('Arial', 15, 'normal'),
                          align="left")
        self.screen.onclick(self.back_click)

    def change_interest_button(self, msg: str, func) -> None:
        """This function is for change interest button."""
        # add interest button
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(145, -140)
        self.writer.begin_fill()
        self.writer.goto(300, -140)
        self.writer.goto(300, -200)
        self.writer.goto(145, -200)
        self.writer.end_fill()
        self.writer.goto(215 - len(msg), -180)
        self.writer.color("white")
        self.writer.write(msg, font=('Arial', 15, 'normal'),
                          align="left")
        # back button
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(-416.0, -202.0)
        self.writer.begin_fill()
        self.writer.goto(-316, -202.0)
        self.writer.goto(-316, -252.0)
        self.writer.goto(-416.0, -252.0)
        self.writer.end_fill()
        self.writer.goto(-380, -237.0)
        self.writer.color("white")
        self.writer.write("Back", font=('Arial', 15, 'normal'),
                          align="left")
        self.screen.onclick(func)

    def mail_button(self) -> None:
        """This function is for mail button."""
        # add interest button
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(-305, -140)
        self.writer.begin_fill()
        self.writer.goto(-150, -140)
        self.writer.goto(-150, -200)
        self.writer.goto(-305, -200)
        self.writer.end_fill()
        self.writer.goto(-260, -180)
        self.writer.color("white")
        self.writer.write("Send mail", font=('Arial', 15, 'normal'),
                          align="left")
        self.change_interest_button("Change        ", self.mail_click)

    def delete_button(self, func) -> None:
        """This function is for delete button."""
        # delete button
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(-305, -140)
        self.writer.begin_fill()
        self.writer.goto(-150, -140)
        self.writer.goto(-150, -200)
        self.writer.goto(-305, -200)
        self.writer.end_fill()
        self.writer.goto(-250, -180)
        self.writer.color("white")
        self.writer.write("Delete", font=('Arial', 15, 'normal'),
                          align="left")
        self.change_interest_button("Add", func)

    def four_interest_buttons(self) -> None:
        """This function is for four interest buttons."""
        # Eats
        self.back_button()
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(-225.0, 120)
        self.writer.begin_fill()
        self.writer.goto(-25.0, 120)
        self.writer.goto(-25.0, 20)
        self.writer.goto(-225, 20)
        self.writer.end_fill()
        self.writer.goto(-190, 65)
        self.writer.forward(50)
        self.writer.color("white")
        self.writer.write("Eats", font=('Arial', 15, 'normal'),
                          align="left")
        # Songs
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(25, 120)
        self.writer.begin_fill()
        self.writer.goto(225, 120)
        self.writer.goto(225, 20)
        self.writer.goto(25, 20)
        self.writer.end_fill()
        self.writer.goto(105, 65)
        self.writer.color("white")
        self.writer.write("Songs", font=('Arial', 15, 'normal'),
                          align="left")
        # News
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(-225.0, -20)
        self.writer.begin_fill()
        self.writer.goto(-25.0, -20)
        self.writer.goto(-25.0, -120)
        self.writer.goto(-225, -120)
        self.writer.end_fill()
        self.writer.goto(-190, -80)
        self.writer.forward(50)
        self.writer.color("white")
        self.writer.write("News", font=('Arial', 15, 'normal'),
                          align="left")
        # Fortune
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(25, -20)
        self.writer.begin_fill()
        self.writer.goto(225, -20)
        self.writer.goto(225, -120)
        self.writer.goto(25, -120)
        self.writer.end_fill()
        self.writer.goto(60, -80)
        self.writer.forward(40)
        self.writer.color("white")
        self.writer.write("Fortune", font=('Arial', 15, 'normal'),
                          align="left")

    # Login/Register
    def login(self) -> None:
        """This function is for login."""
        username = self.screen.textinput("What is your username?", "Username")
        password = self.screen.textinput("What is your password?", "Password")
        mail = self.screen.textinput("What is your email?", "Email")
        self.loging = Login(username, password, mail)
        while not self.loging.login():
            ask = self.screen.textinput("Your account doesn't existing.",
                                        "Do you want to register? (y/n): ")
            if ask.lower() == 'y':
                self.loging.register()
                self.any_screen(message="You were a successful registrant.")
            elif ask.lower() == 'n':
                username = self.screen.textinput("What is your username?",
                                                 "Username")
                password = self.screen.textinput("What is your password?",
                                                 "Password")
                mail = self.screen.textinput("What is your email?", "Email")
                self.loging = Login(username, password, mail)
            else:
                self.any_screen("Error", "Wrong input.")
        self.any_screen(message="Login successful.")
        time.sleep(0.75)
        self.menu()

    def register(self) -> None:
        """This function is for register."""
        username = self.screen.textinput("What is your username?", "Username")
        password = self.screen.textinput("What is your password?", "Password")
        mail = self.screen.textinput("What is your email?", "Email")
        self.loging = Login(username, password, mail)
        while self.loging.check_register():
            if not (username and password and mail):
                self.any_screen("Error", "Needed to fill all input.")
            else:
                self.any_screen("Error", "Username already exists.")
            username = self.screen.textinput("What is your username?",
                                             "Username")
            password = self.screen.textinput("What is your password?",
                                             "Password")
            mail = self.screen.textinput("What is your email?", "Email")
            self.loging = Login(username, password, mail)
        self.loging.register()
        self.any_screen(message="You were a successful registrant.")
        time.sleep(0.75)
        self.menu()

    def forget_password(self) -> None:
        """This function is for the user who forget their password."""
        recovery = random.choice(
            ["asdlkco", "iqowejoijao", "cmxlkwemqkm, 'kJSDoxcjwdo",
             "aosjdij123", "1i2u381238ioajds", "jasjnxcjknqw",
             "190827389712389aksljd", "asjhdjxzhclkiveieicc",
             "kxcjoieqjcibqojnew", " 18923798123klsdackmldmklckmldklm",
             "aksdhjlxjcioqjweiojewiojc"])
        username = self.screen.textinput("Recovery", "What is your username?")
        email = self.screen.textinput("Recovery", "What is your mail?")
        with open("user.json", mode="r", encoding="utf-8") as data:
            users = json.load(data)
        if username and email:
            if username in users:
                if email == users[username]["Mail"]:
                    password = users[username]["Password"]
                    self.mail = Mail(Login(username, password, email))
                    self.mail.send_mail(
                        f"This is your recovery code '{recovery}' "
                        f"(not include single quotes).")
                    recovery_code = self.screen.textinput("Recovery",
                                                          "Enter your "
                                                          "recovery code: ")
                    if recovery_code == recovery:
                        new_password = self.screen.textinput("Recovery",
                                                             "Enter your new "
                                                             "password: ")
                        with open("user.json", mode="r",
                                  encoding="utf-8") as data:
                            users = json.load(data)
                        users[username]["Password"] = new_password
                        with open("user.json", mode="w",
                                  encoding="utf-8") as data:
                            json.dump(users, data, indent=4)
                        self.any_screen("Recovery",
                                        "Your password was changed.")
                        self.loging = Login(username, new_password, email)
                        self.menu()
                    else:
                        self.any_screen("Error", "Wrong recovery code.")
                        time.sleep(1.5)
                        self.init_screen("mate", "background/main.png")
                        self.login_register_button()
                else:
                    self.any_screen("Error", "Wrong email.")
                    time.sleep(1.5)
                    self.init_screen("mate", "background/main.png")
                    self.login_register_button()

            else:
                self.any_screen("Error", "Not found your username.")
                time.sleep(1.5)
                self.init_screen("mate", "background/main.png")
                self.login_register_button()

        else:
            self.any_screen("Error", "Needed to fill all input.")
            time.sleep(1.5)
            self.init_screen("mate", "background/main.png")
            self.login_register_button()

    # Screen
    def init_screen(self, title: str, background: str) -> None:
        """This function is for init the screen."""
        self.writer.clear()
        self.writer.hideturtle()
        self.writer.penup()
        self.screen.title(title)
        self.screen.setup(900, 600)
        self.screen.bgpic(background)
        self.screen.tracer(0)

    def menu(self) -> None:
        """This function is for menu."""
        self.writer.clear()
        self.init_screen("Menu", "background/menu.png")
        self.menu_button()

    def function_choice(self, func) -> None:
        """This function is for function choice."""
        ask = self.screen.textinput("", "show or exit? (s/e): ")
        if ask:
            while ask.lower() != "e":
                if ask.lower() == "s":
                    self.any_screen("Wish!", func())
                elif ask.lower() == "e":
                    break
                else:
                    self.any_screen("Error", "Wrong input.")
                ask = self.screen.textinput("", "show or exit? (s/e): ")
        else:
            self.any_screen("Error", "Wrong input.")
        self.back_button()

    def any_screen(self, title: str = "", message: str = "",
                   png: str = "background/normal.png") -> None:
        """This function is for any screen."""
        self.init_screen(title, png)
        self.writer.goto(0, 0)
        self.writer.color("brown")
        self.writer.write(message, font=('Arial', 20, 'normal'),
                          align="center")

    def weather_screen(self) -> None:
        """This function is for weather screen."""
        address = self.screen.textinput("Enter your location",
                                        "In any languages.")
        if address:
            geolocator = Nominatim(user_agent="MyApp")
            location = geolocator.geocode(address)
            self.weather = Weather(location.latitude, location.longitude)
            self.any_screen("Done", "Successfully update your location.")
        else:
            self.any_screen("Error", "Something went wrong, using bangkok "
                                     "location instead.")
            self.weather = Weather()
        time.sleep(1.2)
        self.any_screen(png="background/weather.png")
        for index in range(0, 6):
            self.writer.goto(-230, 120 - (index * 30))
            self.writer.write(self.weather.show_weather()[index],
                              font=('Arial', 15, 'normal'))
        for index in range(6, 12):
            self.writer.goto(55, 120 - ((index - 5) * 30))
            self.writer.write(self.weather.show_weather()[index],
                              font=('Arial', 15, 'normal'))
        try:
            self.weather.show_weather()[12]
        except IndexError:
            pass
        else:
            self.screen.textinput("Alert!",
                                  "Don't forget to bring an umbrella!")

    # Click Zone
    def menu_click(self, x_cor: (int, float), y_cor: (int, float)) -> None:
        """This function is for menu click."""
        if -150 <= x_cor <= 150:
            if 75 <= y_cor <= 125:
                self.any_screen(png="background/interest.png")
                self.four_interest_buttons()
                self.screen.onclick(self.four_interest_click)

            # weather
            if 0 <= y_cor <= 50:
                self.any_screen(png="background/weather.png")
                self.weather_screen()
                self.back_button()

            # note
            if -75 <= y_cor <= -25:
                self.any_screen(png="background/note.png")
                note = Note(self.loging)

                self.writer.goto(-200, 100)
                self.writer.write("List of your Note:",
                                  font=('Arial', 25, 'normal'))
                self.writer.goto(-200, 50)
                if note.show_note() != "You don't have any note.":
                    for index, note in enumerate(note.show_note()):
                        self.writer.goto(-200, 50 - (index * 30))
                        self.writer.write(note, font=('Arial', 20, 'normal'))
                else:
                    self.writer.write("You don't have any note.",
                                      font=('Arial', 20, 'normal'))

                self.delete_button(self.delete_click)

            # mail
            if -145 <= y_cor <= -95:
                self.any_screen(png="background/mail.png")
                mails = Mail(self.loging)
                self.writer.goto(-200, 100)
                self.writer.write("List of subscribed topics: ",
                                  font=('Arial', 25, 'normal'))
                if mails.topics_to_send:
                    for index, mail in enumerate(mails.topics_to_send):
                        self.writer.goto(-200, 50 - (index * 30))
                        self.writer.write(mail, font=('Arial', 20, 'normal'))
                else:
                    self.writer.goto(-200, 50)
                    self.writer.write("You don't have any.",
                                      font=('Arial', 20, 'normal'))
                self.mail_button()

        if 180.0 <= x_cor <= 250 and -160.0 <= y_cor <= -110:
            ask = self.screen.textinput("Agree? (y/n)",
                                        "Do you want to delete your "
                                        "account?")
            if ask in "yY":
                password = self.screen.textinput("Confirm."
                                                 "",
                                                 "Fill in your password")
                if password == self.loging.password:
                    self.loging.delete_account()
                    self.any_screen("", "Account deleted.")
                    time.sleep(0.75)
                    self.init_screen("mate", "background/main.png")
                    self.login_register_button()
                else:
                    self.any_screen("", "Wrong password.")
                    self.back_button()

            elif ask in "nN":
                self.any_screen("", "Account not deleted.")
                self.back_button()

            else:
                self.any_screen("", "Wrong input.")
                self.back_button()

    def login_register_click(self, x_cor: (int, float),
                             y_cor: (int, float)) -> None:
        """This function is for login and register click."""
        if -150 <= x_cor <= 150:
            if 0 <= y_cor <= 50:
                self.login()
            if -75 <= y_cor <= -25:
                self.register()
        if 170 <= x_cor <= 250 and -180 <= y_cor <= -110:
            self.forget_password()

    def back_click(self, x_cor: (int, float), y_cor: (int, float)) -> None:
        """This function is for back click."""
        if -316 >= x_cor >= -416.0:
            if -252.0 <= y_cor <= -202.0:
                self.menu()

    def four_interest_click(self, x_cor: (int, float), y_cor: (int, float)) \
            -> None:
        """This function is for four interest click."""
        self.interesting = Interest(self.loging)

        # Eats
        if -225.0 < x_cor < -25.0 and 120 > y_cor > 20:
            self.any_screen("", "Nom nom nom!")
            self.function_choice(self.interesting.show_something_to_eat)

        # Songs
        elif 25 < x_cor < 225 and 120 > y_cor > 20:
            self.any_screen()
            self.writer.goto(-300, 200)
            self.writer.write("List of the songs:",
                              font=('Arial', 25, 'normal'))
            for index, song in enumerate(self.interesting.show_top_10_songs()):
                self.writer.goto(-200, 100 - index * 20)
                self.writer.write(song, font=('Arial', 15, 'normal'))
            self.back_button()

        # News
        elif -225.0 < x_cor < -25.0 and -20 > y_cor > -120:
            self.any_screen()
            self.interesting = Interest(self.loging)
            self.writer.goto(-300, 200)
            self.writer.write("List of your interest:",
                              font=('Arial', 25, 'normal'))
            if self.interesting.interest:
                if len(self.interesting.interest) < 8:
                    for index, interest in enumerate(
                            self.interesting.interest):
                        self.writer.goto(-200, 100 - (index * 30))
                        self.writer.write(interest,
                                          font=('Arial', 20, 'normal'))
                else:
                    for index in range(0, 8):
                        self.writer.goto(-200, 100 - (index * 30))
                        self.writer.write(self.interesting.interest[index],
                                          font=('Arial', 20, 'normal'))
                    for index in range(8, len(self.interesting.interest)):
                        self.writer.goto(80, 100 - ((index - 8) * 30))
                        self.writer.write(self.interesting.interest[index],
                                          font=('Arial', 20, 'normal'))
            else:
                self.any_screen("", "No news found.")
            self.back_button()
            self.change_interest_button("Change", self.change_interest_click)

        # Fortune
        elif 25 < x_cor < 225 and -20 > y_cor > -120:
            self.any_screen("", "Fortune.")
            self.function_choice(self.interesting.show_fortune_telling)
        # Back
        if -316 >= x_cor >= -416.0:
            if -252.0 <= y_cor <= -202.0:
                self.menu()

    def change_interest_click(self, x_cor: (int, float), y_cor: (int, float)) \
            -> None:
        """This function is for change interest click."""
        if 145 < x_cor < 300 and -140 > y_cor > -200:
            self.any_screen()
            self.writer.goto(-300, 200)
            self.writer.write("List of the topics:",
                              font=('Arial', 25, 'normal'))

            for index in range(1, 8):
                self.writer.goto(-230, 120 - (index * 30))
                self.writer.write(
                    f"{index}. {self.interesting.all_toppics[index]}",
                    font=('Arial', 20, 'normal'))
            for index in range(8, 15):
                self.writer.goto(55, 120 - ((index - 7) * 30))
                self.writer.write(
                    f"{index}. {self.interesting.all_toppics[index]}",
                    font=('Arial', 20, 'normal'))

            interest = self.screen.textinput("",
                                             "What kind of news are you "
                                             "interested? type in oneline. "
                                             "(Ex. 1 3 4 11) : ")
            if interest:
                self.interesting.change_interest(interest)
                self.any_screen("Success", "Your interest has been changed.")
            else:
                self.any_screen("Error", "Wrong input.")
            self.back_button()

        self.back_click(x_cor, y_cor)

    def delete_click(self, x_cor: (int, float), y_cor: (int, float)) -> None:
        """This function is for delete click."""

        # Add
        if 145 < x_cor < 300 and -140 > y_cor > -200:
            self.any_screen()
            note = Note(self.loging)
            while True:
                deadline = self.screen.textinput(
                    "", "Enter the deadline date (day/month/year): ")
                if not deadline:
                    self.any_screen("Error", "You must fill in the deadline.")
                    self.back_button()

                elif deadline and deadline.count("/") != 2:
                    self.any_screen("Error", "Wrong format. Try again.")
                    self.back_button()
                else:
                    break

            if deadline:
                notes = self.screen.textinput("", "Enter the note: ")
                if notes:
                    note.add_note(deadline, notes)
                    self.any_screen("", "Note added.")
                    self.back_button()
                else:
                    self.any_screen("Error", "You must fill in the note.")
                    self.back_button()
            else:
                self.any_screen("Error", "You must fill in the deadline.")
                self.back_button()

        # Delete
        if -305 < x_cor < -150 and -140 > y_cor > -200:
            self.any_screen()
            note = Note(self.loging)
            while True:
                deadline = self.screen.textinput(
                    "", "Enter the deadline date (day/month/year): ")
                if not deadline or deadline.count("/") != 2:
                    self.any_screen("", "Wrong format. Try again.")
                    continue
                break
            if note.delete_note(deadline):
                self.any_screen("", "Note deleted.")
            else:
                self.any_screen("", "Note not found.")
            self.back_button()

        self.back_click(x_cor, y_cor)

    def mail_click(self, x_cor: (int, float), y_cor: (int, float)) -> None:
        """This function is for mail click."""

        # add
        mail = Mail(self.loging)
        if 145 < x_cor < 300 and -140 > y_cor > -200:
            self.any_screen()
            self.writer.goto(-260, 150)
            self.writer.color("brown")
            self.writer.write("1.Food - Every morning, one of the menus will "
                              "be delivered to you.",
                              font=('Arial', 15, 'normal'))
            self.writer.goto(-260, 100)
            self.writer.write("2. Song - Every morning, you will receive a "
                              "list of the ten hottest songs right now on "
                              "Billboard.", font=('Arial', 15, 'normal'))

            self.writer.goto(-260, 50)
            self.writer.write("3. Fortune - Every morning, you 'll receive a "
                              "fortune-telling session.",
                              font=('Arial', 15, 'normal'))

            self.writer.goto(-260, 0)
            self.writer.write("4. Weather - Every morning, you will receive "
                              "the weather forecast for the day.",
                              font=('Arial', 15, 'normal'))

            self.writer.goto(-260, -50)
            self.writer.write("5. News - Every morning, one of each of your "
                              "interesting news topics will be delivered "
                              "to you.", font=('Arial', 15, 'normal'))

            self.writer.goto(-260, -100)
            self.writer.write("6. Note - Every morning, you will receive a "
                              "note which has the deadline tomorrow.",
                              font=('Arial', 15, 'normal'))

            self.writer.goto(-260, -150)
            self.writer.write("7. Reset - Reset your topics.",
                              font=('Arial', 15, 'normal'))

            topics = self.screen.textinput("", "Enter the number of topics you"
                                               "are interested in "
                                               "(Ex. 1 3 4):")
            convert_number_to_topic = {1: "Food", 2: "Song", 3: "Fortune",
                                       4: "Weather", 5: "News", 6: "Note",
                                       7: ""}
            if topics:
                topics = [convert_number_to_topic[int(index)] for index in
                          topics.split()]
                mail.change_topics_to_send(topics)
                self.any_screen("", "Topics changed.")
            else:
                self.any_screen("Error", "Wrong input.")
            self.back_button()

        # Send mail
        if -305 < x_cor < -150 and -140 > y_cor > -200:
            self.interesting = Interest(self.loging)
            self.any_screen()
            self.writer.goto(-200, 100)
            self.writer.write("List of subscribed topics: ",
                              font=('Arial', 25, 'normal'))
            for index, news in enumerate(mail.topics_to_send):
                if news != "":
                    self.writer.goto(-200, 100 - (index + 1) * 40)
                    self.writer.color("brown")
                    self.writer.write(f"{index + 1}.{news}",
                                      font=('Arial', 15, 'normal'))
            ask = self.screen.textinput("Agree? (y/n)", f"The information will"
                                                        f" be sent to "
                                                        f"{mail.mymail} "
                                                        f"now are you sure?"
                                                        f"")
            if ask and ask.lower() == "y":
                self.any_screen("", "Mail sent.\n It might take a few "
                                    "minutes.")

                mail.send_mail(mail.create_text(self.interesting,
                                                self.weather).encode('utf-8',
                                                                     'ignore'))
                self.back_button()
            else:
                self.any_screen("", "Mail not sent.")
                self.back_button()
        self.back_click(x_cor, y_cor)


d = Display()
d.init_screen("mate", "background/main.png")
d.login_register_button()
turtle.done()
