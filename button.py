import turtle


class Button:
    def __init__(self):
        self.writer = turtle.Pen()
        self.screen = turtle.Screen()

    def login_register_button(self) -> None:
        """This function is for login and register button."""
        # login button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("#315d79")
        self.writer.goto(-150, 0)
        self.writer.goto(150, 0)
        self.writer.goto(150, 50)
        self.writer.goto(-150, 50)
        self.writer.goto(-150, 0)
        self.writer.end_fill()
        self.writer.goto(-18, 15)
        self.writer.color("white")
        self.writer.write("Login", font=('Comic Sans MS', 15, 'normal'),
                          align="left")

        # register button
        self.writer.begin_fill()
        self.writer.color("#315d79")
        self.writer.goto(-150, -75)
        self.writer.goto(150, -75)
        self.writer.goto(150, -25)
        self.writer.goto(-150, -25)
        self.writer.goto(-150, -75)
        self.writer.end_fill()
        self.writer.goto(-20, -60)
        self.writer.color("white")
        self.writer.write("Register", font=('Comic Sans MS', 15, 'normal'),
                          align="left")

    def menu_button(self) -> None:
        """This function is for menu button."""
        # weather button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("#315d79")
        self.writer.goto(-150, 0)
        self.writer.goto(150, 0)
        self.writer.goto(150, 50)
        self.writer.goto(-150, 50)
        self.writer.goto(-150, 0)
        self.writer.end_fill()
        self.writer.goto(-20, 15)
        self.writer.color("white")
        self.writer.write("Weather", font=('Comic Sans MS', 15, 'normal'),
                          align="left")
        # note button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("#315d79")
        self.writer.goto(-150, -75)
        self.writer.goto(150, -75)
        self.writer.goto(150, -25)
        self.writer.goto(-150, -25)
        self.writer.goto(-150, -75)
        self.writer.end_fill()
        self.writer.goto(-13, -60)
        self.writer.color("white")
        self.writer.write("Note", font=('Comic Sans MS', 15, 'normal'),
                          align="left")
        # interest button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("#315d79")
        self.writer.goto(-150, 75)
        self.writer.goto(150, 75)
        self.writer.goto(150, 125)
        self.writer.goto(-150, 125)
        self.writer.goto(-150, 75)
        self.writer.end_fill()
        self.writer.goto(-23, 90)
        self.writer.color("white")
        self.writer.write("Interest", font=('Comic Sans MS', 15, 'normal'),
                          align="left")
        # mail button
        self.writer.penup()
        self.writer.begin_fill()
        self.writer.color("#315d79")
        self.writer.goto(-150, -145)
        self.writer.goto(150, -145)
        self.writer.goto(150, -95)
        self.writer.goto(-150, -95)
        self.writer.goto(-150, -145)
        self.writer.end_fill()
        self.writer.goto(-10, -130)
        self.writer.color("white")
        self.writer.write("Mail", font=('Comic Sans MS', 15, 'normal'),
                          align="left")


    def back_button(self) -> None:
        """This function is for back button."""
        self.writer.penup()
        self.writer.color("white")
        self.writer.goto(-416.0, -202.0)
        self.writer.begin_fill()
        self.writer.goto(-316, -202.0)
        self.writer.goto(-316, -252.0)
        self.writer.goto(-416.0, -252.0)
        self.writer.end_fill()
        self.writer.goto(-380.0, -237.0)
        self.writer.color("#315d79")
        self.writer.write("Back", font=('Comic Sans MS', 15, 'normal'),
                          align="left")

    def change_interest_button(self, msg: str, func) -> None:
        """This function is for change interest button."""
        # add interest button
        self.writer.penup()
        self.writer.color("white")
        self.writer.goto(145, -140)
        self.writer.begin_fill()
        self.writer.goto(300, -140)
        self.writer.goto(300, -200)
        self.writer.goto(145, -200)
        self.writer.end_fill()
        self.writer.goto(215 - len(msg), -180)
        self.writer.color("#315d79")
        self.writer.write(msg, font=('Comic Sans MS', 15, 'normal'),
                          align="left")
        # back button
        self.writer.penup()
        self.writer.color("white")
        self.writer.goto(-416.0, -202.0)
        self.writer.begin_fill()
        self.writer.goto(-316, -202.0)
        self.writer.goto(-316, -252.0)
        self.writer.goto(-416.0, -252.0)
        self.writer.end_fill()
        self.writer.goto(-380, -237.0)
        self.writer.color("#315d79")
        self.writer.write("Back", font=('Comic Sans MS', 15, 'normal'),
                          align="left")
        self.screen.onclick(func)

    def mail_button(self) -> None:
        """This function is for mail button."""
        # add interest button
        self.writer.penup()
        self.writer.color("white")
        self.writer.goto(-305, -140)
        self.writer.begin_fill()
        self.writer.goto(-150, -140)
        self.writer.goto(-150, -200)
        self.writer.goto(-305, -200)
        self.writer.end_fill()
        self.writer.goto(-260, -180)
        self.writer.color("#315d79")
        self.writer.write("Send mail", font=('Comic Sans MS', 15, 'normal'),
                          align="left")

    def delete_button(self, func) -> None:
        """This function is for delete button."""
        # delete button
        self.writer.penup()
        self.writer.color("white")
        self.writer.goto(-305, -140)
        self.writer.begin_fill()
        self.writer.goto(-150, -140)
        self.writer.goto(-150, -200)
        self.writer.goto(-305, -200)
        self.writer.end_fill()
        self.writer.goto(-250, -180)
        self.writer.color("#315d79")
        self.writer.write("Delete", font=('Comic Sans MS', 15, 'normal'),
                          align="left")
        self.change_interest_button("Add", func)

    def interest_menu_buttons(self) -> None:
        """This function is for four interest buttons."""
        # Eats
        self.back_button()
        self.writer.penup()
        self.writer.color("white")
        self.writer.goto(-225.0, 120)
        self.writer.begin_fill()
        self.writer.goto(-25.0, 120)
        self.writer.goto(-25.0, 20)
        self.writer.goto(-225, 20)
        self.writer.end_fill()
        self.writer.goto(-190, 65)
        self.writer.forward(50)
        self.writer.color("#315d79")
        self.writer.write("Eats", font=('Comic Sans MS', 15, 'normal'),
                          align="left")
        # Songs
        self.writer.penup()
        self.writer.color("white")
        self.writer.goto(25, 120)
        self.writer.begin_fill()
        self.writer.goto(225, 120)
        self.writer.goto(225, 20)
        self.writer.goto(25, 20)
        self.writer.end_fill()
        self.writer.goto(105, 65)
        self.writer.color("#315d79")
        self.writer.write("Songs", font=('Comic Sans MS', 15, 'normal'),
                          align="left")
        # News
        self.writer.penup()
        self.writer.color("white")
        self.writer.goto(-225.0, -20)
        self.writer.begin_fill()
        self.writer.goto(-25.0, -20)
        self.writer.goto(-25.0, -120)
        self.writer.goto(-225, -120)
        self.writer.end_fill()
        self.writer.goto(-190, -80)
        self.writer.forward(50)
        self.writer.color("#315d79")
        self.writer.write("News", font=('Comic Sans MS', 15, 'normal'),
                          align="left")
        # Fortune
        self.writer.penup()
        self.writer.color("white")
        self.writer.goto(25, -20)
        self.writer.begin_fill()
        self.writer.goto(225, -20)
        self.writer.goto(225, -120)
        self.writer.goto(25, -120)
        self.writer.end_fill()
        self.writer.goto(60, -80)
        self.writer.forward(40)
        self.writer.color("#315d79")
        self.writer.write("Fortune", font=('Comic Sans MS', 15, 'normal'),
                          align="left")
