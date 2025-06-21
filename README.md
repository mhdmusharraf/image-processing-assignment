# 🖼️ Image Processing Assignment

A small collection of Python scripts to demonstrate basic image‐processing operations.

---

## ✨ Features

1. **Intensity Reduction**  
   Reduce 256 gray levels to any power-of-2 levels (2–256).

2. **Spatial Averaging**  
   Apply a k×k box filter (e.g., 3×3, 10×10, 20×20).

3. **Rotation**  
   Rotate an image by any angle (commonly 45° or 90°).

4. **Block Averaging**  
   Perform non-overlapping block-wise averaging (e.g., 3×3, 5×5, 7×7).

---

## 📁 Project Structure

plaintext
image_processing_assignment/
├── .gitignore
├── README.md
├── requirements.txt
├── images/
│   └── input.jpg          # Put your test image here
├── results/               # Output images will be saved here
└── src/
    ├── intensity_reduction.py
    ├── spatial_filter_average.py
    ├── rotate_image.py
    └── block_average.py


---

## 🚀 Prerequisites

- **Python 3.7+**  
- **pip**  
- A terminal (VS Code integrated terminal recommended)

---

## ⚙️ Setup

1. **Clone or create** this folder on your machine.  
2. From the project root, create and activate a virtual environment:
bash
   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate

   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1