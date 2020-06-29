### Forked from vipintom's repo here! -> https://github.com/vipintom/gpm2spotify
# gpm2spotify - A simple Google Play Music to Spotify Library Migrator!

These scripts migrate your Thumbs Up tracks from **Google Play Music** to **Spotify**. It's free, and your credentials stay with you!

Feel free to make whatever changes you'd like, based on how Google and Spotify decide to upgrade their APIs.

Uses simon-weber's **gmusicapi** (https://github.com/simon-weber/gmusicapi) and plamere's **spotipy** (https://github.com/plamere/spotipy)
# What do these scripts do?

These scripts use wrappers for Spotify and GPM Web APIs to access and modify your libraries. 

`gpm.py` fetches your GPM library and stores it in a file (GPMLibraryParsed.txt). `spotify.py` reads this file, searches for that track on Spotify, and adds it to your Liked Songs list and a playlist of your liking. To enable this, you simply have to create a new app on a Spotify Developer account, and use it to access Spotify's Web API. 

# Instructions

- Download and install Python from https://wiki.python.org/moin/BeginnersGuide/Download, and follow the appropriate instructions based on your system.
  - Make sure that you select the "Add Python 3.7 to Path" Option    
  - Complete your installation
  - Open a terminal (PowerShell/Command Prompt/bash) and enter the following command to check if Python has been installed properly: `python -V`; if your Python version is **3.7.2 or higher**, you're good to go.
  - Update pip: `python -m pip install --upgrade pip`
       
- Install these packages required for our scripts to work:
    ```bash
    pip install spotipy
    pip install gmusicapi
    ```
- Download `Config.txt`, `gpm.py` and `spotify.py` and put them into a folder.

- Next, we want to register our script as an application on a Spotify Developer account. This will help us use Spotify's Web API.
  - Go to https://developer.spotify.com/dashboard/
  - Log in using your Spotify credentials
  - Accept T&Cs
  - Create an app
  - Enter an **App Name** and **App Description** (use any name & description, it's irrelevant to the procedure)
  - Check all the prerequisite boxes & accept T&C
  - Click **Edit Settings**
  - Add "http://localhost:8080/" to the **Redirect URI** section
  - Copy **Client ID** and **Client Secret** to `Config.txt`
  - Go to "https://www.spotify.com/in/account/overview/" and copy your **username** to `Config.txt`
  
- We've also got to make sure that your Google Play Music libraries are accessible to the scripts. Head to https://myaccount.google.com/security and follow these steps:
  - Scroll down to the **Signing in to Google** section and make sure that **2-Step Verification** is enabled.
  - After enabling 2-Step Verification, go back to the **Signing in to Google** section and click on **App passwords**.
  - Under the _**Select the app and device you want to generate the app password for**_ area, click the _**Select app**_ dropdown, select _**Other (custom name)**_, enter any name into the next box, click the **Generate** button and note down the **16-character app password** that shows up.

- Open a terminal in the location where you've downloaded the `.py` scripts, and run them as follows:
  - Execute `python gpm.py` and follow instructions. Make sure you log in with your **Google Account email** and the **16-character App password** that you'd noted down before. This should create a file `GPMLibraryParsed.txt` containing your Google Play Music **Thumbs Up** tracks, with each line describing **\<Artist> \<Song Title>**
  - Execute `python spotify.py` and follow instructions. It will ask you to provide a URL to your playlist where it can add all the songs it has pulled from GPM. Create a playlist, and copy its URL which may look like this: "https://open.spotify.com/playlist/2v3egqg2ONyDTJOL1aHun9". This will import all songs from `GPMLibraryParsed.txt`, look up each song on Spotify and add the ones it finds to your library. It also spits out a list of the songs that it couldn't find, possibly due to incorrect name parsing (for which you could manually edit the entries in `GPMLibraryParsed.txt`), or the songs simply do not exist in Spotify's libraries.
       
That's it. Sit back and enjoy your library being populated! Yay!

# Reference Documentation
- **gmusicapi**: https://unofficial-google-music-api.readthedocs.io/en/latest/
- **spotipy**: https://spotipy.readthedocs.io/en/latest/
