import sys
from display import Display

if __name__ == "__main__":
    ask = input("Do you want to run the program? (y/n): ")
    while ask != "n":
        if ask.lower() == "y":
            Display().run()
            sys.exit()
        else:
            print("Invalid input.")
        ask = input("Do you want to run the program? (y/n): ")
    print("Program terminated.")
