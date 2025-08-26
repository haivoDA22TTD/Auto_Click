import pyautogui
import time

def auto_click(interval=0.5, duration=10):
    print(f"[⏳] Sẽ bắt đầu click sau 5 giây...")
    time.sleep(5)

    print(f"[🖱] Đang click chuột mỗi {interval} giây trong {duration} giây...")
    start_time = time.time()
    while time.time() - start_time < duration:
        pyautogui.click()
        time.sleep(interval)

    print("[✅] Đã hoàn thành auto click.")

if __name__ == "__main__":
    try:
        interval = float(input("Nhập thời gian giữa mỗi click (giây): ").strip())
        duration = float(input("Nhập tổng thời gian click (giây): ").strip())
        auto_click(interval=interval, duration=duration)
    except KeyboardInterrupt:
        print("\n[⛔] Đã dừng bởi người dùng.")
