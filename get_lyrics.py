"""
Code to get all song lyrics by an artist
"""
from time import sleep
from urllib.request import urlopen
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup
from const import KEY, L_COM_KEY   # pylint: disable=import-error
import lyricsgenius
import re
import os

def get_raw_lyrics(artist, title):
    """
    Inputs:
        artist: person who sings the song
        title: title of song
    Output:
        lyrics of the song

    """

    l_com_uid = "11118"
    l_com_url = "https://www.stands4.com/services/v2/lyrics.php?uid=" + l_com_uid + "&tokenid=" + L_COM_KEY + "&term="
    
 
    l_com_url += title.replace(" ", "%20").replace("’", "%27")
    l_com_url += "&artist=" + artist.replace("’", "%27").replace(" ", "%20")

    l_com_url += "&format=json"

    print("L_COM_URL: " + l_com_url)
    
    l_com_response = requests.get(l_com_url).json()
    if l_com_response == {'error': 'Daily Usage Exceeded'}:
        return "FAIL"

    print(l_com_response)

    lyrics_link = l_com_response["result"][0]["song-link"]
    print("LYRICS LINK FOR " + title + " BY " + artist + ": " + lyrics_link)

    url = lyrics_link
    try:
        url = url.replace(" ", "%20")
        url = re.sub(r'[^a-zA-Z0-9./:]', "", url)
        source = urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for ele in soup.find_all("pre"):
            if ele.get_text():
                return ele.get_text()
            else:
                return " "
    except:
        print("fail")
        return ""
    
    return " "


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
            # print(song["title"])
        page += 1
        request = genius.artist_songs(artist_id,
                                sort='popularity',
                                per_page=50,
                                page=page)

    return songs

def _get_artist_id(artist):
    path = "search?q="+artist
    find_id = _get("https://api.genius.com", path)
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
    with open("song_titles.txt", "w") as song_file:
        for song in songs:
            song_file.write(song + "\n")
    return songs

def get_song_lyrics(artist, index = 0):
    """
    gets lyrics of a song
    """
    titles = []
    if "song_titles.txt" in os.listdir("."):
        with open("song_titles.txt", "r") as song_file:
            titles = song_file.readlines()    
    else:
        titles = get_titles(artist)

    count = index

    for title in titles[count:]:
        title_processed = title.replace("/", " ")
        with open("lyric_files/" + title_processed + ".txt", "w") as lyrics_file:
            try:
                lyrics = get_raw_lyrics(artist, title)
                if lyrics == "FAIL":
                    print("FAIL")
                    break
                lyrics_file.write(lyrics)
                count += 1
            except:
                print(title)
                continue

    print("Finished at count " + str(count))

if __name__ == "__main__":

    # # code to get song titles
    # get_titles("Drake")

    # code to actually get lyrics

    start_idx = 1
    get_song_lyrics("Drake", start_idx)


    # code to remove empty files

    # count = 0
    # for file in os.listdir("lyric_files/"):
    #     with open("lyric_files/" + file, "r") as f:
    #         if f.read().strip() != "":
    #             count += 1
    #         else:
    #             os.remove("lyric_files/" + file)
    # print(count)

# finished at count 191