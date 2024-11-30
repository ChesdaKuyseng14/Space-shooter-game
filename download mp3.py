import yt_dlp
#False = download playlist
#True = only one mp3

def download_audio(video_url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',  # Download the best available audio
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract and convert audio
                'preferredcodec': 'mp3',  # Force conversion to MP3
                'preferredquality': '192',  # Set MP3 quality to 192 kbps
            }],
            'outtmpl': '%(title)s.%(ext)s',  # Use the video title as the filename
            'noplaylist': typedownload,  # Avoid downloading entire playlists
            'extractaudio': True,  # Ensure audio is extracted (no video)
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Audio saved successfully as MP3.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
user = input('''1 for one music while 
             2 for music playlist: ''')
if user == 2:
    typedownload =False
else:
    typedownload = True

video_url = input("Enter YouTube video URL: ")
download_audio(video_url)
