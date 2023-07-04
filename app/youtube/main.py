import io
import pytube

def download_youtube_video(video_url, resolution='720p'):
    try:
        youtube = pytube.YouTube(video_url)
        video_streams = youtube.streams.filter(progressive=True, file_extension='mp4')
        video = video_streams.get_by_resolution(resolution)
        if not video:
            raise Exception(f"No stream found for resolution: {resolution}")
        video_data = video.stream_to_buffer()
        video_name = video.title
        return video_data.getvalue(), video_name
    except Exception as e:
        raise Exception("Failed to download video: " + str(e))