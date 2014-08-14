import urllib.request
import os.path
from bs4 import BeautifulSoup

BASE_URL = 'http://www.lyrics.com/'


def main():
    while True:
        print("1.Enter band name and song name\n(Band - Song format)\n")
        author = input("Author: ")
        title = input("Title: ")
        get_and_save_lyrics(author, title)


def trim_name(name):
    """
    Turns lower-case and separates with hyphens
    """
    name = str(name)
    return name.strip().lower().replace(" ", "-")


def get_url_lyrics_com(artist, title):
    adopt_artist = trim_name(artist)
    adopt_title = trim_name(title)
    search_url = BASE_URL + adopt_title + '-lyrics-' + adopt_artist + ".html"
    print("Debug url: ", search_url)
    return search_url


def get_lyrics_com(search_url):

    if not search_url:
        print("Something's wrong with url")
        return
    html_doc = urllib.request.urlopen(search_url)
    soup = BeautifulSoup(html_doc)

    lyrics = soup.find('div', {"class": "SCREENONLY"})
    if not lyrics:
        return False
    else:
        return lyrics.get_text()


def save_into_file(filename, lyrics):
    with open(filename, "w") as f:
        for line in lyrics:
            f.write(line)


def get_and_save_lyrics(author, title):
    url = get_url_lyrics_com(author, title)
    filename = url[:-5]
    if not os.path.exists(filename):
        lyrics = get_lyrics_com(url)
        if lyrics:
            print(lyrics)
            return lyrics
            save_into_file(filename)
        else:
            print("No lyrics found.")
    else:
        with open(filename, "r") as f:
            lyrics = f.readlines()
            print(lyrics)
            return lyrics

if __name__ == "__main__":
    main()
