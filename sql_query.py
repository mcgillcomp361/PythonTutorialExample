# McGill Python Workshop 2
# Author: Mathieu Perreault (mathieu.perreault@gmail.com)
# Copyright 2011
import sqlite3

# Connect to the database
connection = sqlite3.connect('database.sql')

# Get the cursor
cursor = connection.cursor()

# Accept keyboard input.
keyboard_input = raw_input("Enter a list of artists, separated by a comma:\n")

result_set = None
unknown_artists = []
for artist in keyboard_input.split(','):
  cursor.execute("SELECT taglist FROM tags WHERE artist_name=?", (artist.lower().strip(),))
  fetchone = cursor.fetchone()
  if fetchone is None:
    unknown_artists.append(artist)
  else:
    tagset = set(fetchone[0].split(','))
    result_set = tagset if result_set is None else result_set.intersection(tagset)

print "Common tags:\n%s" % ('\n'.join(result_set)) if result_set else "No known artists"
print "Unknown artists: %s" % (unknown_artists)