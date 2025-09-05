FROM python:3.11-slim

# Cài thư viện hệ thống cho OpenCV
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
