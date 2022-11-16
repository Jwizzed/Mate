import turtle
from login import Login
import time
from interest import Interest
from mail import Mail

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

    def init_screen(self, title, bg):
        self.writer.clear()
        self.writer.hideturtle()
        self.writer.penup()
        self.screen.title(title)
        self.screen.setup(900, 600)
        self.screen.bgpic(bg)
        self.screen.tracer(0)

    def login_button(self):
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

    def register_button(self):
        self.writer.goto(0, 0)
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

    def interest_button(self):
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
        self.writer.forward(115)
        self.writer.color("brown")
        self.writer.write("Weather", font=('Arial', 15, 'normal'),
                          align="left")

    def note_button(self):
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.goto(0, 0)
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(Button_x, Button_y - 75)
        self.writer.goto(Button_x + ButtonLength, Button_y - 75)
        self.writer.goto(Button_x + ButtonLength, Button_y - 75 + ButtonWidth)
        self.writer.goto(Button_x, Button_y - 75 + ButtonWidth)
        self.writer.goto(Button_x, Button_y - 75)
        self.writer.end_fill()
        self.writer.goto(Button_x + 7, Button_y - 60)
        self.writer.forward(130)
        self.writer.color("brown")
        self.writer.write("Note", font=('Arial', 15, 'normal'),
                          align="left")

    def weather_button(self):
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.goto(0, 0)
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(Button_x, Button_y + 75)
        self.writer.goto(Button_x + ButtonLength, Button_y + 75)
        self.writer.goto(Button_x + ButtonLength, Button_y + 75 + ButtonWidth)
        self.writer.goto(Button_x, Button_y + 75 + ButtonWidth)
        self.writer.goto(Button_x, Button_y + 75)
        self.writer.end_fill()
        self.writer.goto(Button_x + 7, Button_y + 90)
        self.writer.forward(120)
        self.writer.color("brown")
        self.writer.write("Interest", font=('Arial', 15, 'normal'),
                          align="left")

    def mail_button(self):
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.goto(0, 0)
        self.writer.begin_fill()
        self.writer.color("white")
        self.writer.goto(Button_x, Button_y - 145)
        self.writer.goto(Button_x + ButtonLength, Button_y - 145)
        self.writer.goto(Button_x + ButtonLength, Button_y - 145 + ButtonWidth)
        self.writer.goto(Button_x, Button_y - 145 + ButtonWidth)
        self.writer.goto(Button_x, Button_y - 145)
        self.writer.end_fill()
        self.writer.goto(Button_x + 7, Button_y - 130)
        self.writer.forward(133)
        self.writer.color("brown")
        self.writer.write("Mail", font=('Arial', 15, 'normal'),
                          align="left")

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

    # def inside_interest_button(self):
    #     self.writer.penup()
    #     self.writer.color("white")
    #     self.writer.goto(-416.0, -202.0)
    #     self.writer.begin_fill()
    #     self.writer.goto(-416.0 + 100, -202.0)
    #     self.writer.goto(-416.0 + 100, -252.0)
    #     self.writer.goto(-416.0, -252.0)
    #     self.writer.end_fill()
    #     self.writer.goto(-430.0, -237.0)
    #     self.writer.forward(50)
    #     self.writer.color("brown")
    #     self.writer.write("Back", font=('Arial', 15, 'normal'),
    #                       align="left")

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
        self.screen.onclick(self.menu_click)

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
            self.screen.onclick(self.menu_click)

    # Screen
    def menu(self):
        self.writer.clear()
        self.init_screen("Menu", "background/menu.png")
        self.interest_button()
        self.weather_button()
        self.note_button()
        self.mail_button()


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

    def four_interest_click(self, x, y):
        interesting = Interest(self.loging)
        if -225.0 < x < -25.0 and 120 > y > 20:
            self.any_screen("", "Nom nom nom!")
            self.function_choice(interesting.show_something_to_eat)

        elif -225.0 + 250 < x < -25.0 + 250 and 120 > y > 20:
            self.any_screen("", "Interest")

        elif -225.0 < x < -25.0 and -20 > y > -120:
            number = int(self.screen.textinput("",
                                               "How many news do you want?"))
            interesting.show_bbc_new(interesting.interest, number)
            # make another screen for take interest input
        elif -225.0 + 250 < x < -25.0 + 250 and -20 > y > -120:
            self.any_screen("", "Fortune.")
            self.function_choice(interesting.show_fortune_telling)

        if -416.0 + 100 >= x >= -416.0:
            if -252.0 <= y <= -202.0:
                self.menu()
                self.screen.onclick(self.menu_click)

    def function_choice(self, func):
        ask = self.screen.textinput("",
                                    "Send mail, "
                                    "print or exit? (m/p/e): ").lower()
        while ask != "e":
            if ask == "p":
                self.any_screen("Wish!",
                                func())
            elif ask == "m":
                self.mail = Mail(self.loging)
                self.mail.send_mail(func())
                self.any_screen("Mail", "Mail was sent.")
            elif ask == "e":
                break
            ask = self.screen.textinput("",
                                        "Send mail, "
                                        "print or exit? (m/p/e): ").lower()
            self.back_button()
            self.screen.onclick(d.back_click)

    def any_screen(self, title="", message="", png="background/normal.png"):
        self.init_screen(title, png)
        self.writer.goto(0, 0)
        self.writer.color("brown")
        self.writer.write(message, font=('Arial', 20, 'normal'),
                          align="center")

    # Click Zone
    def menu_click(self, x, y):
        if Button_x + ButtonLength >= Button_x <= x:
            if Button_y + 75 <= y <= Button_y + 75 + ButtonWidth:
                self.any_screen(png="background/interest.png")
                self.four_interest_buttons()
                self.screen.onclick(self.four_interest_click)

            if Button_y <= y <= Button_y + ButtonWidth:
                self.any_screen(png="background/weather.png")
                self.back_button()
                self.screen.onclick(self.back_click)
            if Button_y - 75 <= y <= Button_y - 75 + ButtonWidth:
                self.any_screen(png="background/note.png")
                self.back_button()
                self.screen.onclick(self.back_click)
            if Button_y - 145 <= y <= Button_y - 145 + ButtonWidth:
                self.any_screen(png="background/mail.png")
                self.back_button()
                self.screen.onclick(self.back_click)


    def login_register_click(self, x, y):
        if Button_x + ButtonLength >= Button_x <= x:
            if Button_y <= y <= Button_y + ButtonWidth:
                self.login()
            if Button_y - 75 <= y <= Button_y - 75 + ButtonWidth:
                self.register()

    def back_click(self, x, y):
        if -416.0 + 100 >= x >= -416.0:
            if -252.0 <= y <= -202.0:
                self.menu()
                self.screen.onclick(self.menu_click)


def get_mouse_click_coor(x, y):
    print(x, y)


d = Display()
d.init_screen("mate", "background/main.png")
d.login_button()
d.register_button()

d.screen.onclick(d.login_register_click)

# turtle.onscreenclick(get_mouse_click_coor)


turtle.done()
