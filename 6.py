from songs import (songs, artists)

print([
    song["name"]
    for song in songs
    for artist in artists
    if song["artist_id"] == artist["id"]
    if artist["name"] == "Post Malone"
])
