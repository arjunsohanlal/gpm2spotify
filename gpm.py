from gmusicapi import Mobileclient
import codecs

api = Mobileclient()

trackEntryStart = "sj#track"
trackPrefix = "'title'"
artistPrefix = "'artist'"
delim = ","

# Logging out before login
api.logout()

print("\n\nNote: ==========\nMake sure you've set up 2FA on your Google Account, as well as an App Password for this script. \n================\n")

# Logging in
android_id = api.FROM_MAC_ADDRESS
email = input('Email: ');
app_pwd = input('App password: ')
api.login(email, app_pwd, android_id, locale='en_US')

# Checking login status
print('Login status: '+str(api.is_authenticated()))

# Pulling all songs from thumbs up list
response = str(api.get_top_songs())

index = 0
f = codecs.open("GPMLibraryParsed.txt", mode="w", encoding = "utf-8")
result = ""

while index < len(response) :
    if  response.find(trackEntryStart, index) != -1 :
        
        index = response.index(trackEntryStart, index)

        titleIndex = response.index(trackPrefix, index) + 10
        titleDelimIndex = response.index(delim, titleIndex) - 1

        artistIndex = response.index(artistPrefix, index) + 11
        artistDelimIndex = response.index(delim, artistIndex) - 1

        result = result + response[artistIndex : artistDelimIndex] + " " + response[titleIndex : titleDelimIndex] + "\n"
    
    index = index + 1

print("\n\nThumbs up tracks ---\n")
print(result)
f.write(result)
f.close()
