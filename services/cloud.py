# services/cloud.py
from supabase import create_client
import os

# Kết nối Supabase
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Hàm upload file lên Supabase Storage
def upload_to_supabase(bucket: str, path: str, data: bytes, mime: str):
    supabase.storage.from_(bucket).upload(path, data, {"content-type": mime})
