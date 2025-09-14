# 🎥 FastAPI Video Analyzer by Nhật Anh

Một ứng dụng web sử dụng AI để phân tích nội dung từ video hoặc ảnh, được xây dựng bằng FastAPI, Supabase, và có giao diện thử nghiệm bằng Streamlit. Dự án hướng đến việc xử lý video thông minh, trích xuất nội dung, và tích hợp dễ dàng với các mô hình AI như BLIP, OCR, hoặc GPT-4 Vision.
Ý tưởng từ việc một số bài tập online không cho phép sự can thiệp của Ai , không cho copy paste và chỉ có thể bấm từng câu để trả lời , dựa vào đó tôi nhận ra chỉ có thể học bài hoặc chụp màn hình từng bức , từng câu để gửi Ai như vậy sẽ rất mất thời gian nên tôi đã tạo ra trang web chỉ cần quay video và gửi video trang web sẽ phân tích từ hàng ngàn frame trong video để lọc những ảnh trùng về nội dung , và sau đó đưa ra những bức ảnh thật sự khác biệt như 20 bức ảnh về 20 câu hỏi có trong video , không những thể còn rất nhiều ứng dụng như nhận diện 20 người khác nhau từ video chứa rất nhiều người. 

## 🚀 Demo trực tiếp

🔗 [Truy cập web tại đây](https://ai-image-app-frontend-super-anhkt015s-projects.vercel.app/)

---

## 🧱 Công nghệ sử dụng

| Thành phần       | Công nghệ            |
|------------------|----------------------|
| Backend API      | FastAPI (Python)     |
| AI Model         | Hugging Face API / Pytesseract |
| Media Storage    | Supabase Storage     |
| Database         | Supabase PostgreSQL  |
| Auth             | JWT (python-jose)    |
| Prototype UI     | Streamlit            |
| Deploy Backend   | Railway              |
| Deploy Frontend  | Vercel (React/Vite)  |

---

## 📦 Tính năng chính

- 📤 Upload video để xử lý nội dung , lọc ảnh trùng để chọn ra ảnh cần bằng imagehash/Pytesseract.
- 🧠 Phân tích ảnh hoặc URL ảnh bằng AI
- 🔄 Gửi request đến mô hình AI (BLIP, OCR, v.v.)
- 🗂 Quản lý dữ liệu video bằng Supabase
- 🔐 Xác thực người dùng bằng JWT
- 🧪 Giao diện thử nghiệm bằng Streamlit
- ⚡ Giao diện đơn giản, dễ dùng, responsive

---

## 📁 Cấu trúc thư mục

```bash
fastapi-video-app/
├── auth/               # Xử lý JWT
├── frame2/             # Xử lý khung hình video
├── routers/            # Các route API
├── services/           # Logic xử lý AI
├── static/uploads/     # Lưu video/ảnh tạm
├── templates/          # Giao diện HTML (nếu dùng Jinja2)
├── .env.example        # Biến môi trường mẫu
├── Dockerfile          # Cấu hình Docker
├── railway.json        # Cấu hình Railway
├── render.yaml         # Cấu hình Render (nếu dùng)
├── requirements.txt    # Thư viện Python
├── main.py             # Entry point FastAPI
