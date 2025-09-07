from fastapi import APIRouter, UploadFile
from services.video_processor import extract_frames
from services.filter_engine import filter_unique_images
from services.cloud import upload_to_supabase
import os
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@router.post("/process_video")
async def process_video(file: UploadFile):
    try:
        # Tạo thư mục lưu video
        upload_dir = "static/uploads"
        os.makedirs(upload_dir, exist_ok=True)
        video_path = os.path.join(upload_dir, file.filename)

        # Lưu video vào thư mục
        with open(video_path, "wb") as f:
            f.write(await file.read())
        logger.info(f"[UPLOAD] Video saved to {video_path}")

        # Tách frame từ video
        frame_paths = extract_frames(video_path)
        logger.info(f"[FRAME] Extracted {len(frame_paths)} frames")

        # Lọc ảnh chứa chữ
        unique_images = filter_unique_images(frame_paths)
        logger.info(f"[FILTER] Found {len(unique_images)} unique images")

        # Upload ảnh lên Supabase
        for i, img_path in enumerate(unique_images):
            with open(img_path, "rb") as f:
                upload_to_supabase(
                    bucket="processed",
                    path=f"frames/{file.filename}/frame_{i}.jpg",
                    data=f.read(),
                    mime="image/jpeg"
                )
        logger.info(f"[UPLOAD] Uploaded {len(unique_images)} images to Supabase")

        return {"results": unique_images}

    except Exception as e:
        logger.error(f"[ERROR] Failed to process video: {e}")
        return {"error": str(e)}
