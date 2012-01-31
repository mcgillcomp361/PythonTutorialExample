# McGill Python Workshop 2
# Author: Mathieu Perreault (mathieu.perreault@gmail.com)
# Copyright 2011
import csv, os
from pickle import Pickler

# Create the CSV reader.
csvreader = csv.reader(open('ArtistTags.csv'))

### CHANGES from SQLite
if os.path.exists('data.pickle'):
  os.remove('data.pickle')
  
file_handler = open('data.pickle', 'ab')
pickler = Pickler(file_handler)

artistMap = {}
###

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
### CHANGES
  if artist in artistMap:
    # Artist was in the map
    taglist = artistMap[artist].split(',')
    taglist.append(tag)
    artistMap[artist] = ','.join(taglist)
  else:
    artistMap[artist] = tag

pickler.dump(artistMap)
###

    