from gmusicapi import Mobileclient
import codecs

api = Mobileclient()

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
response = api.get_top_songs()

# Writing to output TXT
f = codecs.open("GPMLibraryParsed.txt", mode="w", encoding = "utf-8")
result = ""

for ele in response:
	artist = str(ele['artist'])
	song = str(ele['title'])
	entry = artist + " " + song
	result = entry + '\n'

print("\n\n\nImported Thumbs Up tracks -")
print("========================================\n")
print(result)
f.write(result)
f.close()
