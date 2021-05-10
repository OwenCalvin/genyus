import json
from typing import List

from api.API import API
from api.Song import Song
from lib.File import File

api = API()
songs: List[Song] = []


with open("./datas/import.txt", "r", encoding="utf8") as file:
    lines = file.read().splitlines()
    for songQuery in lines:
        results = api.search(songQuery)
        if len(results) > 0:
            song = api.getSong(results[0].song_id, True, True, 10, 0)
            songs.append(song)
            print(f"SCRAPED: {song.artist.name} - {song.name}")
            File.write_json("./datas/songs_2.json", songs)