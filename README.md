### ML Code for this project linked in Colaboratory notebook below 

# course-project-group-44
course-project-group-44 created by GitHub Classroom

### This is the Drizzybot Project (Group 44).

## Summary of Introduction

 Drake doesn’t drop songs enough. With DrizzyBot you can do it for him. Simply run a script, and DrizzyBot spits out an entire Drake-like song for you. Instantly. This project DrizzyBot generates lyrics in the style of Drake using GPT-2 by OpenAI. There are other models that generate songs using artificial intelligence. Our project is unique in the sense we generate songs in the style of a specific artist. Our project used GPT-2 due to costs (it is free). We all really like Drake’s music, and thought this project would be a cool way to get our hands on ML and webscraping.

## Technical Architecture

In-depth:

<img width="780" alt="image" src="https://user-images.githubusercontent.com/22452113/206310404-00c8c531-f7ce-4a8a-ad59-c2ccc36bba57.png">

To implement we wrote a data gathering script (gets all lyrics from Drake songs), then we 
collected data files (saved lyrics used for training), trained the model (fine-tunes GPT-2 to generate Drake songs), saved the model (output of training), and finally inference the model (Generates song lyrics using saved model).

**List of Libraries:**

* urllib
* requests
* BeautifulSoup
* GPT-2
* Tensorflow

**List of APIs used:**

* [Genius]([url](https://docs.genius.com/#/annotations-h2))
* [LyricsGenius]([url](https://lyricsgenius.readthedocs.io/en/master/))
* [Lyrics.com]([url](https://www.lyrics.com/lyrics_api.php))

## Installation

1. Clone this repo
2. Install the relevant dependencies using your package manager (`requirements.txt` included)
3. Get song titles and song lyrics by uncommenting code in `get_lyrics.py`. _See Notes 1 & 2_
4. Open the following Colab Notebook: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/14IsF81EZACLEt6ZCWPkQiNLSujeviWNU?usp=sharing)
5. Run the blocks to train the model (make sure you upload the song lyrics)
6. Once the training is done, by running the last block, you will be able to generate Drake lyrics!


**Note 1:** _to use the Genius and Lyrics.com APIs you will need an API key. Get them and put them in `const.py`. Your Genius Key should be assigned to the variable `KEY` and the Lyrics.com key should be in `L_COM_KEY`._

**Note 2:** _The Lyrics.com API restricts you to 100 requests per day, so that will be a limiting factor in how fast you can get lyrics._

## Group Members and Roles

Prithvi Balaji (developer)

Pranav Gaka (developer)

Krishna Rao (developer)

Sumay Thakurdesai (developer)

All of us worked equally on all parts because we all have similar experiences with ML and software so we split the work. The team collaborated on the project through a GitHub repository. In order to structure our work in a way that it sticks to the schedule, we made issues on GitHub weekly. In order to prevent team friction, we made sure that we communicate with each other and that everyone’s voice is heard. Additionally, we worked on all parts of the project synchronously together, to ensure an even division of work for each team member. 
