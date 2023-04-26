from songs import (songs, artists)

def average(list):
    return sum(list) / len(list)

print(average([
    song["energy"]
    for song in songs
    for artist in artists
    if song["artist_id"] == artist["id"]
    if artist["name"] == "Drake"
]))
