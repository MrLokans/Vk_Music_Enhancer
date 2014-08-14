import urllib.request
import os.path
from bs4 import BeautifulSoup

BASE_URL = 'http://www.lyrics.com/'


def main():
    while True:
        print("1.Enter band name and song name\n(Band - Song format)\n")
        author = input("Author: ")
        title = input("Title: ")
        search_url = get_url_lyrics_com(author, title)
        get_lyrics_com(search_url)


def get_user_input():
    return input("==> ").lower()


def parse_for_search(user_input):
    if not "-" in user_input:
        print("Wrong naming format, aborting...\n")
        return 0
    res = user_input.split('-')
    song = {}
    song['Author'] = res[0]
    song['Title'] = res[1]
    parsed_author = trim_name(song['Author'])
    parsed_title = trim_name(song['Title'])
    search_string = parsed_title+"-lyrics-"+parsed_author
    return search_string


def trim_name(name):
    """
    Turns lower-case and separates with hyphens
    """
    name = str(name)
    #return "-".join([part.lower().strip() for part in name])
    return name.strip().lower().replace(" ", "-")


def get_url_lyrics_com(artist, title):
    adopt_artist = trim_name(artist)
    adopt_title = trim_name(title)
    search_url = BASE_URL + adopt_title + '-lyrics-' + adopt_artist + ".html"
    print("DEBUF LINK: ", search_url)
    return search_url


def get_lyrics_com(search_url):
    if not search_url:
        print("Something's wrong with url")
        return
    html_doc = urllib.request.urlopen(search_url)
    soup = BeautifulSoup(html_doc)

    lyrics = soup.find('div', {"class": "SCREENONLY"})
    if not lyrics:
        print("Lyrics not found")
    else:
        return lyrics.get_text()


def get_lyrics(search_str):
    url = BASE_URL + search_str+".html"
    print("Debug url is %s\n" % url)
    filename = search_str+".txt"
    if os.path.isfile(filename):
        print("Local lyrics file found\n\n")
        with open(filename) as f1:
            for line in f1.readlines():
                print(line)
        return 0
    html_doc = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_doc)
    #lyrics_a = soup.find('div', {"id" : "lyric_space"})
    lyrics = soup.find('div', {"class": "SCREENONLY"})
    if not lyrics:
        print("Lyrics not found")
    else:
        print(lyrics.get_text())
        filename = search_str+".txt"
        f1 = open(filename, "w")
        f1.writelines(lyrics.get_text())
        f1.close()

if __name__ == "__main__":
    main()
