import json
import random
import time
from geopy.geocoders import Nominatim
from login import Login
from mail import Mail
from weather import Weather
from button import Button


class Display(Button):
    """This class is for display the whole program."""

    def __init__(self) -> None:
        super().__init__()
        self.logging = None
        self.mail = None
        self.weather = Weather()

    # Login/Register
    def login(self) -> None:
        """This function is for login."""
        username = self.screen.textinput("What is your username?", "Username")
        password = self.screen.textinput("What is your password?", "Password")
        mail = self.screen.textinput("What is your email?", "Email")
        while not (username and password and mail):
            self.any_screen("Error", "Needed to fill all input.")
            username = self.screen.textinput("What is your username?",
                                             "Username")
            password = self.screen.textinput("What is your password?",
                                             "Password")
            mail = self.screen.textinput("What is your email?", "Email")
        self.logging = Login(username, password, mail)
        while not self.logging.login():
            ask = self.screen.textinput("Your account doesn't existing.",
                                        "Do you want to register? (y/n): ")
            if ask.lower() == 'y':
                self.logging.register()
                self.any_screen(message="You were a successful registrant.")
            elif ask.lower() == 'n':
                username = self.screen.textinput("What is your username?",
                                                 "Username")
                password = self.screen.textinput("What is your password?",
                                                 "Password")
                mail = self.screen.textinput("What is your email?", "Email")
                self.logging = Login(username, password, mail)
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
        self.logging = Login(username, password, mail)
        while self.logging.check_register():
            if not (username and password and mail):
                self.any_screen("Error", "Needed to fill all input.")
            else:
                self.any_screen("Error", "Username already exists.")
            username = self.screen.textinput("What is your username?",
                                             "Username")
            password = self.screen.textinput("What is your password?",
                                             "Password")
            mail = self.screen.textinput("What is your email?", "Email")
            self.logging = Login(username, password, mail)
        self.logging.register()
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
                        self.logging = Login(username, new_password, email)
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
                                  "Don't forget to bring an umbrella!")

    def run(self):
        """Run the program."""
        self.init_screen("mate", "background/main.png")
        self.login_register_button()
        self.screen.mainloop()
