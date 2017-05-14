from mutagen.easyid3 import EasyID3
import os

def tag_genres(dir):
    genre = os.path.basename(dir)
    for file in os.listdir(dir):
        audiofile = dir + "/" + file
        if not file.startswith('.') and os.path.isfile(audiofile):
            audio = EasyID3(audiofile)
            audio["genre"] = unicode(genre)
            audio.save()

def get_metadata(file):
    audio = EasyID3(file)
    song_data = dict()
    #check if file has relevant tag
    if audio.get("artist") == None:
        a = "Unknown Artist"
    else:
        a = audio.get("artist")[0]
    if audio.get("title") == None:
        t = "Unknown Title"
    else:
        t = audio.get("title")[0]
    if audio.get("album") == None:
        al = "Unknown Album"
    else:
        al = audio.get("album")[0]
    if audio.get("genre") == None:
        g = "Unknown Genre"
    else:
        g = audio.get("genre")[0]
    song_data["artist"] = a.encode("utf-8")
    song_data["title"] = t.encode("utf-8")
    song_data["album"] = al.encode("utf-8")
    song_data["genre"] = g.encode("utf-8")
    return song_data

def get_artist_title(file):
    audio = EasyID3(file)
    song_data = dict()
    #check if file has relevant tag
    if audio.get("artist") == None:
        a = "Unknown Artist"
    else:
        a = audio.get("artist")[0]
    if audio.get("title") == None:
        t = "Unknown Title"
    else:
        t = audio.get("title")[0]
    song_data["artist"] = a.encode("utf-8")
    song_data["title"] = t.encode("utf-8")
    return song_data

def main(dir):
    for genre_subdir in os.listdir(dir):
        genre_path = dir + "/" + genre_subdir
        if os.path.isdir(genre_path):
            tag_genres(genre_path)

if __name__ == '__main__':
    dir = raw_input("Input the directory of dataset: ")
    main(dir)



