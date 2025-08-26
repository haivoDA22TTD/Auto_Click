# 🖱️ Auto Click Tool (Python)

Một công cụ auto click đơn giản viết bằng Python sử dụng thư viện `pyautogui`. Cho phép bạn tự động click chuột với thời gian tùy chỉnh.

---

## 📦 Tính năng

- Tự động click chuột trái
- Thiết lập thời gian giữa mỗi click
- Chạy trong khoảng thời gian bạn chỉ định
- Tạm dừng khởi động 5 giây để bạn đặt chuột đúng vị trí

---

## 🚀 Cài đặt & Sử dụng

### 1️⃣ Clone về máy

```bash
git clone https://github.com/haivoDA22TTD/Auto_Click.git
cd Auto-Click
```
### 2️⃣ Cài đặt thư viện cần thiết
```bash
pip install pyautogui
```
🪟 Windows

Không cần cài thêm gì.
```bash
python auto_click.py
```

🍎 Hướng dẫn chạy Auto Click Tool trên macOS

✅ Bước 1: Cài Python (nếu chưa có)

Mở Terminal và kiểm tra:
```bash
python3 --version
```

Nếu chưa có, cài từ: https://www.python.org/downloads/macos/

✅ Bước 2: Tạo môi trường ảo (tuỳ chọn)
```bash
python3 -m venv venv
source venv/bin/activate
```
✅ Bước 3: Cài pyautogui và các phụ thuộc
```bash
pip install pyautogui pyobjc
```

pyobjc là bắt buộc trên macOS để cho phép tương tác chuột & bàn phím.

✅ Bước 4: Cấp quyền điều khiển máy cho Terminal / Python

Đây là bước QUAN TRỌNG. Nếu không làm, tool sẽ không click được.

Vào:
System Settings (Cài đặt hệ thống) →
Privacy & Security →
Accessibility (Trợ năng)

Thêm quyền cho:

Terminal

Hoặc IDE bạn đang dùng (VSCode, PyCharm, etc.)

Hoặc /usr/bin/python3 nếu chạy bằng Python hệ thống

Bật checkbox "Allow the app to control your computer"

✅ Bước 5: Chạy tool
```bash
python3 auto_click.py
```

Sau 5 giây đếm ngược, chuột sẽ tự động click ở vị trí hiện tại.

🧯 Dừng tool:

Nhấn Ctrl + C trong Terminal

Hoặc di chuyển chuột đến góc trên bên trái màn hình (tọa độ 0,0) — sẽ tự động dừng nếu dùng tính năng an toàn
### 🐧 Hướng dẫn chạy trên Linux (Ubuntu/Debian-based)
✅ Bước 1: Cài Python (nếu chưa có)
```bash
sudo apt update
sudo apt install python3 python3-pip
```
✅ Bước 2: Cài các phụ thuộc cần thiết
```bash
sudo apt install scrot python3-tk python3-dev
```
✅ Bước 3: Cài pyautogui
```bash
pip3 install pyautogui
```
✅ Bước 4: Chạy tool
```bash
python3 auto_click.py
```
🧯 Dừng tool:

Nhấn Ctrl + C trong Terminal

Hoặc cài đặt vùng an toàn: đưa chuột về góc (0,0) để tắt tự động
