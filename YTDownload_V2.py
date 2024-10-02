import yt_dlp

# List of YouTube video URLs you want to download
url = input("Video Url:")
type = input("Download Type(mp3 or mp4):")

# Replace with your desired output directory
output_path = './'

flag = 0

while flag != 1:  
    if type == "mp3" or type == "MP3":
        video_info = yt_dlp.YoutubeDL().extract_info(
            url ,download=False
        )
        ydl_opts={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':f"{video_info['title']}.mp3", #filename
        }            
        flag = 1

    elif type == "mp4" or type == "MP4":
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio',  # 畫質可改成"best"下載較快(720p)
            'outtmpl': output_path + '%(title)s.%(ext)s',  # Output file template
            'quiet': True,  # Suppress output messages
        }
        flag = 1
    else:
        print("Input Error!Plase input again.")
        type = input("Download Type(mp3 or mp4):")
        flag = 0

print("----------Download-----------")
print("\n" * 2)

# Initialize YouTube Downloader with the provided options
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            if type == "mp3" or type == "MP3":
                ydl.download([video_info['webpage_url']])
            else:
                ydl.download(url)  # Download the video

            print("\nSuccessful downloads:",url)
        except Exception as e:
            print(f"\nFailed to download {url}: {e}")
            
