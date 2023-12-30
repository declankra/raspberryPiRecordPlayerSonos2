import json

def get_spotify_uri_from_tag(tag_id, json_file='/home/pi/raspberryPiRecordPlayerSonos2/vinylCollection.json'):
    with open(json_file, 'r') as file:
        vinyl_collection = json.load(file)
    print("searching for uri from vinyl collection")
    for record in vinyl_collection:
        if record['tag_id'] == tag_id:
            print("found tag id in records")
            return record['spotify_URI']
    return None
