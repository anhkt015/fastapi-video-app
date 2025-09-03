from fastapi import APIRouter, UploadFile
from services.video_processor import extract_frames
from services.filter_engine import filter_unique_images
import os
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@router.post("/process_video")
async def process_video(file: UploadFile):
    try:
        upload_dir = "static/uploads"
        os.makedirs(upload_dir, exist_ok=True)

        video_path = os.path.join(upload_dir, file.filename)
        with open(video_path, "wb") as f:
            f.write(await file.read())
        logger.info(f"[UPLOAD] Video saved to {video_path}")

        frame_paths = extract_frames(video_path)
        logger.info(f"[FRAME] Extracted {len(frame_paths)} frames")

        unique_images = filter_unique_images(frame_paths)
        logger.info(f"[FILTER] Found {len(unique_images)} unique images")

        return {"results": unique_images}
    except Exception as e:
        logger.error(f"[ERROR] Failed to process video: {e}")
        return {"error": str(e)}
