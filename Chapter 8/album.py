def make_album(artist, title, number_songs = None):
    musician = {"artist_name" : artist, "album_name" : title}

    if number_songs:
        musician["number_songs"] = number_songs
    return musician

def get_album_input():
    artist = input("Artist name?\n")
    title = input("Album name?\n")
    songs = input("Song count?\n")
    return make_album(artist, title, songs)

check = input("Do you have more than 3 favorite artists? yes/no\n")

if check == "no":
    for i in range(0,3):
        print(get_album_input())

elif check == "yes":
    while True:
        print(get_album_input())
        quit = input("Would you like to quit? (yes/no)\n")
        if quit == "yes":
            break