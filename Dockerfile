FROM python:3.11-slim

# Cài libGL để OpenCV hoạt động
RUN apt-get update && apt-get install -y libgl1


# Tạo thư mục app
WORKDIR /app

# Copy code vào container
COPY . .

# Cài thư viện Python
RUN pip install --no-cache-dir -r requirements.txt

# Chạy app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
