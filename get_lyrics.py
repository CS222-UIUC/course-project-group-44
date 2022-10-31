"""
Code to get all song lyrics by an artist
"""
from time import sleep
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from const import KEY   # pylint: disable=import-error-for-const

def get_lyrics(artist, title):
    """
    Inputs:
        artist: person who sings the song
        title: title of song
    Output:
        lyrics of the song

    """
    url = "https://www.lyrics.com/lyric/35222023/" + artist + "/" + title
    source = urlopen(url).read()
    soup = BeautifulSoup(source, "html.parser")
    for ele in soup.find_all("pre"):
        return ele.get_text()

# get JSON response from Genius API

def _get(base, path, params=None, headers=None):
    """
    Get method
    """
    url = base + '/' + path
    token = "Bearer " + KEY
    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    response = requests.get(url=url, params=params, headers=headers)
    return response.json()

def _get_artist_songs(artist_id):
    """
    Gets songs by an artist with given artist id
    """
    current_page = 1
    next_page = True
    songs = []
    while next_page:
        path = "artists/{}/songs/".format(artist_id)
        params = {'page': current_page}
        data = _get("https://api.genius.com", path=path, params=params)

        page_songs = data['response']['songs']

        if page_songs:
            songs += page_songs
            current_page += 1
        else:
            next_page = False

    songs = [song["id"] for song in songs
             if song["primary_artist"]["id"] == artist_id]
    return songs

def _get_song_titles(song_ids):
    """
    Gets song titles based on song_ids
    """
    titles = []
    for song_id in song_ids:
        path = "songs/{}".format(song_id)
        data = _get("https://api.genius.com", path=path)["response"]["song"]
        titles.append(data["title"])
    return titles

def _get_artist_id(artist):
    find_id = _get("search", {'q': artist})
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
    song_ids = _get_artist_songs(artist_id)
    print("got song ids")
    sleep(30)
    titles = _get_song_titles(song_ids)
    return titles

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
