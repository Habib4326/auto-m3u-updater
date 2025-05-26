import requests

M3U_URL = "https://raw.githubusercontent.com/Habib4326/Movie_plyalist/refs/heads/main/Update.m3u"
LOCAL_FILE = "updated_playlist.m3u"

def update_m3u():
    try:
        response = requests.get(M3U_URL)
        if response.status_code == 200:
            with open(LOCAL_FILE, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print("✅ M3U updated successfully.")
        else:
            print(f"❌ Failed to download M3U: HTTP {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_m3u()
