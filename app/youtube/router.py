from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from typing import Union

from app.youtube.main import download_youtube_video
from app.model import youtubeRequest

router = APIRouter()

@router.post("/download")
def download_video(request: youtubeRequest, response: Response):
        video_url = request.url

    # try:
        # Download the YouTube video
        video_data, video_name = download_youtube_video(video_url)

        # Set the response headers
        response.headers["Content-Disposition"] = f"attachment; filename={video_name}.mp4"
        response.headers["Content-Type"] = "video/mp4"

        # Return the video binary data and name as the response content
        return {"video_name": video_name, "video_data": video_data}
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))