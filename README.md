<p align="center">
  <img src="RP_Video_downloader.ico" alt="Centered image" width="300">
</p>

<h1>Video Downloader 🎥⬇️</h1>

A versatile, dual-language (English/Arabic) graphical desktop application that allows you to download videos and extract audio effortlessly. Built with Python, this tool utilizes the powerful `yt-dlp` backend and features a clean, responsive user interface made with `tkinter`.

## ✨ Features

*   **Multiple Resolutions:** Choose from Highest Available, 1080p, 720p, or 480p.
*   **Audio Extraction:** Easily download videos as MP3 audio files.
*   **Bilingual Interface:** Toggle between English and Arabic layouts instantly.
*   **Custom Save Directory:** Automatically defaults to your system's `Downloads` folder, with an option to browse and choose a custom path.
*   **Real-time Progress Tracking:** A visual progress bar showing the download percentage.
*   **Non-blocking UI:** Built with threading to ensure the application remains responsive during downloads.

*(Note: The application download videos from YouTube, Facebooak and Instagram only).*
## 🛠️ Prerequisites

Before running this application, ensure you have the following installed:

1.  **Python 3.8+**
2.  **FFmpeg:** Essential for merging high-quality video/audio streams and extracting MP3s.
    *   *Windows:* Install via Command Prompt (`winget install ffmpeg`) or download from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) and add it to your system PATH.
    *   *Mac:* `brew install ffmpeg`
    *   *Linux:* `sudo apt install ffmpeg`

## 📦 Installation

1.  Clone this repository or download the source code (`main.py`).
2.  Install the required Python dependency:
    ```bash
    pip install yt-dlp
    ```
    and read more about the library from [yt-dlp](https://github.com/yt-dlp/yt-dlp#dependencies)
    
*(Note: `tkinter`, `threading`, and `os` are part of the standard Python library and do not require separate installation).*

## 🚀 Usage

1.  Run the application from your terminal or IDE:
    ```bash
    python main.py
    ```
2.  Paste the URL of the YouTube video you wish to download.
3.  Select your desired resolution or choose the "Audio only (MP3)" option from the dropdown menu.
4.  (Optional) Click "Browse..." to change the download destination folder.
5.  Click **Download** and watch the progress bar until it completes!

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

## ⚠️ Disclaimer

This tool is intended for personal use and educational purposes. Please respect the copyright of the content creators and abide by social media's Terms of Service when downloading content.
