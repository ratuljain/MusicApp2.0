import urllib
import json
import urllib2


# print urllib.urlencode({'q':'album:arrival artist:abba','type':'album'})

def makeQuery(album, artist):

    url = 'https://api.spotify.com/v1/search?'

    album = 'album:' + album
    artist = 'artist:' + artist

    query = album + " " + artist

    # print url + urllib.urlencode({'q':query,'type':'album'})

    return url + urllib.urlencode({'q':query,'type':'album'})


def parseJson(json):
    return json['albums']['items'][0]['images'][0]['url']

def getAlbumArtURL(album, artist):

    spotURL = makeQuery(album, artist)
    response = json.load(urllib2.urlopen(spotURL))

    print response

    try:
        artURL = parseJson(response)
        return artURL
    except:
        # print "nothing found"
        spotURL = makeQuery('*', artist)
        response = json.load(urllib2.urlopen(spotURL))
        try:
            artURL = parseJson(response)
            return artURL
        except:
            return False
        # return "http://www.ifans.com/forums/attachments/noartplaceholder-png.38049/"


# usage

# print getAlbumArtURL('', 'Theknd')
# y = json.load(urllib2.urlopen(x))
