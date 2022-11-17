import turtle
from login import Login
import time
from interest import Interest
from mail import Mail
from weather import Weather
from note import Note

Button_x = -150
Button_y = 0
ButtonLength = 300
ButtonWidth = 50


class Display:
    def __init__(self):
        self.writer = turtle.Pen()
        self.screen = turtle.Screen()
        self.loging = None
        self.mail = None
        self.interesting = None

    def init_screen(self, title, bg):
        self.writer.clear()
        self.writer.hideturtle()
        self.writer.penup()
        self.screen.title(title)
        self.screen.setup(900, 600)
        self.screen.bgpic(bg)
        self.screen.tracer(0)

    def login_register_button(self):
        # login button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(Button_x, Button_y)
        self.writer.goto(Button_x + ButtonLength, Button_y)
        self.writer.goto(Button_x + ButtonLength, Button_y + ButtonWidth)
        self.writer.goto(Button_x, Button_y + ButtonWidth)
        self.writer.goto(Button_x, Button_y)
        self.writer.end_fill()
        self.writer.goto(Button_x + 15, Button_y + 15)
        self.writer.forward(117)
        self.writer.color("brown")
        self.writer.write("Login", font=('Arial', 15, 'normal'), align="left")
        # register button
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(Button_x, Button_y - 75)
        self.writer.goto(Button_x + ButtonLength, Button_y - 75)
        self.writer.goto(Button_x + ButtonLength, Button_y - 75 + ButtonWidth)
        self.writer.goto(Button_x, Button_y - 75 + ButtonWidth)
        self.writer.goto(Button_x, Button_y - 75)
        self.writer.end_fill()
        self.writer.goto(Button_x + 7, Button_y - 60)
        self.writer.forward(117)
        self.writer.color("brown")
        self.writer.write("Register", font=('Arial', 15, 'normal'),
                          align="left")
        self.screen.onclick(self.login_register_click)

    def menu_button(self):
        # weather button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(Button_x, Button_y)
        self.writer.goto(Button_x + ButtonLength, Button_y)
        self.writer.goto(Button_x + ButtonLength, Button_y + ButtonWidth)
        self.writer.goto(Button_x, Button_y + ButtonWidth)
        self.writer.goto(Button_x, Button_y)
        self.writer.end_fill()
        self.writer.goto(Button_x + 130, Button_y + 15)
        self.writer.color("brown")
        self.writer.write("Weather", font=('Arial', 15, 'normal'),
                          align="left")
        # note button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(Button_x, Button_y - 75)
        self.writer.goto(Button_x + ButtonLength, Button_y - 75)
        self.writer.goto(Button_x + ButtonLength, Button_y - 75 + ButtonWidth)
        self.writer.goto(Button_x, Button_y - 75 + ButtonWidth)
        self.writer.goto(Button_x, Button_y - 75)
        self.writer.end_fill()
        self.writer.goto(Button_x + 137, Button_y - 60)
        self.writer.color("brown")
        self.writer.write("Note", font=('Arial', 15, 'normal'),
                          align="left")
        # interest button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(Button_x, Button_y + 75)
        self.writer.goto(Button_x + ButtonLength, Button_y + 75)
        self.writer.goto(Button_x + ButtonLength, Button_y + 75 + ButtonWidth)
        self.writer.goto(Button_x, Button_y + 75 + ButtonWidth)
        self.writer.goto(Button_x, Button_y + 75)
        self.writer.end_fill()
        self.writer.goto(Button_x + 127, Button_y + 90)
        self.writer.color("brown")
        self.writer.write("Interest", font=('Arial', 15, 'normal'),
                          align="left")
        # mail button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(Button_x, Button_y - 145)
        self.writer.goto(Button_x + ButtonLength, Button_y - 145)
        self.writer.goto(Button_x + ButtonLength, Button_y - 145 + ButtonWidth)
        self.writer.goto(Button_x, Button_y - 145 + ButtonWidth)
        self.writer.goto(Button_x, Button_y - 145)
        self.writer.end_fill()
        self.writer.goto(Button_x + 140, Button_y - 130)
        self.writer.color("brown")
        self.writer.write("Mail", font=('Arial', 15, 'normal'),
                          align="left")
        self.screen.onclick(self.menu_click)

    def back_button(self):
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(-416.0, -202.0)
        self.writer.begin_fill()
        self.writer.goto(-416.0 + 100, -202.0)
        self.writer.goto(-416.0 + 100, -252.0)
        self.writer.goto(-416.0, -252.0)
        self.writer.end_fill()
        self.writer.goto(-430.0, -237.0)
        self.writer.forward(50)
        self.writer.color("white")
        self.writer.write("Back", font=('Arial', 15, 'normal'),
                          align="left")
        self.screen.onclick(self.back_click)

    def change_interest_button(self, msg, func):
        # add interest button
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(145, -140)
        self.writer.begin_fill()
        self.writer.goto(300, -140)
        self.writer.goto(300, -200)
        self.writer.goto(145, -200)
        self.writer.end_fill()
        self.writer.goto(210-len(msg)-10, -180)
        self.writer.color("white")
        self.writer.write(msg, font=('Arial', 15, 'normal'),
                          align="left")
        # back button
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(-416.0, -202.0)
        self.writer.begin_fill()
        self.writer.goto(-416.0 + 100, -202.0)
        self.writer.goto(-416.0 + 100, -252.0)
        self.writer.goto(-416.0, -252.0)
        self.writer.end_fill()
        self.writer.goto(-430.0, -237.0)
        self.writer.forward(50)
        self.writer.color("white")
        self.writer.write("Back", font=('Arial', 15, 'normal'),
                          align="left")
        self.screen.onclick(func)

    def four_interest_buttons(self):
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
        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(-225.0 + 250, 120)
        self.writer.begin_fill()
        self.writer.goto(-25.0 + 250, 120)
        self.writer.goto(-25.0 + 250, 20)
        self.writer.goto(-225 + 250, 20)
        self.writer.end_fill()
        self.writer.goto(-190 + 250, 65)
        self.writer.forward(45)
        self.writer.color("white")
        self.writer.write("Songs", font=('Arial', 15, 'normal'),
                          align="left")

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

        self.writer.penup()
        self.writer.color("brown")
        self.writer.goto(-225.0 + 250, -20)
        self.writer.begin_fill()
        self.writer.goto(-25.0 + 250, -20)
        self.writer.goto(-25.0 + 250, -120)
        self.writer.goto(-225 + 250, -120)
        self.writer.end_fill()
        self.writer.goto(-190 + 250, -80)
        self.writer.forward(40)
        self.writer.color("white")
        self.writer.write("Fortune", font=('Arial', 15, 'normal'),
                          align="left")

    # Login/Register
    def login(self) -> None:
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

    def register(self):
        username = self.screen.textinput("What is your username?", "Username")
        password = self.screen.textinput("What is your password?", "Password")
        mail = self.screen.textinput("What is your email?", "Email")
        do = 0
        while not (username or password or mail):
            self.any_screen("Error", "Needed to fill all input.")
            username = self.screen.textinput("What is your username?",
                                             "Username")
            password = self.screen.textinput("What is your password?",
                                             "Password")
            mail = self.screen.textinput("What is your email?", "Email")

        self.loging = Login(username, password, mail)
        if not self.loging.check_register():
            self.any_screen("Error", "Username is already used.")
            self.register()
        else:
            do += 1
        if do == 1:
            self.loging.register()
            self.any_screen(message="You were a successful registrant.")
            time.sleep(0.75)
            self.menu()

    # Screen
    def menu(self):
        self.writer.clear()
        self.init_screen("Menu", "background/menu.png")
        self.menu_button()

    def function_choice(self, func):
        ask = self.screen.textinput("", "show or exit? (s/e): ").lower()
        while ask != "e":
            if ask == "s":
                self.any_screen("Wish!", func())
            elif ask == "e":
                break
            else:
                self.any_screen("Error", "Wrong input.")
            ask = self.screen.textinput("", "show or exit? (s/e): ").lower()
        self.back_button()

    def any_screen(self, title="", message="", png="background/normal.png"):
        self.init_screen(title, png)
        self.writer.goto(0, 0)
        self.writer.color("brown")
        self.writer.write(message, font=('Arial', 20, 'normal'),
                          align="center")

    def weather_screen(self):
        weather = Weather()
        for index in range(0, 6):
            self.writer.goto(-230, 120 - (index * 30))
            self.writer.write(weather.show_weather()[index],
                              font=('Arial', 15, 'normal'))
        for index in range(6, 12):
            self.writer.goto(55, 120 - ((index - 5) * 30))
            self.writer.write(weather.show_weather()[index],
                              font=('Arial', 15, 'normal'))
        try:
            weather.show_weather()[12]
        except:
            pass
        else:
            self.screen.textinput("Alert!",
                                  "Don't forget to bring an umbrella!")

    # Click Zone
    def menu_click(self, x, y):
        if Button_x + ButtonLength >= Button_x <= x:
            if Button_y + 75 <= y <= Button_y + 75 + ButtonWidth:
                self.any_screen(png="background/interest.png")
                self.four_interest_buttons()
                self.screen.onclick(self.four_interest_click)

            if Button_y <= y <= Button_y + ButtonWidth:
                self.any_screen(png="background/weather.png")
                self.weather_screen()
                self.back_button()

            if Button_y - 75 <= y <= Button_y - 75 + ButtonWidth:
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
                self.change_interest_button("Add note", self.add_note_click)


            if Button_y - 145 <= y <= Button_y - 145 + ButtonWidth:
                self.any_screen(png="background/mail.png")
                self.back_button()

    def login_register_click(self, x, y):
        if Button_x + ButtonLength >= Button_x <= x:
            if Button_y <= y <= Button_y + ButtonWidth:
                self.login()
            if Button_y - 75 <= y <= Button_y - 75 + ButtonWidth:
                self.register()

    def add_note_click(self, x, y):
        if 145 < x < 300 and -140 > y > -200:
            self.any_screen("", "")
            note = Note(self.loging)
            while True:
                deadline = self.screen.textinput(
                    "", "Enter the deadline date (day/month/year): ")
                if deadline.count("/") != 2:
                    print("Wrong format. Try again.")
                    continue
                else:
                    break

            notes = self.screen.textinput("", "Enter the note: ")
            note.add_note(deadline, notes)
            self.any_screen("", "Note added.")
        self.back_button()

    def back_click(self, x, y):
        if -416.0 + 100 >= x >= -416.0:
            if -252.0 <= y <= -202.0:
                self.menu()

    def four_interest_click(self, x, y):
        self.interesting = Interest(self.loging)
        # Eats
        if -225.0 < x < -25.0 and 120 > y > 20:
            self.any_screen("", "Nom nom nom!")
            self.function_choice(self.interesting.show_something_to_eat)

        # Songs
        elif -225.0 + 250 < x < -25.0 + 250 and 120 > y > 20:
            self.any_screen("", "")
            self.writer.goto(-300, 200)
            self.writer.write("List of the songs:",
                              font=('Arial', 25, 'normal'))
            for index, song in enumerate(self.interesting.show_top_10_songs()):
                self.writer.goto(-200, 100 - index * 20)
                self.writer.write(song, font=('Arial', 15, 'normal'))
            self.back_button()


        # News
        elif -225.0 < x < -25.0 and -20 > y > -120:
            self.any_screen("", "")
            self.interesting = Interest(self.loging)
            self.writer.goto(-300, 200)
            self.writer.write("List of your interest:",
                              font=('Arial', 25, 'normal'))
            if self.interesting.interest:
                for index, interest in enumerate(self.interesting.interest):
                    self.writer.goto(-200, 100 - (index * 30))
                    self.writer.write(interest, font=('Arial', 20, 'normal'))
            else:
                self.any_screen("", "No news found.")
            self.back_button()
            self.change_interest_button("Change", self.change_interest_click)


        # Fortune
        elif -225.0 + 250 < x < -25.0 + 250 and -20 > y > -120:
            self.any_screen("", "Fortune.")
            self.function_choice(self.interesting.show_fortune_telling)
        # Back
        if -416.0 + 100 >= x >= -416.0:
            if -252.0 <= y <= -202.0:
                self.menu()

    def change_interest_click(self, x, y):
        if 145 < x < 300 and -140 > y > -200:
            self.any_screen("", "")
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
                                             "(Eg. 1 3 4 11) : ")

            self.interesting.change_interest(interest)
            self.back_button()

        if -416.0 + 100 >= x >= -416.0:
            if -252.0 <= y <= -202.0:
                self.menu()


def get_mouse_click_coor(x, y):
    print(x, y)


d = Display()
d.init_screen("mate", "background/main.png")
d.login_register_button()

# turtle.onscreenclick(get_mouse_click_coor)


turtle.done()
