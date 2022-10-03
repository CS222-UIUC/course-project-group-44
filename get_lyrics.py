from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_lyrics(title="Jaded"):
    url = "https://www.lyrics.com/lyric/35222023/Drake/" + title
    source = urlopen(url).read()
    soup = BeautifulSoup(source, "html.parser")
    for ele in soup.find_all("pre"):
        print(ele.get_text())