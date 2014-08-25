#! /usr/bin/env/python2.7
bitreight_values = (32, 64, 96, 128, 160, 192, 256, 320)


def get_song_size(url):
    pass


def get_correct_bitrate(bitrate):
    if bitrate > 320:
            proper_bitrate = 320
    elif bitrate < 16:
        proper_bitrate = 0
    else:
        proper_bitrate = bitrate - bitrate % 16
    return proper_bitrate


def main():
    while True:
        print("Enter bitrate:")
        input_value = int(input("=>\n"))
        print(get_correct_bitrate(input_value))


if __name__ == "__main__":
    main()
