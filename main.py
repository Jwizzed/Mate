from turtle import done
import sys
from display import Display


def run():
    """Run the program."""
    display = Display()
    display.init_screen("mate", "background/main.png")
    display.login_register_button()
    done()


if __name__ == "__main__":
    ask = input("Do you want to run the program? (y/n): ")
    while ask != "n":
        if ask.lower() == "y":
            run()
            sys.exit()
        else:
            print("Invalid input.")
        ask = input("Do you want to run the program? (y/n): ")
    print("Program terminated.")
