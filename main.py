from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBearer
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from routers import process, auth
import requests
import os
import uvicorn

# Khởi tạo app
app = FastAPI()

# Mount thư mục static để phục vụ ảnh/video nếu cần
app.mount("/static", StaticFiles(directory="static"), name="static")

# Kết nối router xử lý video và đăng nhập
app.include_router(process.router)
app.include_router(auth.router)

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

# Endpoint mới: xử lý ảnh gửi từ frontend → gọi Tiny VLMs Lab
class AnalyzeRequest(BaseModel):
    image_url: str
    question: str

@app.post("/analyze")
def analyze_image(req: AnalyzeRequest):
    payload = {
        "data": [req.image_url, req.question]
    }

    try:
        res = requests.post(
            "https://hf.space/embed/prithivMLmods/Tiny-VLMs-Lab/api/predict",
            json=payload
        )

        # Kiểm tra phản hồi HTTP
        if res.status_code != 200:
            return {"answer": f"Lỗi HTTP {res.status_code}: {res.text}"}

        # Kiểm tra phản hồi JSON
        try:
            result = res.json()
            answer = result["data"][0] if "data" in result else "Không có kết quả"
        except Exception as json_err:
            return {
                "answer": f"Lỗi JSON: {str(json_err)}",
                "raw_response": res.text
            }

    except Exception as e:
        return {"answer": f"Lỗi khi gọi mô hình: {str(e)}"}

    return {"answer": answer}

# Cấu hình Swagger để hiển thị nút Authorize
security = HTTPBearer()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI",
        version="0.1.0",
        description="API xử lý video",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Cho phép frontend gọi API từ localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # hoặc ["*"] nếu bạn muốn mở rộng
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Chạy app nếu gọi trực tiếp
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)


