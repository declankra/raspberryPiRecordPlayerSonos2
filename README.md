# raspberrryPiRecordPlayerSonos2
tldr: variation for playing spotify songs through a sonos device using nfc tags as "vinyl records"

!!! Visit notion page for project details and setup: https://www.notion.so/declankramper/raspberryPiRecordPlayerSonos2-64432a48ffa44c0f861dc3d75144c6e3?pvs=4


NFC Record player main page: https://www.notion.so/declankramper/NFC-Record-Player-Build-bf95a606cc474c11a626b50821fb12d4?pvs=4

original project for playing through a spotify connected device:https://www.notion.so/declankramper/raspberryPiRecordPlayer-bc59312559bd4569a0f717fc6efae722?pvs=4 

**GENERAL OVERVIEW**

**what**
a “magic record player” device that plays music on a Sonos speaker when a song/playlist/album is placed on the record player

**how does device work?**
user places nfc tag on top of the reader → reader scans the id of the tag → python program will match the id with a spotify uri → use an http api server to make a call to play the spotify uri on the sonos speaker

### SCRIPTs

1. **playerSonos.py:** the main file. contains SonosController class with functions that make requests to http api server. contains infinite loop main() function that calls the get_spotify_uri_for_tag() function inside idToMp3.py file.
2. **idToMp3.py:** returns a tag id and spotify uri. it calls the read_nfc_tag() js function that will return a tag id and, if valid, calls the get_spotify_uri_from_tag() function that matches the tag id with a spotify uri.
3. **nfc_to_spotify.py**: contains get_spotify_uri_from_tag() function that searches the vinylColleciton.json file
4. **readNfcTag.js:** js file to read the response from the nfc card reader
5. **node-sonos-http-api:** cloned github repo. runs an http server that is used to make song control requests to.
6. **vinylCollection.json:** list of “records” with both tag ids and corresponding spotify uris


### Dependencies and downloads required for program
- python3
    - Python 3.9.7
- node.js
    - v21.2.0
- npm
- requests
- node-sonos-http-api github clone
- nfc-pcsc js library for communicating with scanner
    - PC/SC Lite development libraries