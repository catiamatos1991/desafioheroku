__author__ = 'P057668'

import urllib, json, pprint, getpass, string, time, MySQLdb

from mysql.connector import (connection)

# Connect to the database and create the tables
conn = connection.MySQLConnection(user='root', password='',
                                  host='localhost',
                                  database='database')
cursor = conn.cursor()

# Import library to deal with json
import json

# Import library which can print parsed data
from pprint import pprint

# Open the json file
import urllib.request

testFile = urllib.request.urlopen("http://freemusicarchive.org/recent.json")

# Load json data in python variable
import codecs

reader = codecs.getreader("utf-8")
data = json.load(reader(testFile))

def parse_json_response_populate(content):
    from collections import namedtuple
    tracks = []
    for e in data[u'aTracks']:
        tracks.append(namedtuple('track', e.keys())(*e.values()))

    for track in tracks:
        trackID = track.track_id
        albumTitle = track.album_title
        artistName = track.artist_name
        trackTitle = track.track_title
        duration = track.track_duration
        cover = track. track_image_file
        trackFile = track.track_file
        trackPublisher = track.track_publisher
        trackUrl = track.track_url
        trackListenUrl = track.track_listen_url
        trackUserFavorite = track.track_user_favorite


        #cursor.execute ("INSERT INTO restapi_music (track_id, album_title, artist_name, track_title, track_duration, track_number, track_disc_number, track_file, track_publisher, track_url,track_listen_url, track_user_favorite) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" , (trackID,albumTitle,artistName,trackTitle,trackDuration,trackNumber,trackDiskNumber,trackFile,trackPublisher,trackUrl,trackListenUrl, trackUserFavorite))
        cursor.execute ("INSERT INTO restapi_music (artist_name, track_title, album_title, cover, duration) VALUES (%s, %s, %s, %s,%s)" , (artistName,trackTitle, albumTitle, cover, duration))



        #Commit the changes.
        conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    parse_json_response_populate(data)