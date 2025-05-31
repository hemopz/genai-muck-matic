import torch
import cv2
import os
from pathlib import Path

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:/Final Year Project/AI/yolov5/runs/train/exp7/weights/best.pt', force_reload=True)

# Set confidence threshold
model.conf = 0.25

# Load test image or video
video_path = 'D:\Final Year Project\AI\inference_videos\lane_test_video_1.mp4'  # Replace with your video file

if not os.path.exists(video_path):
    print(f"[ERROR] Video file not found: {video_path}")
    exit()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"[ERROR] Failed to open video file: {video_path}")
    exit()


# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0: fps = 30  # Fallback to default

# Define output path
output_path = 'output_lane_detected.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

print(f"[INFO] Processing video: {video_path}")
print(f"[INFO] Saving output to: {output_path}")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB and run inference
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(img)

    # Render results on frame
    rendered_frame = results.render()[0]
    out.write(rendered_frame)
    cv2.imshow('Lane Detection', rendered_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()