from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBearer
from fastapi.openapi.utils import get_openapi
from routers import process
import os
import uvicorn

# Khởi tạo app
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

# Kích hoạt Swagger bảo mật
app.openapi = custom_openapi
from routers import auth
app.include_router(auth.router)


# Chạy app nếu gọi trực tiếp
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
