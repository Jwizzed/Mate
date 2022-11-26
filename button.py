import time
import turtle

from playsound import playsound

from interest import Interest
from mail import Mail
from note import Note


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
        self.screen.onclick(self.login_register_click)

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
        self.screen.onclick(self.menu_click)

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
        self.screen.onclick(self.back_click)

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
        self.change_interest_button("Change        ", self.mail_click)

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

        if 180.0 <= x_cor <= 250 and -160.0 <= y_cor <= -110:
            playsound("background/click.mp3")
            ask = self.screen.textinput("Agree? (y/n)",
                                        "Do you want to delete your "
                                        "account?")
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
                else:
                    self.any_screen("Error", "Wrong password.")
                    self.back_button()

            elif ask in "nN":
                self.any_screen("Not delete", "Account not deleted.")
                self.back_button()

            else:
                self.any_screen("Error", "Wrong input.")
                self.back_button()

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
        if -316 >= x_cor >= -416.0:
            if -252.0 <= y_cor <= -202.0:
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
        if -316 >= x_cor >= -416.0:
            if -252.0 <= y_cor <= -202.0:
                playsound("background/click.mp3")
                self.menu()

    def change_interest_click(self, x_cor: (int, float),
                              y_cor: (int, float)) \
            -> None:
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

        self.back_click(x_cor, y_cor)

    def delete_click(self, x_cor: (int, float),
                     y_cor: (int, float)) -> None:
        """This function is for delete click."""
        # Add
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
                else:
                    self.any_screen("Note", "You can't add more ")
                    self.back_button()
            else:
                while True:
                    deadline = self.screen.textinput(
                        "", "Enter the deadline date (day/month/year): ")
                    if not deadline:
                        self.any_screen("Error",
                                        "You must fill in the deadline.")
                        self.back_button()

                    elif deadline and deadline.count("/") != 2:
                        self.any_screen("Error",
                                        "Wrong format. Try again.")
                        self.back_button()
                    else:
                        break

                if deadline:
                    notes = self.screen.textinput("", "Enter the note: ")
                    if notes:
                        note.add_note(deadline, notes)
                        self.any_screen("Success", "Note added.")
                        self.back_button()
                    else:
                        self.any_screen("Error",
                                        "You must fill in the note.")
                        self.back_button()
                else:
                    self.any_screen("Error",
                                    "You must fill in the deadline.")
                    self.back_button()

        # Delete
        if -305 < x_cor < -150 and -140 > y_cor > -200:
            playsound("background/click.mp3")
            self.delete_note()
        self.back_click(x_cor, y_cor)

    def delete_note(self) -> None:
        self.any_screen()
        note = Note(self.logging)
        while True:
            deadline = self.screen.textinput(
                "", "Enter the deadline date (day/month/year): ")
            if not deadline or deadline.count("/") != 2:
                self.any_screen("Error", "Wrong format. Try again.")
                continue
            break
        if note.delete_note(deadline):
            self.any_screen("Success", "Note deleted.")
        else:
            self.any_screen("Error", "Note not found.")
        self.back_button()

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
                                                        self.weather).encode(
                    'utf-8', 'ignore'))
                self.back_button()
            else:
                self.any_screen("Mail", "Mail not sent.")
                self.back_button()
        self.back_click(x_cor, y_cor)
