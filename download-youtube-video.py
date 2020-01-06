#youtube-dl is a command line tool which is completely written in python for downloading any youtube videos with various formats and various resolution.

#pip install youtube-dl

import youtube_dl

links=['https://www.youtube.com/watch?v=PCwL3-hkKrg']
ydl=youtube_dl.YoutubeDL() #you can pass various options(resolution,video format and so on)
ydl.download(links)
