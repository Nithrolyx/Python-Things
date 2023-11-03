from pytube import YouTube
from sys import argv

link = argv[1] # FIRST CMD ARGUMENT
yt = YouTube(link)

print(f"Title: {yt.title}")
print(f"View: {yt.views}")

yd = yt.streams.get_highest_resolution() # GET HIGH RES

yd.download('/Users/Graphix 2/Desktop/SLRL/CODE')

#   PUT IN TERMINAL
#   py ytDL.py "insert url"
