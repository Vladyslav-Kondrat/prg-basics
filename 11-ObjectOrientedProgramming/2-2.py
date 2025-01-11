class Music:
    def __init__(self, performer, title, album, year):
        self.performer = performer
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return f"{self.performer}, {self.title}, {self.album}, {self.year}"



song1 = Music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Music("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

print(song1)
print(song2)
