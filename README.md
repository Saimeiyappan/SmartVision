
# 🧠 SmartVision
### Intelligent Multi-Class Object Recognition System

<p align="center">

**An end-to-end Computer Vision project combining CNN-based Image Classification and YOLO11 Object Detection into an interactive Streamlit application.**

</p>

---

## 🚀 Project Overview

**SmartVision** is an end-to-end Artificial Intelligence and Computer Vision project designed to recognize and detect objects from images.

The project combines two major computer vision tasks:

🧠 **Image Classification**  
🎯 **Multi-Object Detection**

The classification module uses trained CNN models to identify the main object in an image, while the detection module uses **YOLO11** to identify multiple objects and localize them using bounding boxes.

The complete workflow covers:

```text
📂 Data
   ↓
🔍 Data Understanding
   ↓
🧹 Data Cleaning & Preprocessing
   ↓
🧠 CNN Model Training
   ↓
📊 Model Evaluation
   ↓
🎯 Object Detection Data Preparation
   ↓
🤖 YOLO11 Training
   ↓
📈 Model Testing
   ↓
🚀 Deployment
   ↓
🌐 Streamlit Application
````

---

# ✨ Key Features

### 🧠 Image Classification

SmartVision uses two trained CNN models:

* ⚡ EfficientNetB0
* 📱 MobileNetV2

The classification interface provides:

* 📤 Image upload
* 🖼️ Image preview
* 🔮 Predicted class
* 📊 Confidence score
* 🏆 Top-5 predictions
* ⚖️ Model prediction comparison
* 🤝 Model agreement information

---

### 🎯 Object Detection

SmartVision uses a trained **YOLO11** model for object detection.

Features include:

* 📤 Image upload
* 🖼️ Input image preview
* 🔍 Object detection
* 📦 Bounding-box visualization
* 🏷️ Object class identification
* 📊 Confidence scores
* 🔢 Number of detected objects
* 📋 Detection summary

---

# 🧩 Overall System Architecture

```text
                         🧠 SMARTVISION
                              │
                              ▼
                       📤 Input Image
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
        🧠 CLASSIFICATION           🎯 DETECTION
                 │                         │
        ┌────────┴────────┐                │
        │                 │                │
        ▼                 ▼                ▼
 EfficientNetB0      MobileNetV2       YOLO11
        │                 │                │
        ▼                 ▼                ▼
   Class +           Class +        Multiple Objects
 Confidence         Confidence       + Bounding Boxes
        │                 │                │
        └────────┬────────┘                │
                 │                         │
                 └────────────┬────────────┘
                              ▼
                     🌐 Streamlit UI
                              │
                              ▼
                     📊 User Results
```

---

# 🔄 Complete Project Workflow

## 1️⃣ Data Understanding

The project begins with understanding the image datasets and their structure.

Tasks include:

* 📂 Dataset inspection
* 🔎 Class analysis
* 📊 Exploratory data analysis
* 🖼️ Image inspection
* ⚠️ Data quality analysis

---

## 2️⃣ Data Preprocessing

The image datasets are prepared for deep learning.

The preprocessing workflow includes:

```text
Raw Images
    ↓
Image Validation
    ↓
Data Cleaning
    ↓
Class Organization
    ↓
Train / Validation / Test
    ↓
Image Transformation
```

---

## 3️⃣ CNN Classification

Two CNN architectures were trained for image classification:

```text
                    Classification
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
      ⚡ EfficientNetB0        📱 MobileNetV2
             │                       │
             └───────────┬───────────┘
                         ▼
                  Class Prediction
                         │
                         ▼
                  Confidence Score
```

The trained checkpoints are:

```text
models/cnn/EfficientNet_exp_1.pth
models/cnn/mobilenet_v2_best.pth
```

---

## 4️⃣ CNN Model Evaluation

The trained classification models were evaluated using the prepared test data.

The actual verified classification accuracy obtained during the project evaluation was:

> 🎯 **66.46%**

This README reports the **actual obtained result**, rather than the expected performance targets mentioned in the project specification.

---

## 5️⃣ Detection Data Preparation

A separate detection dataset was prepared for YOLO-based object detection.

The workflow included:

```text
Detection Dataset
       ↓
Data Cleaning
       ↓
Annotation Validation
       ↓
YOLO Format Preparation
       ↓
Train / Validation / Test
```

---

## 6️⃣ YOLO11 Object Detection

The cleaned detection dataset was used to train the YOLO11 object detection model.

YOLO11 provides:

```text
📦 Bounding Box
      +
🏷️ Class Label
      +
📊 Confidence Score
```

The trained model is stored as:

```text
models/yolo/YOLO11_best.pt
```

---

## 7️⃣ YOLO11 Testing

The trained YOLO11 model was tested on unseen images.

Example workflow:

```text
Test Image
    ↓
YOLO11
    ↓
Object Detection
    ↓
Bounding Boxes
    ↓
Class + Confidence
```

The trained model was successfully integrated into the deployment workflow and Streamlit application.

---

# 🌐 Streamlit Application

The final SmartVision application uses a multi-page Streamlit interface.

```text
🏠 Home
   │
   ├── 🖼️ Classification
   │
   ├── 🎯 Detection
   │
   ├── 📊 Model Performance
   │
   └── ℹ️ About
```

---

## 🏠 Home

The Home page provides:

* Project introduction
* SmartVision overview
* Main computer vision capabilities
* Navigation to different modules

---

## 🖼️ Classification

Users can upload an image and obtain predictions from:

```text
⚡ EfficientNetB0
        +
📱 MobileNetV2
```

The page displays:

* Predicted class
* Confidence
* Top-5 predictions
* Model comparison
* Model agreement

---

## 🎯 Detection

Users can upload an image and run YOLO11 inference.

The page displays:

* Input image
* Detected objects
* Bounding boxes
* Confidence scores
* Detection count
* Detection summary

---

## 📊 Model Performance

The performance page provides an overview of the available model evaluation results.

The actual verified classification accuracy is:

```text
🎯 66.46%
```

Performance values are displayed carefully so that project reference/expected values are not presented as achieved results.

---

## ℹ️ About

The About page explains:

* Project objective
* Computer vision workflow
* Models used
* Technologies
* Application structure
* Project capabilities

---

# 🤖 Models

| Model            | Task           | Purpose                          |
| ---------------- | -------------- | -------------------------------- |
| ⚡ EfficientNetB0 | Classification | Image classification             |
| 📱 MobileNetV2   | Classification | Lightweight image classification |
| 🎯 YOLO11        | Detection      | Multi-object detection           |

---

# 📁 Project Structure

```text
SmartVision/
│
├── 📂 data/
│   ├── raw/
│   └── processed/
│
├── 📂 models/
│   ├── cnn/
│   │   ├── EfficientNet_exp_1.pth
│   │   └── mobilenet_v2_best.pth
│   │
│   └── yolo/
│       └── YOLO11_best.pt
│
├── 📂 notebooks/
│   ├── 01_data_understanding_eda_preprocessing.ipynb
│   ├── 02_cnn_models_performance.ipynb
│   ├── 03_Detection_Data_Cleaning.ipynb
│   ├── 04_yolo_object_detection.ipynb
│   └── 05_deployment.ipynb
│
├── 📂 deployment/
│   ├── app.py
│   │
│   └── 📂 pages/
│       ├── 1_Classification.py
│       ├── 2_Detection.py
│       ├── 3_Model_Performance.py
│       └── 4_About.py
│
├── 📂 results/
│
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md
```

---

# 🛠️ Technology Stack

## 👨‍💻 Programming

* 🐍 Python

## 🧠 Machine Learning & Deep Learning

* PyTorch
* Torchvision
* Ultralytics YOLO
* CNN architectures

## 📊 Data Processing

* Pandas
* NumPy
* Matplotlib

## 🌐 Application Development

* Streamlit

## 💻 Development Tools

* VS Code
* Jupyter Notebook
* Git
* GitHub

---

# ⚙️ Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project:

```bash
cd SmartVision
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

From the SmartVision project root:

```bash
streamlit run deployment/app.py
```

The application will open in your browser.

---

# 📊 Verified Project Result

### 🧠 Classification

```text
Actual Classification Accuracy
              ↓
           66.46%
```

### 🎯 Object Detection

```text
YOLO11
   ↓
Successfully trained
   ↓
Successfully tested
   ↓
Successfully integrated
   ↓
Streamlit detection working
```

---

# 🎯 Project Objective

The primary objective of SmartVision is to demonstrate a complete end-to-end computer vision workflow:

```text
📂 Data Collection
      ↓
🔍 Data Understanding
      ↓
🧹 Data Cleaning
      ↓
🖼️ Image Preprocessing
      ↓
🧠 Deep Learning
      ↓
📊 Evaluation
      ↓
🎯 Object Detection
      ↓
🚀 Deployment
      ↓
🌐 Interactive AI Application
```

The project demonstrates how multiple computer vision models can be integrated into a single practical AI application.

---

# 🚀 Future Improvements

Possible future improvements include:

* 📈 Improving classification accuracy
* 🧠 Further CNN experimentation
* 🎯 Improving YOLO detection performance
* ⚡ GPU-optimized inference
* 📱 Mobile-friendly deployment
* ☁️ Cloud deployment optimization
* 📊 More detailed evaluation dashboards
* 🔄 Continuous model improvement

---

# 🏁 Project Status

| Component                     | Status      |
| ----------------------------- | ----------- |
| 📊 Data Understanding         | ✅ Completed |
| 🧹 Data Preprocessing         | ✅ Completed |
| 🧠 CNN Classification         | ✅ Completed |
| 📈 CNN Evaluation             | ✅ Completed |
| 🎯 Detection Data Preparation | ✅ Completed |
| 🤖 YOLO11 Training            | ✅ Completed |
| 🔍 YOLO11 Testing             | ✅ Completed |
| 🚀 Deployment Workflow        | ✅ Completed |
| 🌐 Streamlit Application      | ✅ Completed |
| 📱 Multi-Page Interface       | ✅ Completed |
| 📖 Documentation              | ✅ Completed |

---

# 💡 Final Note

**SmartVision** brings together data processing, deep learning, computer vision, model evaluation and deployment into one end-to-end AI project.

From raw image data to a working interactive AI application:

```text
          📂 DATA
             ↓
        🧹 CLEANING
             ↓
        🧠 TRAINING
             ↓
        📊 EVALUATION
             ↓
        🤖 AI MODELS
             ↓
        🚀 DEPLOYMENT
             ↓
      🌐 SMARTVISION APP
```

### Built as an end-to-end AI/ML Computer Vision project.

