import json
import random
import time
from geopy.geocoders import Nominatim
from playsound import playsound
from button import Button
from interest import Interest
from login import Login
from mail import Mail
from note import Note
from weather import Weather


class Display(Button):
    """This class is for display the whole program."""

    def __init__(self) -> None:
        super().__init__()
        self.logging = None
        self.mail = None
        self.interesting = None
        self.weather = Weather()

    # Login/Register
    def login(self) -> None:
        """This function is for login."""
        username = input("What is your username?: ")
        password = input("What is your password?: ")
        mail = input("What is your email?: ")
        while not username or (not password) or (not mail):
            print("Error", "Needed to fill all input.")
            username = input("What is your username?: ")
            password = input("What is your password?: ")
            mail = input("What is your email?: ")
        self.logging = Login(username, password, mail)
        while not self.logging.login():
            ask = input("Your account doesn't existing. "
                        "Do you want to register? (y/n): ")
            if ask.lower() == 'y':
                self.logging.register()
                print("You were a successful registrant.")
            elif ask.lower() == 'n':
                username = input("What is your username?: ")
                password = input("What is your password?: ")
                mail = input("What is your email?: ")
                self.logging = Login(username, password, mail)
            else:
                print("Wrong input.")
        print("Login successful.")
        time.sleep(0.75)
        self.menu()

    def register(self) -> None:
        """This function is for register."""
        username = input("What is your username?: ")
        password = input("What is your password?: ")
        mail = input("What is your email?: ")
        self.logging = Login(username, password, mail)
        while self.logging.check_register():
            if not username or (not password) or (not mail):
                print("Needed to fill all input.")
            else:
                print("Username already exists.")
            username = input("What is your username?: ")
            password = input("What is your password?: ")
            mail = input("What is your email?: ")
            self.logging = Login(username, password, mail)
        self.logging.register()
        print("You were a successful registrant.")
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
        username = input("What is your username?: ")
        email = input("What is your email?: ")
        with open("user.json", mode="r", encoding="utf-8") as data:
            users = json.load(data)
        if username and email:
            if username in users:
                if email == users[username]["Mail"]:
                    password = users[username]["Password"]
                    self.mail = Mail(Login(username, password, email))
                    self.mail.send_mail(f"This is your "
                                        f"recovery code '{recovery}' "
                                        f"(not include single quotes).")
                    recovery_code = input("Enter your recovery code: ")
                    if recovery_code == recovery:
                        new_password = input("Enter your new password: ")
                        with open("user.json", mode="r",
                                  encoding="utf-8") as data:
                            users = json.load(data)
                        users[username]["Password"] = new_password
                        with open("user.json", mode="w",
                                  encoding="utf-8") as data:
                            json.dump(users, data, indent=4)
                        print("Your password was changed.")
                        self.logging = Login(username, new_password, email)
                        self.menu()
                    else:
                        print("Error", "Wrong recovery code.")
                        time.sleep(1.5)
                        self.init_screen("mate", "background/main.png")
                        self.login_register_button()
                        self.screen.onclick(self.login_register_click)
                else:
                    print("Error", "Wrong email.")
                    time.sleep(1.5)
                    self.init_screen("mate", "background/main.png")
                    self.login_register_button()
                    self.screen.onclick(self.login_register_click)

            else:
                print("Error", "Not found your username.")
                time.sleep(1.5)
                self.init_screen("mate", "background/main.png")
                self.login_register_button()
                self.screen.onclick(self.login_register_click)

        else:
            print("Error", "Needed to fill all input.")
            time.sleep(1.5)
            self.init_screen("mate", "background/main.png")
            self.login_register_button()
            self.screen.onclick(self.login_register_click)

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
        self.screen.onclick(self.menu_click)

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
        self.screen.onclick(self.back_click)

    def any_screen(self, title: str = "", message: str = "",
                   png: str = "background/normal.png") -> None:
        """This function is for any screen."""
        self.init_screen(title, png)
        self.writer.goto(0, 0)
        self.writer.color("#315d79")
        self.writer.write(message, font=('Comic Sans MS', 20, 'normal'),
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
        self.any_screen("Weather", png="background/weather.png")
        for index in range(0, 6):
            self.writer.goto(-230, 120 - (index * 30))
            show_weather = self.weather.get_weather()[index]
            if "not" in show_weather:
                self.writer.write(show_weather,
                                  font=('Comic Sans MS', 15, 'normal'))
            else:
                self.writer.color("red")
                self.writer.write(show_weather,
                                  font=('Comic Sans MS', 15, 'normal'))
                self.writer.color("#315d79")

        for index in range(6, 12):
            self.writer.goto(55, 120 - ((index - 5) * 30))
            show_weather = self.weather.get_weather()[index]
            if "not" in show_weather:
                self.writer.write(show_weather,
                                  font=('Comic Sans MS', 15, 'normal'))
            else:
                self.writer.color("red")
                self.writer.write(show_weather,
                                  font=('Comic Sans MS', 15, 'normal'))
                self.writer.color("#315d79")
        try:
            self.weather.get_weather()[12]
        except IndexError:
            pass
        else:
            self.screen.textinput("Alert!",
                                  "Good luck!!")

    def menu_click(self, x_cor: (int, float), y_cor: (int, float)) -> None:
        """This function is for menu click."""
        if -150 <= x_cor <= 150:
            if 75 <= y_cor <= 125:
                playsound("background/click.mp3")
                self.any_screen("Interest", png="background/interest.png")
                self.interest_menu_buttons()
                self.screen.onclick(self.interest_menu_click)

            # weather
            if 0 <= y_cor <= 50:
                playsound("background/click.mp3")
                self.any_screen("Weather", png="background/weather.png")
                self.weather_screen()
                self.back_button()
                self.screen.onclick(self.back_click)

            # note
            if -75 <= y_cor <= -25:
                playsound("background/click.mp3")
                self.any_screen("Note", png="background/note.png")
                note = Note(self.logging)

                self.writer.goto(-200, 100)
                self.writer.write("List of your Note:",
                                  font=('Comic Sans MS', 25, 'normal'))
                self.writer.goto(-200, 50)
                if note.get_note() != "You don't have any note.":
                    for index, note in enumerate(note.get_note()):
                        self.writer.goto(-200, 50 - (index * 30))
                        self.writer.write(note,
                                          font=(
                                              'Comic Sans MS', 20,
                                              'normal'))
                else:
                    self.writer.write("You don't have any note.",
                                      font=('Comic Sans MS', 20, 'normal'))

                self.delete_button(self.delete_click)

            # mail
            if -145 <= y_cor <= -95:
                playsound("background/click.mp3")
                self.any_screen("Mail", png="background/mail.png")
                mails = Mail(self.logging)
                self.writer.goto(-200, 100)
                self.writer.write("List of subscribed topics: ",
                                  font=('Comic Sans MS', 25, 'normal'))
                if mails.topics_to_send:
                    for index, mail in enumerate(mails.topics_to_send):
                        self.writer.goto(-200, 50 - (index * 30))
                        self.writer.write(mail,
                                          font=(
                                              'Comic Sans MS', 20,
                                              'normal'))
                else:
                    self.writer.goto(-200, 50)
                    self.writer.write("You don't have any.",
                                      font=('Comic Sans MS', 20, 'normal'))
                self.mail_button()
                self.change_interest_button("Change        ", self.mail_click)

        if 180.0 <= x_cor <= 250 and -160.0 <= y_cor <= -110:
            playsound("background/click.mp3")
            ask = self.screen.textinput("Agree? (y/n)",
                                        "Do you want to delete your "
                                        "account?")
            if ask:
                if ask in "yY":
                    password = self.screen.textinput("Confirm."
                                                     "",
                                                     "Fill in your password")
                    if password == self.logging.password:
                        self.logging.delete_account()
                        self.any_screen("Delete", "Account deleted.")
                        time.sleep(0.75)
                        self.init_screen("mate", "background/main.png")
                        self.login_register_button()
                        self.screen.onclick(self.login_register_click)
                    else:
                        self.any_screen("Error", "Wrong password.")
                        self.back_button()
                        self.screen.onclick(self.back_click)

                elif ask in "nN":
                    self.any_screen("Not delete", "Account not deleted.")
                    self.back_button()
                    self.screen.onclick(self.back_click)

                else:
                    self.any_screen("Error", "Wrong input.")
                    self.back_button()
                    self.screen.onclick(self.back_click)
            else:
                self.any_screen("Error", "Wrong input.")
                self.back_button()
                self.screen.onclick(self.back_click)

    def login_register_click(self, x_cor: (int, float),
                             y_cor: (int, float)) -> None:
        """This function is for login and register click."""
        if -150 <= x_cor <= 150:
            if 0 <= y_cor <= 50:
                playsound("background/click.mp3")
                self.login()
            if -75 <= y_cor <= -25:
                playsound("background/click.mp3")
                self.register()
        if 170 <= x_cor <= 250 and -180 <= y_cor <= -110:
            playsound("background/click.mp3")
            self.forget_password()

    def back_click(self, x_cor: (int, float), y_cor: (int, float)) -> None:
        """This function is for back click."""
        if -316 >= x_cor >= -416.0 and -252.0 <= y_cor <= -202.0:
            playsound("background/click.mp3")
            self.menu()

    def interest_menu_click(self, x_cor: (int, float), y_cor: (int, float)) \
            -> None:
        """This function is for four interest click."""
        self.interesting = Interest(self.logging)

        # Eats
        if -225.0 < x_cor < -25.0 and 120 > y_cor > 20:
            playsound("background/click.mp3")
            self.any_screen("Eat", "Nom nom nom!")
            self.function_choice(self.interesting.get_something_to_eat)

        # Songs
        elif 25 < x_cor < 225 and 120 > y_cor > 20:
            playsound("background/click.mp3")
            self.any_screen()
            self.writer.goto(-300, 200)
            self.writer.write("List of the songs:",
                              font=('Comic Sans MS', 25, 'normal'))
            for index, song in enumerate(
                    self.interesting.get_top_10_songs()):
                self.writer.goto(-200, 100 - index * 20)
                self.writer.write(song,
                                  font=('Comic Sans MS', 15, 'normal'))
            self.back_button()
            self.screen.onclick(self.back_click)

        # News
        elif -225.0 < x_cor < -25.0 and -20 > y_cor > -120:
            playsound("background/click.mp3")
            self.any_screen()
            self.interesting = Interest(self.logging)
            self.writer.goto(-300, 200)
            self.writer.write("List of your interest:",
                              font=('Comic Sans MS', 25, 'normal'))
            if self.interesting.interest:
                if len(self.interesting.interest) < 8:
                    for index, interest in enumerate(
                            self.interesting.interest):
                        self.writer.goto(-200, 100 - (index * 30))
                        self.writer.write(interest,
                                          font=(
                                              'Comic Sans MS', 20,
                                              'normal'))
                else:
                    for index in range(0, 8):
                        self.writer.goto(-200, 100 - (index * 30))
                        self.writer.write(self.interesting.interest[index],
                                          font=(
                                              'Comic Sans MS', 20,
                                              'normal'))
                    for index in range(8, len(self.interesting.interest)):
                        self.writer.goto(80, 100 - ((index - 8) * 30))
                        self.writer.write(self.interesting.interest[index],
                                          font=(
                                              'Comic Sans MS', 20,
                                              'normal'))
            else:
                self.any_screen("News", "No news found.")
            self.back_button()
            self.change_interest_button("Change",
                                        self.change_interest_click)

        # Fortune
        elif 25 < x_cor < 225 and -20 > y_cor > -120:
            playsound("background/click.mp3")
            self.any_screen("Fortune.", "Fortune.")
            self.function_choice(self.interesting.get_fortune_telling)
        # Back
        if -316 >= x_cor >= -416.0 and -252.0 <= y_cor <= -202.0:
            playsound("background/click.mp3")
            self.menu()

    def change_interest_click(self, x_cor: (int, float),
                              y_cor: (int, float)) -> None:
        """This function is for change interest click."""
        if 145 < x_cor < 300 and -140 > y_cor > -200:
            playsound("background/click.mp3")
            self.any_screen()
            self.writer.goto(-300, 200)
            self.writer.write("List of the topics:",
                              font=('Comic Sans MS', 25, 'normal'))

            for index in range(1, 8):
                self.writer.goto(-230, 120 - (index * 30))
                self.writer.write(
                    f"{index}. {self.interesting.all_toppics[index]}",
                    font=('Comic Sans MS', 20, 'normal'))
            for index in range(8, 15):
                self.writer.goto(55, 120 - ((index - 7) * 30))
                self.writer.write(
                    f"{index}. {self.interesting.all_toppics[index]}",
                    font=('Comic Sans MS', 20, 'normal'))

            interest = self.screen.textinput("",
                                             "What kind of news are you "
                                             "interested? type in oneline. "
                                             "(Ex. 1 3 4 11) : ")
            if interest:
                self.interesting.change_interest(interest)
                self.any_screen("Success",
                                "Your interest has been changed.")
            else:
                self.any_screen("Error", "Wrong input.")
            self.back_button()
            self.screen.onclick(self.back_click)

        self.back_click(x_cor, y_cor)

    def delete_click(self, x_cor: (int, float), y_cor: (int, float)) -> None:
        """This function is for delete click."""
        # Add Note
        if 145 < x_cor < 300 and -140 > y_cor > -200:
            playsound("background/click.mp3")
            self.any_screen()
            note = Note(self.logging)
            if isinstance(note.get_note(), list) and \
                    len(note.get_note()) >= 7:
                ask = self.screen.textinput("",
                                            "You can only add up to "
                                            "7 notes. Do you want to "
                                            "delete note? (y/n): ")
                if ask:
                    if ask.lower() == "y":
                        self.delete_note()
                    elif ask.lower() == "n":
                        self.any_screen("Note", "You can't add more ")
                        self.back_button()
                        self.screen.onclick(self.back_click)
                else:
                    self.any_screen("Note", "You can't add more ")
                    self.back_button()
                    self.screen.onclick(self.back_click)
            else:
                while True:
                    deadline = self.screen.textinput(
                        "", "Enter the deadline date (day/month/year): ")
                    current_date = int(time.strftime("%Y%m%d", time.localtime()))
                    date = int(''.join(i.rjust(2, "0") for i in deadline.split("/")[::-1]))
                    if not deadline:
                        self.any_screen("Error",
                                        "You must fill in the deadline.")

                    elif deadline and deadline.count("/") != 2:
                        self.any_screen("Error", "Wrong format. Try again.")
                    elif date < current_date:
                        self.any_screen("Error", "Can't record the past.")
                    else:
                        break
                    self.back_button()
                    self.screen.onclick(self.back_click)

                if deadline:
                    notes = self.screen.textinput("!", "Enter the note: ")
                    if notes:
                        note.add_note(deadline, notes)
                        self.any_screen("Success", "Note added.")
                        self.back_button()
                        self.screen.onclick(self.back_click)
                    else:
                        self.any_screen("Error",
                                        "You must fill in the note.")
                        self.back_button()
                        self.screen.onclick(self.back_click)
                else:
                    self.any_screen("Error",
                                    "You must fill in the deadline.")
                    self.back_button()
                    self.screen.onclick(self.back_click)

        # Delete Note
        if -305 < x_cor < -150 and -140 > y_cor > -200:
            playsound("background/click.mp3")
            self.delete_note()
        self.back_click(x_cor, y_cor)

    def delete_note(self) -> None:
        """This function is for delete note."""
        self.any_screen()
        note = Note(self.logging)
        while True:
            deadline = self.screen.textinput(
                "", "Enter the deadline date (day/month/year): ")
            if not deadline or deadline.count("/") != 2:
                self.any_screen("Error", "Note not found.")
                break
            if note.delete_note(deadline):
                self.any_screen("Success", "Note deleted.")
            else:
                self.any_screen("Error", "Note not found.")
                break
        self.back_button()
        self.screen.onclick(self.back_click)

    def mail_click(self, x_cor: (int, float), y_cor: (int, float)) -> None:
        """This function is for mail click."""
        # add
        mail = Mail(self.logging)
        if 145 < x_cor < 300 and -140 > y_cor > -200:
            playsound("background/click.mp3")
            self.any_screen()
            self.writer.goto(-260, 150)
            self.writer.color("#315d79")
            self.writer.write(
                "1.Food - Every morning, one of the menus will "
                "be delivered to you.",
                font=('Comic Sans MS', 15, 'normal'))
            self.writer.goto(-260, 100)
            self.writer.write(
                "2. Song - Every morning, you will receive a "
                "list of the ten hottest songs right now on "
                "Billboard.",
                font=('Comic Sans MS', 15, 'normal'))

            self.writer.goto(-260, 50)
            self.writer.write(
                "3. Fortune - Every morning, you 'll receive a "
                "fortune-telling session.",
                font=('Comic Sans MS', 15, 'normal'))

            self.writer.goto(-260, 0)
            self.writer.write(
                "4. Weather - Every morning, you will receive "
                "the weather forecast for the day.",
                font=('Comic Sans MS', 15, 'normal'))

            self.writer.goto(-260, -50)
            self.writer.write(
                "5. News - Every morning, one of each of your "
                "interesting news topics will be delivered "
                "to you.", font=('Comic Sans MS', 15, 'normal'))

            self.writer.goto(-260, -100)
            self.writer.write(
                "6. Note - Every morning, you will receive a "
                "note which has the deadline tomorrow.",
                font=('Comic Sans MS', 15, 'normal'))

            self.writer.goto(-260, -150)
            self.writer.write("7. Reset - Reset your topics.",
                              font=('Comic Sans MS', 15, 'normal'))

            topics = self.screen.textinput("",
                                           "Enter the number of topics you"
                                           "are interested in "
                                           "(Ex. 1 3 4):")
            convert_number_to_topic = {1: "Food", 2: "Song", 3: "Fortune",
                                       4: "Weather", 5: "News", 6: "Note",
                                       7: ""}
            if topics:
                topics = [convert_number_to_topic[int(index)] for index in
                          topics.split()]
                mail.change_topics_to_send(topics)
                self.any_screen("Success", "Topics changed.")
            else:
                self.any_screen("Error", "Wrong input.")
            self.back_button()
            self.screen.onclick(self.back_click)

        # Send mail
        if -305 < x_cor < -150 and -140 > y_cor > -200:
            playsound("background/click.mp3")
            self.interesting = Interest(self.logging)
            self.any_screen()
            self.writer.goto(-200, 100)
            self.writer.write("List of subscribed topics: ",
                              font=('Comic Sans MS', 25, 'normal'))
            for index, news in enumerate(mail.topics_to_send):
                if news != "":
                    self.writer.goto(-200, 100 - (index + 1) * 40)
                    self.writer.color("#315d79")
                    self.writer.write(f"{index + 1}.{news}",
                                      font=('Comic Sans MS', 15, 'normal'))
            ask = self.screen.textinput("Agree? (y/n)",
                                        f"The information will"
                                        f" be sent to "
                                        f"{mail.mymail} "
                                        f"now are you sure?"
                                        f"")
            if ask and ask.lower() == "y":
                self.any_screen("Success",
                                "Mail sent.\n It might take a few "
                                "minutes.")

                mail.send_mail(mail.create_text_to_send(self.interesting,
                                                        self.weather))
                self.back_button()
                self.screen.onclick(self.back_click)
            else:
                self.any_screen("Mail", "Mail not sent.")
                self.back_button()
                self.screen.onclick(self.back_click)
        self.back_click(x_cor, y_cor)

    def secret_command(self):
        """This function is for sending all user's mail at once."""
        with open('user.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
            for user, value in users.items():
                if value["Mail"] and "@" in value["Mail"]:
                    self.logging = Login(user, value["Password"],
                                         value["Mail"])
                    mail = Mail(self.logging)
                    self.interesting = Interest(self.logging)
                    mail.send_mail(mail.create_text_to_send(self.interesting,
                                                            self.weather))

    def run(self):
        """Run the program."""
        self.init_screen("mate", "background/main.png")
        self.login_register_button()
        self.screen.onclick(self.login_register_click)
        self.screen.mainloop()
