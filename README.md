# GENAI Muck-Matic 🧰

> A Smart AI-Driven Robotic Poultry Waste Collector

---

## 🚀 Overview

**GENAI Muck-Matic** is an autonomous robot designed for poultry farms to collect muck using AI-based lane detection and ROS coordination. It blends Mechatronics engineering with modern AI/ML technologies like YOLOv5, OpenCV, and Python to deliver a sustainable, smart, and effective cleaning solution.

---

## 🔮 Imagined Output

![GenAI Muck-Matic](genai-muck-matic.png)

  
---

## ✨ Features

* 🤖 **AI Lane Detection with YOLOv5** trained on 2500+ images
* 📊 **Real-Time Video Inference** using OpenCV & PyTorch
* 🧠 **ML/Deep Learning** integration with custom training pipeline
* 🌐 **ROS2 (Planned)** for task-level coordination and control
* ⚡ **ESP32 & ESP32-CAM Integration** (Planned for Edge Deployment)
* ☀️ **Solar Power Ready** for sustainable operation
* 🛠️ **Mechatronics Hardware** designed using SOLIDWORKS and for refrence

---

## 🔧 Setup & Execution

### Prerequisites

* Python 3.10.15 (ROS2 compatible)
* [YOLOv5 Repository](https://github.com/ultralytics/yolov5)
* Trained weights (`best.pt`) inside `models/`
* Test video stored in `tested-videos/`

### Installation

```bash
pip install -r requirements.txt
```

### Run Lane Detection

```bash
python scripts/lane_detection_inference.py
```

> This script processes a video frame-by-frame, overlays lane detections, and saves the output.

---

## 🧠 AI / ML & Deep Learning Usage

### ⚙️ Training Process

* Dataset: 2500+ labeled lane images via **Roboflow**
* Model: YOLOv5m (medium model for better accuracy)
* Environment: GPU (RTX 4060 with 6GB VRAM)

### ⚒️ Inference Engine

* Built with **PyTorch** + **OpenCV**
* Custom real-time video pipeline
* Output rendered with bounding boxes on live or pre-recorded video

### 🔧 AMP Compatibility Patch

To support PyTorch >=2.7:

```python
# OLD:
with torch.cuda.amp.autocast(amp):

# NEW:
with torch.amp.autocast(device_type='cuda', enabled=amp):
```

> This change was necessary to support my local setup with CUDA 12.1.

---

## 🧱 Project Structure

```
GENAI-Muck-Matic/
├── dataset/                 # Roboflow Export (YOLO format)
├── docs/                    # Project Report, Posters, Diagrams
├── hardware/                # 2D and 3D CAD Files
├── models/                  # Trained YOLOv5 weights
├── ros_ws/                  # ROS2 workspace (planned)
├── scripts/                 # Custom scripts including inference.py
├── tested-images/           # Screenshots of detection results
├── tested-videos/           # Raw and processed videos
├── yolov5/                  # YOLOv5 cloned repo (Ultralytics)
├── requirements.txt
└── README.md
```

---

## 👨‍💻 My Role

* Labeled & trained the dataset using **Roboflow + YOLOv5**
* Wrote a custom **OpenCV inference script** for lane tracking
* Helped to Design complete hardware mechanism in **SOLIDWORKS**
* Installed, debugged, and patched environment issues
* Tested the object detection model using custom images and videos to evaluate its performance in real-world poultry farm scenarios
* Created complete **GitHub documentation** & folder structure

---

## 💻 Tech Stack

| Layer           | Tools Used                   |
| --------------- | ---------------------------- |
| AI/ML           | YOLOv5, PyTorch, Roboflow    |
| Computer Vision | OpenCV                       |
| Microcontroller | ESP32, ESP32-CAM *(planned)* |
| Robotics        | ROS2 *(planned)*             |
| IDE/Platform    | VS Code, GitHub, Windows 11  |

---

## 🔮 Future Work

* Real-world test using ROS2 & ESP32 on robot
* Solar charging dock for autonomous runtime
* IoT dashboard to monitor battery & activity logs
* Imporved overall detection and path planning by training dataset of poultury farm walls 

---

## 📤 Contact

* 📧 Email: \[ID (hemandchindu2255@gmail.com)]
* 🔗 GitHub: [https://github.com/hemopz/genai-muck-matic](https://github.com/hemopz/genai-muck-matic)
* 💼 LinkedIn: [hemand-sreenivasan](www.linkedin.com/in/hemand-sreenivasan)

---

## 📄 License

This project is licensed under the [](LICENSE).

---

> ✨ Built with Mechatronics + IT and AI passion to solve real-world waste management challenges in poultry farms. 🚜💡


