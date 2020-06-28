import sys
import spotipy
import spotipy.util as util
import codecs

def GetTracks(playlist_response) :

    input = str(playlist_response)
    idePrefix = "spotify:track:"
    delim = "'"
    index = 0
    result = ""
    while index < len(input) :
        if input.find(idePrefix, index) != -1 :
            index = input.index(idePrefix, index) + 14
            delimIndex = input.index(delim, index)
            result = result + str(input[index : delimIndex]) + "\n"
        index = index + 1
    return result

def GetUserId(current_user) :

    input = str(current_user)
    idPrefix = "spotify:user:"
    delim = "'"

    if input.find(idPrefix) :
        idIndex = input.index(idPrefix) + 13
        delimIndex = input.index(delim, idIndex)
        result = str(input[idIndex : delimIndex])
        return result
    return ""

def GetPlaylistId(SpotifyClient, playlistName, userId) :

    input = str(playlistName)
    idPrefix = "spotify:playlist:"
    delim = "'"

    response = SpotifyClient.user_playlists(userId)
    print(response)

def GetKeyFromConfig(key) :
    keyStr = str(key)
    f = codecs.open("Config.txt", encoding = "utf-8")
    for x in f :
        input = str(x)
        if input.find(keyStr) != -1 :
            tempList = input.split(':')
            return tempList[1].strip()

def GetUserName() :
    return GetKeyFromConfig(key="USERNAME")

def GetClientId() :
    return GetKeyFromConfig(key="CLIENT_ID")

def GetClientSecret() :
    return GetKeyFromConfig(key="CLIENT_SECRET")

def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


username = GetUserName()
clientId = GetClientId()
clientSecret = GetClientSecret()

print(username)
print(clientId)
print(clientSecret)

scope = 'user-library-read user-library-modify playlist-modify-private playlist-modify-public'
redirect_uri = 'http://localhost:8080/'

token = util.prompt_for_user_token(username,scope,clientId,clientSecret, redirect_uri)
sp = spotipy.Spotify(auth=token)

userId = GetUserId(current_user = sp.current_user())
playlistURL = str(input("Enter playlist URL: "))
playlistSplit = playlistURL.split('/')
playlistID = playlistSplit[len(playlistSplit) - 1]

# Removing any further parameters from the URL
if ((not playlistID.isalnum()) and not(playlistID == "")):
    cleanID = playlistID
    while not cleanID.isalnum():
        cleanID = cleanID[:-1]
    playlistID = cleanID


# Creating a list of unlisted tracks
unlisted_tracks = []

f = open("GPMLibraryParsed.txt", encoding="utf8")
for x in f:
    print(x)
    response = sp.search(x, limit = 1)
    strResponse = str(response)
    if  strResponse.find("spotify:track") != -1 :
        index = strResponse.index("spotify:track")
        delimiter = strResponse.index("'", index)
        trackId = str(strResponse[index : delimiter])
        trackId = trackId.replace("spotify:track:", "")
        sp.current_user_saved_tracks_add(tracks=[trackId])
        sp.user_playlist_add_tracks(user = userId,playlist_id = playlistID, tracks=[trackId])
    else:
        unlisted_tracks.append(x)

# Displaying unlisted tracks
print("\n\n\nUnlisted tracks --- \n");
for x in unlisted_tracks:
    print(x[:-1])
