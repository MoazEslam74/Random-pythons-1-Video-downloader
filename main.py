import yt_dlp
lang='EN'
def changeLang():
    if lang=='AR':
        lang=='EN'
    elif lang =='EN':
        lang=='AR'
def downloadVideo():
    url= input('Enter the url:' if lang == 'EN' else 'أدخل رابط الفيديو:')
    print("choose your resolution:\n" if lang == 'EN' else "\nاختر الجودة المطلوبة:")
    print("1. Highest resolution" if lang == 'EN' else "1. أعلى جودة ممكنة")
    print("2. 1080p")
    print("3. 720p")
    print("4. 480p")
    print("5. Audio only")

    choice=input('choose num: (1-5)' if lang == 'EN' else "\nأدخل رقم الخيار (1-5): ")
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
        print("Wrong choic, The download will be in the default resolution (480p)"  if lang == 'EN' else  "اختيار غير صحيح، سيتم التحميل بأعلى جودة افتراضياً.")
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

    print("Downloading... please wait!\n" if lang == 'EN' else "\nجاري التحميل... يرجى الانتظار.\n")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nDownloaded sucessfuly" if lang == 'EN' else "\nتم التحميل بنجاح!")
    except Exception as e:
        print(f"\nError while the download:2 {e}" if lang == 'EN' else f"\nحدث خطأ أثناء التحميل: {e}")
if __name__ == "__main__":
    downloadVideo()