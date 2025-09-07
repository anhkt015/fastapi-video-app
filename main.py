from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from routers import process
import os
import uvicorn

app = FastAPI()

# Mount thư mục static để phục vụ ảnh/video nếu cần
app.mount("/static", StaticFiles(directory="static"), name="static")

# Kết nối router xử lý video
app.include_router(process.router)

# Cấu hình thư mục chứa HTML
templates = Jinja2Templates(directory="templates")

# Route giao diện upload video
@app.get("/upload", response_class=HTMLResponse)
def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

# Route kiểm tra app đang chạy
@app.get("/")
def home():
    return {"status": "App is running"}

# Chạy app nếu gọi trực tiếp
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
