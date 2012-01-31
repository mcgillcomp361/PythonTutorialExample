# McGill Python Workshop 2
# Author: Mathieu Perreault (mathieu.perreault@gmail.com)
# Copyright 2011
import sqlite3, csv, os

# Create the CSV reader.
csvreader = csv.reader(open('ArtistTags.csv'))

# (Re)create the database and connect to it.
if os.path.exists('database.sql'):
  os.remove('database.sql')
connection = sqlite3.connect('database.sql')

# Get the cursor and create a table.
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS tags (artist_name VARCHAR(200) PRIMARY KEY, taglist VARCHAR(1000))')

# Iterate through the rows and add artists and tags.
for row in csvreader:
  # Format: 000b1990-4dd8-4835-abcd-bb6038c13ac7,Hayden,indie rock,19
  if len(row) < 4:
    continue
  artist = row[1].lower()
  tag = row[2].lower()
  score = int(row[3])
  if score < 40:
    # Relevance tweak.
    continue
  # Check the existence of the artist in the database.
  cursor.execute('SELECT * FROM tags WHERE artist_name=?', (artist,)) #replace variables with question marks
  fetched = cursor.fetchone() # Important not to call fetch twice! 
  if fetched is None:
    # Artist wasn't in the database, add the tag.
    cursor.execute('INSERT INTO tags VALUES (?, ?)', (artist, tag))
  else:
    # Artist was in the database, add the tag to the list that was there.
    taglist = fetched[1].split(',')
    taglist.append(tag)
    cursor.execute('UPDATE tags SET taglist=? WHERE artist_name=?', (",".join(taglist), artist))
connection.commit()


