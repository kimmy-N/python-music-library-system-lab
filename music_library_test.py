# music_library_test.py

class Song:
    """
    Song class represents a song with a name, artist, and genre.
    Tracks global statistics about all song instances:
    - Total number of songs
    - Unique artists and genres
    - Count of songs per artist and genre
    """

    # Class attributes
    total_songs = 0
    artists = set()
    genres = set()
    songs_by_artist = {}
    songs_by_genre = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class attributes
        Song.total_songs += 1
        Song.artists.add(artist)
        Song.genres.add(genre)

        # Update songs by artist count
        if artist in Song.songs_by_artist:
            Song.songs_by_artist[artist] += 1
        else:
            Song.songs_by_artist[artist] = 1

        # Update songs by genre count
        if genre in Song.songs_by_genre:
            Song.songs_by_genre[genre] += 1
        else:
            Song.songs_by_genre[genre] = 1


    # Class methods to access class attributes
    @classmethod
    def get_total_songs(cls):
        return cls.total_songs

    @classmethod
    def get_artists(cls):
        return list(cls.artists)

    @classmethod
    def get_genres(cls):
        return list(cls.genres)

    @classmethod
    def get_songs_by_artist(cls):
        return cls.songs_by_artist

    @classmethod
    def get_songs_by_genre(cls):
        return cls.songs_by_genre


# ------------------------------
# Test the Song class
# ------------------------------
song1 = Song("Blinding Lights", "The Weeknd", "Pop")
song2 = Song("Save Your Tears", "The Weeknd", "Pop")
song3 = Song("Levitating", "Dua Lipa", "Pop")
song4 = Song("Peaches", "Justin Bieber", "R&B")

print("Total songs:", Song.get_total_songs())
print("Artists:", Song.get_artists())
print("Genres:", Song.get_genres())
print("Songs by artist:", Song.get_songs_by_artist())
print("Songs by genre:", Song.get_songs_by_genre())