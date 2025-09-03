import cv2, os

def extract_frames(video_path, output_folder="frame2"):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    frame_paths = []
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        path = os.path.join(output_folder, f"{count:04d}.jpg")
        cv2.imwrite(path, frame)
        frame_paths.append(path)
        count += 1
    cap.release()
    return frame_paths
