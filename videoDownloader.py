from pytube import YouTube

link = input("masukkan link yang ingin di download:")
yt = YouTube(link)

downloader = yt.streams.get_highest_resolution()
print("dwnloading")

downloader.download(filename = "ochyy_video_downloader.mp3")
print("finish downloadig")