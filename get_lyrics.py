"""
Code to get all song lyrics by an artist
"""
from time import sleep
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from const import KEY   # pylint: disable=import-error
import lyricsgenius
import re

def get_lyrics(artist, title):
    """
    Inputs:
        artist: person who sings the song
        title: title of song
    Output:
        lyrics of the song

    """
    url = "https://www.lyrics.com/lyric/35222023/" + artist + "/" + title
    # try:
    url = url.replace(" ", "%20")
    url = re.sub(r'[^a-zA-Z0-9./:]', "", url)
    source = urlopen(url).read()
    soup = BeautifulSoup(source, "html.parser")
    for ele in soup.find_all("pre"):
        return ele.get_text()
    # except:
    #     print("fail")
    #     return ""

# get JSON response from Genius API

def _get(base, path, params=None):
    """
    Get method
    """

    url = base + '/' + path + "&access_token=" + KEY
    response = requests.get(url=url, params=params)
    return response.json()

def _get_artist_songs(artist_id):
    """
    Gets songs by an artist with given artist id
    """

    genius = lyricsgenius.Genius(KEY)
    page = 1
    songs = []
    request = genius.artist_songs(artist_id,
                                sort='popularity',
                                per_page=50,
                                page=1)
    while request["songs"]:
        for song in request["songs"]:
            songs.append(song["title"])
            print(song["title"])
        page += 1
        request = genius.artist_songs(artist_id,
                                sort='popularity',
                                per_page=50,
                                page=page)



    # print(request)
    
    # print(page)
    
    # request = genius.artist_songs(artist_id,
    #                             sort='popularity',
    #                             per_page=50,
    #                             page=2)

    
    
    # print(len(songs))
    # for song in songs:
    #     print(song["title"])
    
    # request = genius.artist_songs(artist_id,
    #                             sort='popularity',
    #                             per_page=50,
    #                             page=3)
    # songs.extend(request['songs'])
    # for song in songs:
    #     print(song["title"])

    return songs

# def _get_song_titles(song_ids):
#     """
#     Gets song titles based on song_ids
#     """
#     titles = []
#     for song_id in song_ids:
#         path = "songs/{}".format(song_id)
#         data = _get("https://api.genius.com", path=path)["response"]["song"]
#         titles.append(data["title"])
#     return titles

def _get_artist_id(artist):
    path = "search?q="+artist
    find_id = _get("https://api.genius.com", path)
    # print(find_id["response"]["hits"])
    for hit in find_id["response"]["hits"]:
        if hit["result"]["primary_artist"]["name"] == artist:
            return hit["result"]["primary_artist"]["id"]
    return ""


def get_titles(artist):
    """
    gets all song titles by an artist
    """
    print("finding " +  artist + "'s artist id.")
    artist_id = _get_artist_id(artist)
    print("found")
    print("getting song ids. \n")
    songs = _get_artist_songs(artist_id)
    print("got song titles")
    return songs

def get_song_lyrics(artist):
    """
    gets lyrics of a song
    """
    titles = get_titles(artist)
    with open("lyrics.txt", "w") as lyrics_file:
        for title in titles:
            lyrics_file.write(get_lyrics(artist, title))

if __name__ == "__main__":
    get_song_lyrics("Drake")
