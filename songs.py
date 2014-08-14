#!/usr/binpython2.7
"""
TODO:
-Getting and saving list of songs of the user and downloading those ones that are not listed
-Adding lyrics to songs that do not have one
"""

# coding: utf8

import vk_api
import os
import urllib


def main():
    login, password = 'hydrargyrum1911@gmail.com', input("Enter your password: ")
    try:
        global vk
        vk = vk_api.VkApi(login, password)
    except vk_api.AuthorizationError as error_msg:
        print("Authorsation fails!")
        print(error_msg)
        return
    audio_urls = get_audio_info()
    #save_urls_in_file(audio_urls)
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
            f.write(str(song_detail))


def upload_photo_on_wall():
    #my_photos = vk_api.openPhotos("test.png")
    #r = vk_photo.photo_wall("test.png")
    pass
    return


def get_new_urls():
    pass


def download_new_audios():
    if not os.path.exists("Music"):
        os.mkdir("Music")


if __name__ == '__main__':
    main()
