### Forked from vipintom's repo here! -> https://github.com/vipintom/gpm2spotify
# gpm2spotify - A simple Google Play Music to Spotify Library Migrator!

These scripts migrate your Thumbs Up playlist from **Google Play Music** to **Spotify**. It's free, and your credentials stay with you!

Feel free to make whatever changes you'd like, based on how Google and Spotify decide to upgrade their APIs.

Uses simon-weber's **gmusicapi** (https://github.com/simon-weber/gmusicapi) and plamere's **spotipy** (https://github.com/plamere/spotipy)
# What do these scripts actually do ?

These scripts use wrappers for Spotify and GPM Web APIs to access and modify your libraries. 

`gpm.py` fetches your GPM library and stores it in a file (GPMLibraryParsed.txt). `spotify.py` reads this file, searches for that track on Spotify, and adds it to your Liked Songs list and a playlist of your liking. To enable this, you have to register a new App on a Spotify Developer account and use it to access Spotify's web APIs. 

# Instructions

- Download and install Python from https://www.python.org/downloads/release/python-372/  (x86-64 Installer)
  - Select Add Python 3.7 to Path Option    
  - Select **Install Now**
  - Close the installer
  - Open Powershell and enter following command: `python -V`. If version is displayed we are good to go.
  - Update pip: `python -m pip install --upgrade pip`
       
- Install Python Libraries required for scripts to work
    ```bash
    pip install spotipy
    pip install gmusicapi
    ```

- Next we want to register our script as an application on a Spotify Developer account. This will help us use Spotify's web APIs.
  - Go to https://developer.spotify.com/dashboard/
  - Log in using your Spotify credentials
  - Accept Developer Terms
  - Create an app
  - Enter an **App Name** and **App Description** (you may GPM2Spotify)
  - Check all the prerequisite boxes & accept T&C
  - Click **Edit Settings**
  - Add "http://localhost:8080/" to the **Redirect URI**
  - Copy **Client ID** and **Client Secret** to `Config.txt`
  - Go to "https://www.spotify.com/in/account/overview/" and copy your username to `Config.txt`

- Copy the script to local machine. Go to the previous folder
  - Execute `python gpm.py` and follow instructions. This should create a file `GPMLibraryParsed.txt` containing your Google Play Music **Thumbs Up** list with each line describing **\<Artist> \<Song Title>**
  - Execute `python spotify.py` and follow instructions. It will ask you to provide a URL to your playlist where it can add all the songs it has pulled from GPM. Create a playlist, and copy its URL which may look like this: "https://open.spotify.com/playlist/2v3egqg2ONyDTJOL1aHun9". This will import all songs from `GPMLibraryParsed.txt`, look up each song on Spotify and add the ones it finds to your library. It also spits out a list of the songs that it couldn't find, possibly due to incorrect name parsing (for which you could manually edit the entries in `GPMLibraryParsed.txt`), or the songs simply do not exist in Spotify's libraries.
       
That's it. Sit back and enjoy your library being populated! Yay!

# Reference Documentation
- **gmusicapi**: https://unofficial-google-music-api.readthedocs.io/en/latest/
- **spotipy**: https://spotipy.readthedocs.io/en/latest/