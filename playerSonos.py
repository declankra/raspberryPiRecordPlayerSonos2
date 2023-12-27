from time import sleep
import requests
import idToMp3

class SonosController:
    def __init__(self, api_url, room):
        self.api_url = api_url
        self.room = room

    def is_music_playing(self):
        print("playback state checked")
        status = requests.get(f"{self.api_url}/{self.room}/state").json()
        return status.get('playbackState') == 'PLAYING'

    def set_volume(self, volume):
        print("volume set")
        requests.get(f"{self.api_url}/{self.room}/volume/{volume}")

    def stop_music(self):
        print("music stopped")
        response = requests.get(f"{self.api_url}/{self.room}/pause")
        return response.json()
    
    def start_music(self, spotify_uri):
        # Set volume to 50% if no music is playing
        if not self.is_music_playing():
            self.set_volume(35)
        # Adjust the URI to use the correct endpoint for Spotify URIs
        if "track:" in spotify_uri:
            uri_type = 'now'
        elif "playlist:" in spotify_uri:
            uri_type = 'now'  # 'now', 'next', or 'queue' can be used as per desired functionality
            spotify_uri = spotify_uri.replace('playlist:', 'user:spotify:playlist:')  # Adjust for playlists
        elif "album:" in spotify_uri:
            uri_type = 'now'  # 'now', 'next', or 'queue' can be used as per desired functionality
        else:
            return {"error": "Invalid Spotify URI"}

        # Using Spotify URI directly as per documentation for the endpoint
        print("making request to play")
        response = requests.get(f"{self.api_url}/{self.room}/spotify/{uri_type}/{spotify_uri}")
        return response.json()


def main():
    sonos = SonosController('http://localhost:5005', 'Family Room')
    last_tag_id = None

    while True:
        current_tag_id, spotify_uri = idToMp3.get_spotify_uri_for_tag()

        if current_tag_id is None and current_tag_id != last_tag_id:
            print("initiating stop")
            sonos.stop_music()
            last_tag_id = current_tag_id
        elif current_tag_id != last_tag_id:
            if spotify_uri:
                print("initiating start")
                sonos.start_music(spotify_uri)
                last_tag_id = current_tag_id
        sleep(1)  # Sleep to prevent a tight loop

if __name__ == "__main__":
    main()
