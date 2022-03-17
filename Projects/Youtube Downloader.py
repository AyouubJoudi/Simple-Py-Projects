from pathlib import Path
from pytube import YouTube, Playlist
print('A disclaimer: this sucks on mobile :)')
while True:
    choice = input('1 : video | 2 : playlist | 3 : stream\n')
    if choice in ['1', '2', '3']:
        break


def video():
    yt = YouTube(input("What is the url of the video you want to download : "))
    while True:
        choice = input("mp4 or mp3: ")
        if choice in ['mp3', 'mp4']:
            break

    def mp4(yt):
        quality = []
        for i in yt.streams:
            if i.resolution != None:
                quality.append(i.resolution)
        quality = list(dict.fromkeys(quality))
        print('available resolutions;\n', quality)
        ress = input('choose a quality["...p"]: ')
        path = input('choose a folder path: ')
        print("Please Wait... ")
        yt.streams.filter(res=ress).first().download(path)
        print('Downloaded!')

    def mp3(yt):
        path = input('choose a folder path: ')
        (yt.streams.filter(only_audio=True))[0].download(path)
        old_name = yt.streams.first().default_filename[:-5]+".mp4"
        print("Loading... ")
        p = Path(path+f'\\'+old_name)
        p.rename(p.with_suffix('.mp3'))

    if choice == "mp3":
        mp3(yt)
    else:
        mp4(yt)


def playlist():
    def download_playlist(p):
        while True:
            choice = input("mp4 or mp3: ")
            if choice in ['mp3', 'mp4']:
                break
        path = input('choose a folder path: ')
        print('Playlist name : '+p.title)

        def mp4(p, path):
            print('The videos will be downloaded on the highest resolution!')
            for video in p.videos:
                try:
                    video.streams.first().download(path)
                except Exception as e:
                    print(e,type(e))
                print("[ "+video.title+" ] is downloading...")
                old_name = video.streams.first().default_filename
                p = Path(path+f'\\'+old_name)
                p.rename(p.with_suffix('.mp4'))

            print("Playlist is Downloaded")

        def mp3(yt, path):
            for video in yt.videos:
                (video.streams.filter(only_audio=True))[0].download(path)
                old_name = video.streams.first().default_filename[:-5]+".mp4"
                print("[ "+video.title+" ] is downloading...")
                p = Path(path+f'\\'+old_name)
                p.rename(p.with_suffix('.mp3'))
            print("Playlist is Downloaded")
        if choice == "mp3":
            mp3(p, path)
        else:
            mp4(p, path)
    link = input("What is the url of the playlist you want to download : ")
    p = Playlist(link)
    download_playlist(p)


def stream():
    yt = YouTube(input("What is the url of the stream you want to download : "))
    while True:
        choice = input("mp4 or mp3: ")
        if choice in ['mp3', 'mp4']:
            break

    def mp4(yt):
        quality = []
        for i in yt.streams:
            if i.resolution != None:
                quality.append(i.resolution)
        quality = list(dict.fromkeys(quality))
        print('available resolutions;\n', quality)
        ress = input('choose a quality["...p"]: ')
        path = input('choose a folder path: ')
        print("The video is downloading until the stream is closed")
        yt.streams.filter(res=ress).first().download(path)
        print('Downloaded!')

    def mp3(yt):
        path = input('choose a folder path: ')
        (yt.streams.filter(only_audio=True))[0].download(path)
        old_name = yt.streams.first().default_filename[:-5]+".mp4"
        print("The video is downloading until the stream is closed")
        p = Path(path+f'\\'+old_name)
        p.rename(p.with_suffix('.mp3'))

    if choice == "mp3":
        mp3(yt)
    else:
        mp4(yt)



if __name__ == "__main__" :
    if choice == '1':
        video()
    elif choice == '2':
        playlist()
    else:
        stream()
