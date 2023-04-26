import csv
from functools import (reduce)
import inspect

compose = lambda *fs: reduce(lambda f, g: lambda a: f(g(a)), fs)

adjust = lambda function, key: lambda dictionary: {
    k: function(v) if k == key else v for (k, v) in dictionary.items()
}

with open("artists.csv", newline="") as f:
    artists = tuple(adjust(int, "id")(artist) for artist in csv.DictReader(f))

with open("songs.csv", newline="") as f:
    songs = tuple(
        compose(
            adjust(int, "duration_ms"),
            adjust(float, "tempo"),
            adjust(float, "valence"),
            adjust(float, "speechiness"),
            adjust(float, "loudness"),
            adjust(int, "key"),
            adjust(float, "energy"),
            adjust(float, "danceability"),
            adjust(int, "artist_id"),
            adjust(int, "id"),
        )(song)
        for song
        in csv.DictReader(f)
    )

fix_width = lambda text: (str(text).ljust(10))[:10]

def print_table(table):
    print(*(fix_width(t) for t in table[0]))
    for row in table:
        print(*(fix_width(t) for t in row.values()))

def select(*identifiers):
    locals_result = inspect.currentframe().f_back.f_locals
    return {identifier: locals_result[identifier] for identifier in identifiers}
