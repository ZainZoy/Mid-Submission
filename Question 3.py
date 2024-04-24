
class Song:
    all_songs = []
    def add(self,title,artist,album,duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.all_songs.append(self)

    def remove(self,title):
        if title in self.all_songs:
            index = self.all_songs.index(title)
            self.all_songs.pop(index)
        else:
            print("not in the the list of songs")
    def display_all(self):
        for i in self.all_songs:
            print(f"title: {i.title} \nartist: {i.artist}\nalbum: {i.album}\nduration: {i.duration}\n")


songs = Song()
songs.add("Darday Disco","Khan","Dard",90)
songs.add("Dhoom macha le","Khansi","Dhoom",80)
songs.add("Scattered", "Abdul Hannan", "Bikhra",240)


songs.display_all()


# class Playlist:
class Playlist:
    playlists = []
    def __init__(self,Title,Description,list_of_songs):
        self.Title = Title
        self.Description = Description
        self.songs = list_of_songs
        self.playlists.append(self)

    def display_all(self):
        for i in self.playlists:
            print(f"title: {i.title} \ndescription: {i.Description}\nlist of songs: {i.list_of_songs}\n")

# class library

class Library:
    def __init__(self,playlists):
        self.all_lists = playlists

    def display_all(self):
        for i in self.list_of_songs:
            print(f"title: {i.title} \ndescription: {i.Description}\nlist of songs: {i.list_of_songs}\n")

