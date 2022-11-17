import json
import random
import requests
from bs4 import BeautifulSoup
from login import Login


class Interest:
    """This class is all about user's interest"""

    def __init__(self, login_class: Login):
        self.__user = login_class.information[0]
        self.__password = login_class.information[1]
        self.__mymail = login_class.information[2]
        self.__interest = []
        self.all_toppics = {
            1: "Home",
            2: "War in Ukraine",
            3: "Coronavirus",
            4: "Climate",
            5: "Video",
            6: "World",
            7: "Asia",
            8: "UK",
            9: "Business",
            10: "Tech",
            11: "Science",
            12: "Stories",
            13: "Entertainment & Arts",
            14: "Health"
        }
        self.interest_to_url = {

            "Home": "",
            "War in Ukraine": "world-60525350",
            "Coronavirus": "coronavirus",
            "Climate": "science-environment-56837908",
            "Video": "av/10462520",
            "World": "world",
            "Asia": "asia",
            "UK": "uk",
            "Business": "business",
            "Tech": "technology",
            "Science": "science_and_environment",
            "Stories": "stories",
            "Entertainment & Arts": "entertainment_and_arts"
        }

    @property
    def user(self):
        """Return the username"""
        return self.__user

    @property
    def password(self):
        """Return the password"""
        return self.__password

    @property
    def mymail(self):
        """Return the user's mail."""
        return self.__mymail

    @property
    def interest(self):
        """Return the user's interest"""
        with open('user.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
            if self.user in users:
                try:
                    self.__interest = users[self.user]['interest']
                except KeyError:
                    pass
        return self.__interest

    @interest.setter
    def interest(self, new_interest):
        """Change the user's interest"""
        self.__interest = new_interest

    def change_interest(self, new_interest):
        """Add the user's interest"""
        _list = [self.all_toppics[int(interest)]
                 for interest in new_interest.split()]
        with open('user.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
            if self.user in users:
                users[self.user]['interest'] = _list
                self.interest = _list
        with open('user.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4)

    def show_interest_news(self):
        """Show the news of the user's interest"""
        number = int(input("How many news per each do you want to see? "))
        _list = []
        for interest in self.interest:
            _list.append(self.show_bbc_new(self.interest_to_url
                                           [interest], number))
        return _list

    @staticmethod
    def show_something_to_eat():
        """Show the random food"""
        with open("food_list.txt", 'r', encoding='utf-8') as foods:
            food_list = foods.read().splitlines()
            return random.choice(food_list)

    @staticmethod
    def show_top_10_songs(number=10):
        """Show the top 100 songs"""
        url = "https://www.billboard.com/charts/hot-100/"

        response = requests.get(url, timeout=5)
        website_html = response.text

        soup = BeautifulSoup(website_html, "html.parser")

        titles = soup.find_all(class_="o-chart-results-list-row-container")

        songs = []
        artists = []

        for title in range(number):
            song_tag = titles[title].select_one('h3')
            artist_tag = song_tag.find_next_sibling()
            songs.append(song_tag.string.strip())
            artists.append(artist_tag.string.strip())
        _list = []
        for index, song in enumerate(list(zip(songs, artists))):
            _list.append(f"{index + 1}. {song[0]} by {song[1]}")
        return _list

    def show_bbc_new(self, topic, number):
        """Show the news of the topic"""
        url = f"https://www.bbc.com/news/{topic}"
        response = requests.get(url, timeout=5)
        website_html = response.text
        soup = BeautifulSoup(website_html, "html.parser")
        links = soup.find_all(class_="gs-c-promo-heading")
        new = ""
        _list = []
        for key, value in self.interest_to_url.items():
            if value == topic:
                new = key
        _list.append(f"Here are some news about {new}:")

        for link in range(1, number + 1):
            try:
                _list.append(f"Title: {links[link].getText()}")
            except IndexError:
                _list.append("There are not enough news about this topic.")
                break
            try:
                if links[link].get("href")[0] == "/":
                    _list.append(
                        f"Link: https://www.bbc.com{links[link].get('href')}")
                else:
                    _list.append(f'Link: {links[link].get("href")}')
            except TypeError:
                pass
        return _list

    @staticmethod
    def show_fortune_telling():
        """Show the fortune telling"""
        with open('fortune.txt', 'r', encoding='utf-8') as fortunes:
            return random.choice(fortunes.read().split('%'))
