from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

def send_images_to_copilot(image_list):
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument(r"user-data-dir=C:\Users\Dell\AppData\Local\Google\Chrome\User Data")
    options.add_argument("profile-directory=Default")

    driver = webdriver.Chrome(options=options)
    driver.get("https://copilot.microsoft.com/")
    time.sleep(30)

    for path, _ in image_list:
        try:
            upload = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
            if os.path.exists(path):
                upload.send_keys(os.path.abspath(path))
                time.sleep(5)
        except Exception as e:
            print(f"Lỗi gửi ảnh {path}: {e}")
