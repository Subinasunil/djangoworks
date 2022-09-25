import json
import random
from functools import reduce
with open("songs.json",encoding="utf-8")as f:
    data=json.load(f)
# num_song=[song for song in data if song["album"]=="album1"]
# print(len(num_song))
num_song=list(filter(lambda s:s["album"]=="album1",data))
print(len(num_song))

# highest_rating_song=max(data,key=lambda s:s["rating"])
# print(highest_rating_song["rating"])
# rating_song=[s for s in data if s["rating"]==highest_rating_song["rating"]]
# print(rating_song)
top_songs=reduce(lambda s1,s2:s1 if s1["rating"] > s2["rating"] else s2,data)
print(top_songs)
sad_songs=[song for song in data if song["mode"]=="sad"]
print(random.sample(sad_songs,2))

no_of_albums=set([song["album"] for song in data])
print(len(no_of_albums))

sc={}
for song in data:
    album_song=song.get("album")
    if album_song in sc:
        sc[album_song]+=1
    else:
        sc[album_song]=1
print(sc)
print(max(sc.items(),key=lambda s:s[1]))
