import yt_dlp
lang='AR'
def changeLang():
    if lang=='AR':
        lang=='EN'
    elif lang =='EN':
        lang=='AR'
def downloadVideo():
    url= input('Enter the url:')
    print("choose your resolution:\n")
    print("1. Highest resolution")
    print("2. 1080p")
    print("3. 720p")
    print("4. 480p")
    print("5. Audio only")

    choice=input('choose num:')
    if choice == '1':
        format_selector = 'bestvideo+bestaudio/best'
    elif choice == '2':
        format_selector = 'bestvideo[height<=1080]+bestaudio/best'
    elif choice == '3':
        format_selector = 'bestvideo[height<=720]+bestaudio/best'
    elif choice == '4':
        format_selector = 'bestvideo[height<=480]+bestaudio/best'
    elif choice == '5':
        format_selector = 'bestaudio/best'
    else:
        print("Wrong choic, The download will be in the default resolution (480p)")
        format_selector = 'bestvideo[height<=480]+bestaudio/best'

    #Advance settings
    ydl_opts = {
        'format': format_selector,
        'outtmpl': '%(title)s.%(ext)s', 
    }
    
    #For audio only
    if choice == '5':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    print("Downloading... please wait!\n")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nDownloaded sucessfuly")
    except Exception as e:
        print(f"\nError while the download:2 {e}")
if __name__ == "__main__":
    downloadVideo()