from pytube import YouTube
print("Enter the YouTube video link")
link=input()
yt = YouTube(link)
lst=[]
lst1=[]
lst2=[]
for i in yt.streams.filter(progressive=True):
    lst.append(i)
for i in yt.streams.filter(only_video=True, subtype="mp4"):
    lst1.append(i)
for i in yt.streams.filter(only_audio=True, subtype="mp4"):
    lst2.append(i)
print("Enter the stream number you want to download. Type -1 for more options")
for i in range(len(lst)):
    print(i,"-", lst[i].fps,"fps", lst[i].resolution, lst[i].mime_type, lst[i].abr,yt.streams.get_by_itag(lst[i].itag).filesize/1024/1024,"MB")
sn=int(input())
if sn==-1:
    print("Enter 1 to download both audio and video seperately\nEnter 2 to download only video\nEnter 3 to download only audio")
    op=int(input())
    if op==2:
        for i in range(len(lst1)):
            print(i,"-", lst1[i].fps,"fps", lst1[i].resolution, lst1[i].mime_type, yt.streams.get_by_itag(lst1[i].itag).filesize/1024/1024,"MB")
        vs=int(input())
        print("What should be the name?")
        vd=input()
        yt.streams.get_by_itag(lst1[vs].itag).download(filename=vd)
    elif op==3:
        print("Select the audio file")
        for i in range(len(lst2)):
            print(i,"-", lst2[i].fps,"fps", lst2[i].mime_type, lst2[i].abr, yt.streams.get_by_itag(lst2[i].itag).filesize/1024/1024,"MB")
        ms=int(input())
        print("What should be the name?")
        ad=input()
        yt.streams.get_by_itag(lst2[ms].itag).download(filename=ad)
    elif op==1:
        print("Select the video resolution and type")
        for i in range(len(lst1)):
            print(i,"-", lst1[i].fps,"fps", lst1[i].resolution, lst1[i].mime_type, yt.streams.get_by_itag(lst1[i].itag).filesize/1024/1024,"MB")
        vs=int(input())
        print("What should be the name?")
        vd=input()
        yt.streams.get_by_itag(lst1[vs].itag).download(filename=vd)
        print("Select the audio file")
        for i in range(len(lst2)):
            print(i,"-", lst2[i].fps,"fps", lst2[i].mime_type, lst2[i].abr, yt.streams.get_by_itag(lst2[i].itag).filesize/1024/1024,"MB")
        ms=int(input())
        print("What should be the name?")
        ad=input()
        yt.streams.get_by_itag(lst2[ms].itag).download(filename=ad)
else:
    print("Enter the file name you want to have for the video")
    fn=input()
    yt.streams.get_by_itag(lst[sn].itag).download(filename=fn)