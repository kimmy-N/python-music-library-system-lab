class Song:
    # Class attributes
    total_songs = 0
    artists = []
    genres = []
    songs_by_artist = {}
    songs_by_genre = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Count total songs
        Song.total_songs += 1

        # Track unique artists
        if artist not in Song.artists:
            Song.artists.append(artist)

        # Track unique genres
        if genre not in Song.genres:
            Song.genres.append(genre)

        # Count songs by artist
        if artist in Song.songs_by_artist:
            Song.songs_by_artist[artist] += 1
        else:
            Song.songs_by_artist[artist] = 1

        # Count songs by genre
        if genre in Song.songs_by_genre:
            Song.songs_by_genre[genre] += 1
        else:
            Song.songs_by_genre[genre] = 1

    @classmethod
    def get_total_songs(cls):
        return cls.total_songs

    @classmethod
    def get_artists(cls):
        return cls.artists

    @classmethod
    def get_genres(cls):
        return cls.genres

    @classmethod
    def get_songs_by_artist(cls):
        return cls.songs_by_artist

    @classmethod
    def get_songs_by_genre(cls):
        return cls.songs_by_genre