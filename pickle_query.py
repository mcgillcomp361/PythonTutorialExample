# McGill Python Workshop 2
# Author: Mathieu Perreault (mathieu.perreault@gmail.com)
# Copyright 2011
from pickle import Unpickler

### CHANGES from SQLite
unpickler = Unpickler(open('data.pickle', 'rb'))
artistMap = unpickler.load()
###

# Accept keyboard input.
keyboard_input = raw_input("Enter a list of artists, separated by a comma:\n")

result_set = None
unknown_artists = []
for artist in keyboard_input.split(','):
### CHANGES
  artist = artist.lower().strip()
  if not artist in artistMap:
    unknown_artists.append(artist)
  else:
    tagset = set(artistMap[artist].split(','))
###
    result_set = tagset if result_set is None else result_set.intersection(tagset)

print "Common tags:\n%s" % ('\n'.join(result_set)) if result_set else "No known artists"
print "Unknown artists: %s" % (unknown_artists)