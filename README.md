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

- 📤 Uppysse
   Ban đầu mình dùng OpenCV để trích frame, nhưng gặp vấn đề với hiệu suất và ảnh trùng lặp. Sau đó mình tích hợp `imagehash` để lọc ảnh gần giống, giúp giảm số lượng ảnh cần xử lý.

- **Tích hợp Supabase:**  
  Việc lưu video và metadata lên Supabase khá mới với mình. Mình phải học cách dùng bucket, tạo bảng `video_jobs`, và viết truy vấn SQL để lọc kết quả.

- **Gọi mô hình AI từ Hugging Face:**  
  Gặp lỗi xác thực API và giới hạn tốc độ. Mình đã viết hàm retry và xử lý lỗi để đảm bảo hệ thống không bị crash khi gọi model.

- **Triển khai backend lên Railway:**  
  Railway không hỗ trợ lưu file tạm nên mình phải cấu hình lại đường dẫn lưu ảnh và dùng Supabase làm storage chính.

- **JWT và bảo mật API:**  
  Việc tạo và kiểm tra token bằng `python-jose` khá phức tạp lúc đầu. Sau khi đọc tài liệu và test kỹ, mình đã viết module `jwt_handler.py` để tái sử dụng dễ dàng.

- **Giao diện thử nghiệm bằng Streamlit:**  
  Dù không phải UI chính, Streamlit giúp mình test nhanh mô hình AI và hiển thị kết quả trực quan trước khi tích hợp vào frontend React.

---

## 💡 Bài học rút ra

- Biết cách chia nhỏ hệ thống thành các phần độc lập: frontend, backend, AI, storage
- Hiểu rõ luồng xử lý video và ảnh trong môi trường thực tế
- Làm quen với Supabase, Railway, Hugging Face API, và Streamlit
- Viết README và tài liệu kỹ thuật rõ ràng để người khác dễ hiểu và đóng góp
---

## 🧠 Lessons Learned

- Cách xử lý ảnh trùng bằng imagehash và Pytesseract
- Tích hợp Supabase để lưu video và metadata
- Deploy backend bằng Railway và frontend bằng Vercel
- Viết API bảo mật bằng JWT và FastAPI

  ---
  
## 🛣 Roadmap

- [x] Upload video và trích frame
- [x] Lọc ảnh trùng bằng imagehash
- [x] Gửi ảnh đến AI model (BLIP, OCR)
- [ ] Tích hợp GPT-4 Vision
- [ ] Giao diện React đầy đủ
- [ ] Lưu lịch sử phân tích theo user

---

## 👨‍💻 Tác giả

**Nhật Anh**  
📧 Email: anhkt015@gmail.com
```

---
