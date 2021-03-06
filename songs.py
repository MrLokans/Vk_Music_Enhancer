#!/usr/binpython2.7
"""
TODO:
-Getting and saving list of songs of the user and downloading those ones that are not listed
-Adding lyrics to songs that do not have one
"""

# coding: utf8

import vk_api
from vk_api.Vk import Vk
import os
import getpass
import sqlite3
#import urllib

USER_ID = "5"


def print_menu():
    print("What do you want to do:\n")
    print("1. Get list of my songs.\n")
    print("2. Save list of songs in file.\n")
    print("3. Download all songs.\n")
    print("4. Get and download new songs.\n")
    print("5. Clear db.\n")


def main():
    # password = getpass.getpass("Enter your password: ")

    # login = 'hydrargyrum1911@gmail.com'
# try:
    global vk
    vk = Vk()
    if not vk.is_valid_access_token():
        vk.get_access_token()
    db = connect_db()
    # TODO: Menu
    """while True:
        print_menu()
        choice = input("\nYour choice => ")
        {
        "1": print(get_audio_info()),
        "2": print("2"),
        "3": print("3"),
        "4": print("4"),
        "5": remove_table(),
        }[choice]"""
    info = get_audio_info()
    save_urls_in_db(info, db)
    #get_difference(info, db)
    close_db(db)

    return


def connect_db(name='songs.db'):
    if os.path.exists(name):
        conn = sqlite3.connect(name)
        return conn
    else:
        conn = sqlite3.connect(name)
        c = conn.cursor()
        c.execute('''CREATE TABLE songs
            (artist text, title text, url text)''')
    return conn


def close_db(db):
    db.close()


def trim_urls(url):
        """
        Used to trim urls by removing
        anythind after '.mp3'
        """
        if '.mp3' in url:
            return url[:url.find(".mp3")+len(".mp3")]
        else:
            return url


def get_audio_info():
    """
    returns list of tuples with song artist, title and url
    """
    response = vk.api_method('audio.get', user_id=USER_ID)
    if response:
        response = response["response"]
        song_urls = [trim_urls(song['url']) for song in response['items']]
        song_authors = [song['artist'] for song in response['items']]
        song_titles = [song['title'] for song in response['items']]
        song_info = list(zip(song_authors, song_titles, song_urls))
        return song_info


def save_urls_in_db(song_info, db):
    """
    saves provided urls in songs table in db
    """
    c = db.cursor()
    diff = get_difference(song_info, db)
    if diff:
        c.executemany('INSERT INTO songs VALUES (?, ?, ?)', diff)
        db.commit()
        return
    else:
        c.executemany('INSERT INTO songs VALUES (?, ?, ?)', song_info)
        db.commit()


def get_difference(song_info, db):
    """Transforms list of song_info into set,
    transforms db songs table into set
    and returns list of get_difference"""
    c = db.cursor()
    diff_info = []
    db_song_info = [song for song in c.execute('SELECT artist, title FROM songs')]
    diff_info = [song for song in song_info if (song[0],song[1]) not in db_song_info]
    return diff_info


"""
def upload_photo_on_wall():
    #my_photos = vk_api.openPhotos("test.png")
    #r = vk_photo.photo_wall("test.png")
    pass
    return
"""



def download_new_audios():
    if not os.path.exists("Music"):
        os.mkdir("Music")

def remove_table():
    print("removing table")

if __name__ == '__main__':
    main()
