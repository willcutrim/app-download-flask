from pytube import YouTube

def get_informcao_video(url):
    yt = YouTube(url)
    resolutions = [stream.resolution for stream in yt.streams.filter(progressive=True)]
    thumbnail = yt.thumbnail_url
    title = yt.title

    return resolutions, thumbnail, title