channels = [
    {
        "name": "Channel 1",
        "url": "http://example.com/stream1.m3u8",
        "logo": "http://example.com/logo1.png",
        "group": "News"
    },
    {
        "name": "Channel 2",
        "url": "http://example.com/stream2.m3u8",
        "logo": "http://example.com/logo2.png",
        "group": "Sports"
    }
]

def generate_m3u(filename="generated_playlist.m3u"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("#EXTM3U\n")
        for ch in channels:
            line = f'#EXTINF:-1 tvg-logo="{ch["logo"]}" group-title="{ch["group"]}",{ch["name"]}\n{ch["url"]}\n'
            file.write(line)
    print("✅ M3U playlist generated.")

if __name__ == "__main__":
    generate_m3u()
