import subprocess
from nfc_to_spotify import get_spotify_uri_from_tag

def read_nfc_tag():
    try:
        # Run the Node.js script and wait for 2 seconds for NFC read, then timeout
        result = subprocess.run(['node', 'readNfcTag.js'], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            print(result.stdout.strip())
            return result.stdout.strip()
    except subprocess.TimeoutExpired:
        print("Timeout: No NFC tag read within 2 seconds.")
    except Exception as e:
        print(f"Error reading NFC tag: {e}")

    return None

def get_spotify_uri_for_tag():
    tag_id = read_nfc_tag()
    if not tag_id:
        return None, None  # No tag detected

    spotify_uri = get_spotify_uri_from_tag(tag_id)
    return tag_id, spotify_uri

