#!/usr/binpython2.7
"""
TODO:
-Getting and saving list of songs of the user and downloading those ones that are not listed
-Adding lyrics to songs that do not have one
-use sqlite db to store information
"""

# coding: utf8

import vk_api
import os
#import getpass
import sqlite3
#import urllib


def main():
    password = getpass.getpass("Enter your password: ")
    login = 'hydrargyrum1911@gmail.com'
    try:
        global vk
        vk = vk_api.VkApi(login, password)
    except vk_api.AuthorizationError as error_msg:
        print("Authorsation fails!")
        print(error_msg)
        return
    audio_info = get_audio_info()
    get_difference(audio_info)
    #print("saving urls")
    #save_urls_in_file(audio_info)
    #print("saved")
    #upload_photo_on_wall()
    return


def trim_urls(url):
        """
        Used to trim urls by removing
        anythind after '.mp3'
        """
        if '.mp3' in url:
            return url[:url.find(".mp3")+4]
        else:
            return url


def get_audio_info():
    response = vk.method('audio.get')
    if response:
        song_urls = [trim_urls(song['url']) for song in response['items']]
        song_name = [song['artist']+" - "+song['title'] for song in response['items']]
        song_info = zip(song_name, song_urls)
        return song_info


def save_urls_in_file(song_info):
    #urls = "\n".join(song_info)
    with open("songs.txt", "w") as f:
        for song_detail in song_info:
            f.writelines(str(song_detail))


def get_difference(new_lyrics, filename='songs.txt'):
    if not os.path.exists(filename):
        print("File does not exist, nothing to compare with")
        return
    else:
        with open(filename, "r") as f:
            saved_audio = f.readlines()
            print("debugging...")
            print(saved_audio)
            print("="*20)
            for song in new_lyrics:
                if not str(song) in saved_audio:
                    print(song)


"""
def upload_photo_on_wall():
    #my_photos = vk_api.openPhotos("test.png")
    #r = vk_photo.photo_wall("test.png")
    pass
    return
"""

def get_new_urls():
    pass


def download_new_audios():
    if not os.path.exists("Music"):
        os.mkdir("Music")


if __name__ == '__main__':
    main()
