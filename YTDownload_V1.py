from pytube import YouTube
from pytube.innertube import _default_clients

url = input("Video Url:")
name = input("Video Name:")
type = input("Download Type(mp3 or mp4):")

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID"]

# print(yt.title)           # 影片標題
# print(yt.length)          # 影片長度 ( 秒 )
# print(yt.author)          # 影片作者
# print(yt.channel_url)     # 影片作者頻道網址
# print(yt.thumbnail_url)   # 影片縮圖網址
# print(yt.views)           # 影片觀看數
# 參考https://ithelp.ithome.com.tw/m/articles/10298678
# 年齡限制參考:https://stackoverflow.com/questions/75791765/how-to-download-videos-that-require-age-verification-with-pytube

def onProgress(stream, chunk, remains):
    total = stream.filesize                     # 取得完整尺寸
    percent = (total-remains) / total * 100     # 減去剩餘尺寸 ( 剩餘尺寸會抓取存取的檔案大小 )
    print(f'Loading... {percent:05.2f}%', end='\r')  # 顯示進度，\r 表示不換行，在同一行更新

yt = YouTube(url, use_oauth= True, allow_oauth_cache=True, on_progress_callback=onProgress)   # 網址

if not name:
    name = yt.title
flag = 0

while flag != 1:  
    if type == "mp3" or type == "MP3":
        print("-------Download-------")
        yt.streams.filter().get_audio_only().download(filename = name +'.mp3')
        flag = 1
    elif type == "mp4" or type == "MP4":
        print("-------Download-------")
        yt.streams.filter().get_highest_resolution().download(filename = name + '.mp4')
        flag = 1
    else:
        print("Input Error!Plase input again.")
        type = input("Download Type(mp3 or mp4):")
        flag = 0


# video_stream = yt.streams.get_highest_resolution()
# destination_path = './video/youtube'
# video_stream.download(output_path=destination_path)
# video_size_bytes = video_stream.filesize
# video_duration_seconds = yt.length

print('-------Success-------')


# import yt_dlp

# # List of YouTube video URLs you want to download
# video_urls = [
#     'https://www.youtube.com/watch?v=XWgdPt1kjOI'

# ]

# # Replace with your desired output directory
# output_path = r'c:\Users\88697\Downloads'

# # Options for yt_dlp (YouTube Downloader)
# ydl_opts = {
#     'format': 'best',  # Select the best available format
#     'outtmpl': output_path + '%(title)s.%(ext)s',  # Output file template
#     'quiet': True,  # Suppress output messages
# }

# # Lists to store successful and failed download URLs
# failed_downloads = []
# successful_downloads = []

# # Initialize YouTube Downloader with the provided options
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     for url in video_urls:
#         try:
#             ydl.download([url])  # Download the video
#             print("Downloaded:", url)
#             successful_downloads.append(url)
#         except Exception as e:
#             print(f"Failed to download {url}: {e}")
#             failed_downloads.append(url)
            
# # Print results
# print("\n" * 4)
# print("Failed downloads:", failed_downloads)
# print("Successful downloads:", successful_downloads)