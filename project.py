from __future__ import unicode_literals
from pytube import YouTube
import re

#main function
def main():
    user_url = input('Youtube URL: ')

    choice = input("PLease choose between Video complete or Audio only: ").lower()

    if choice  == 'Video complete' or choice == 'video complete' or choice == 'video' or choice=='v' or choice=='v c' or choice=='vc':
         print(downloader_full(user_url))
    elif choice  == 'audio' or choice == 'audio only' or choice == 'Audio only' or choice=='a':
        print(downloader_audio(user_url))
    else:
        print('Please choose one of the option above!')


def youtube_link(link):

     if match := re.search( r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w-]+',link):
        youtube =  match.group(0)
        return youtube
     else:
         return None


# the downloader function

def downloader_full(link):

    if  youtube_link(link):

        yt = YouTube(link)

        yt.streams.filter(only_audio=True).all()
        stream = yt.streams.get_by_itag(22)
        return stream.download()
    else:
        return None



def downloader_audio(link):
    if youtube_link(link):
        yt = YouTube(link)

        stream = yt.streams.filter(only_audio=True).first()

        return stream.download()
    else:
        return None






if __name__ == "__main__":
    main()
