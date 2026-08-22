import yt_dlp
import tkinter as tk
from tkinter import ttk, messagebox
import threading

class VideoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.lang = 'EN'
        self.root.title("Video Downloader")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        # Language dictionary
        self.texts = {
            'EN': {
                'title': 'YouTube Video Downloader',
                'url_label': 'Enter the URL:',
                'res_label': 'Choose Resolution:',
                'btn_download': 'Download',
                'btn_lang': 'عربي',
                'status_ready': 'Ready to download.',
                'status_downloading': 'Downloading... please wait!',
                'success': 'Downloaded successfully!',
                'error': 'Error during download: ',
                'resolutions': ["1. Highest resolution", "2. 1080p", "3. 720p", "4. 480p", "5. Audio only (MP3)"]
            },
            'AR': {
                'title': 'برنامج تحميل الفيديوهات',
                'url_label': 'أدخل رابط الفيديو:',
                'res_label': 'اختر الجودة المطلوبة:',
                'btn_download': 'تحميل',
                'btn_lang': 'English',
                'status_ready': 'جاهز للتحميل.',
                'status_downloading': 'جاري التحميل... يرجى الانتظار!',
                'success': 'تم التحميل بنجاح!',
                'error': 'حدث خطأ أثناء التحميل: ',
                'resolutions': ["1. أعلى جودة ممكنة", "2. 1080p", "3. 720p", "4. 480p", "5. صوت فقط (MP3)"]
            }
        }

        self.setup_ui()
        self.update_ui_text()

    def setup_ui(self):
        # language button
        self.lang_btn = tk.Button(self.root, text="", command=self.toggle_lang, font=("Arial", 10, "bold"))
        self.lang_btn.pack(anchor="ne", padx=10, pady=10)

        # Title
        self.title_label = tk.Label(self.root, text="", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Video URL link
        self.url_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.url_label.pack(anchor="w", padx=30)
        
        self.url_entry = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.url_entry.pack(padx=30, pady=5)

        # Choose resolution
        self.res_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.res_label.pack(anchor="w", padx=30, pady=(10, 0))
        
        self.resolution_combo = ttk.Combobox(self.root, state="readonly", width=47, font=("Arial", 11))
        self.resolution_combo.pack(padx=30, pady=5)
        

        # Download button
        self.download_btn = tk.Button(self.root, text="", command=self.start_download_thread, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=20)
        self.download_btn.pack(pady=20)

        # states
        self.status_label = tk.Label(self.root, text="", font=("Arial", 10), fg="gray")
        self.status_label.pack(pady=5)

    def update_ui_text(self):
        """Update UI depend on the language"""
        t = self.texts[self.lang]
        self.root.title(t['title'])
        self.title_label.config(text=t['title'])
        self.url_label.config(text=t['url_label'])
        self.res_label.config(text=t['res_label'])
        self.download_btn.config(text=t['btn_download'])
        self.lang_btn.config(text=t['btn_lang'])
        self.status_label.config(text=t['status_ready'])
        
        
        current_index = self.resolution_combo.current()
        if current_index == -1: current_index = 0
        self.resolution_combo['values'] = t['resolutions']
        self.resolution_combo.current(current_index)

    def toggle_lang(self):
        
        self.lang = 'AR' if self.lang == 'EN' else 'EN'
        self.update_ui_text()

    def start_download_thread(self):
        """Isolated Thread to avoid freeze the frame"""
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Please enter a URL" if self.lang == 'EN' else "يرجى إدخال الرابط أولاً")
            return

        # Freeze the download button
        self.download_btn.config(state=tk.DISABLED)
        self.status_label.config(text=self.texts[self.lang]['status_downloading'], fg="blue")

        # Start the thread
        thread = threading.Thread(target=self.download_video, args=(url,))
        thread.start()

    def download_video(self, url):
        
        choice_index = self.resolution_combo.current() + 1 
        
        if choice_index == 1:
            format_selector = 'bestvideo+bestaudio/best'
        elif choice_index == 2:
            format_selector = 'bestvideo[height<=1080]+bestaudio/best'
        elif choice_index == 3:
            format_selector = 'bestvideo[height<=720]+bestaudio/best'
        elif choice_index == 4:
            format_selector = 'bestvideo[height<=480]+bestaudio/best'
        elif choice_index == 5:
            format_selector = 'bestaudio/best'
        else:
            format_selector = 'bestvideo[height<=480]+bestaudio/best'

        ydl_opts = {
            'format': format_selector,
            'outtmpl': '%(title)s.%(ext)s', 
            'noplaylist': True 
        }
        
        if choice_index == 5:
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            
            self.root.after(0, self.download_success)
        except Exception as e:
            
            self.root.after(0, self.download_error, str(e))

    def download_success(self):
        self.status_label.config(text=self.texts[self.lang]['success'], fg="green")
        self.download_btn.config(state=tk.NORMAL)
        self.url_entry.delete(0, tk.END) 
        messagebox.showinfo("Success", self.texts[self.lang]['success'])

    def download_error(self, error_msg):
        error_text = self.texts[self.lang]['error']
        self.status_label.config(text=error_text + " (Check URL)", fg="red")
        self.download_btn.config(state=tk.NORMAL)
        messagebox.showerror("Error", f"{error_text}\n{error_msg}")

if __name__ == "__main__":
   
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    
    root.mainloop()