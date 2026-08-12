# ============================================================
# SmartVision - About
# ============================================================

import streamlit as st


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartVision - About",
    page_icon="ℹ️",
    layout="wide"
)


# ============================================================
# 2. PAGE HEADER
# ============================================================

st.title("ℹ️ About SmartVision")

st.write(
    "SmartVision is an AI-powered computer vision system "
    "designed for image classification and multi-object detection."
)

st.divider()


# ============================================================
# 3. PROJECT OVERVIEW
# ============================================================

st.header("📌 Project Overview")

st.write(
    """
    SmartVision combines deep learning based image classification
    and object detection into a single interactive application.

    The system allows users to upload an image and either classify
    the main object present in the image or detect multiple objects
    together with their locations and confidence scores.
    """
)


# ============================================================
# 4. WHAT SMARTVISION CAN DO
# ============================================================

st.header("🚀 What SmartVision Can Do")

feature_col1, feature_col2 = st.columns(2)


with feature_col1:

    st.subheader("🧠 Image Classification")

    st.write(
        """
        The classification module uses trained CNN models to
        identify objects from the supported object categories.

        The application compares predictions from:

        • EfficientNetB0
        • MobileNetV2

        Each model provides a predicted class and confidence score.
        """
    )


with feature_col2:

    st.subheader("🎯 Object Detection")

    st.write(
        """
        The detection module uses the trained YOLO11 model to
        identify multiple objects within an image.

        The results include:

        • Detected object classes
        • Bounding boxes
        • Confidence scores
        • Total number of detected objects
        """
    )


st.divider()


# ============================================================
# 5. TECHNOLOGIES USED
# ============================================================

st.header("🛠️ Technologies Used")

tech_col1, tech_col2, tech_col3 = st.columns(3)


with tech_col1:

    st.subheader("🐍 Programming")

    st.write(
        """
        • Python
        • NumPy
        • Pandas
        """
    )


with tech_col2:

    st.subheader("🤖 AI / ML")

    st.write(
        """
        • PyTorch
        • Torchvision
        • Ultralytics YOLO
        • CNN architectures
        """
    )


with tech_col3:

    st.subheader("🌐 Application")

    st.write(
        """
        • Streamlit
        • Multi-page interface
        • Image upload
        • Real-time inference
        """
    )


st.divider()


# ============================================================
# 6. MODELS USED
# ============================================================

st.header("🤖 Models Used")

model_col1, model_col2, model_col3 = st.columns(3)


with model_col1:

    st.info(
        """
        **EfficientNetB0**

        Used for image classification.
        """
    )


with model_col2:

    st.info(
        """
        **MobileNetV2**

        Used for image classification.
        """
    )


with model_col3:

    st.info(
        """
        **YOLO11**

        Used for multi-object detection.
        """
    )


st.divider()


# ============================================================
# 7. APPLICATION PAGES
# ============================================================

st.header("📱 Application Pages")

pages_col1, pages_col2 = st.columns(2)


with pages_col1:

    st.write(
        """
        **🏠 Home**

        Introduction and overview of SmartVision.

        **🖼️ Classification**

        Upload an image and compare CNN predictions.

        **🎯 Detection**

        Upload an image and detect multiple objects
        using YOLO11.
        """
    )


with pages_col2:

    st.write(
        """
        **📊 Model Performance**

        Review the available model evaluation results.

        **ℹ️ About**

        Project overview, technologies, models and
        application information.
        """
    )


st.divider()


# ============================================================
# 8. PROJECT OBJECTIVE
# ============================================================

st.header("🎯 Project Objective")

st.write(
    """
    The objective of SmartVision is to demonstrate how
    deep learning based computer vision models can be
    integrated into a practical application.

    The project combines image classification and object
    detection into one user-friendly interface, allowing
    users to interact with trained AI models without
    directly working with the underlying machine learning
    code.
    """
)


st.divider()


# ============================================================
# 9. PROJECT WORKFLOW
# ============================================================

st.header("🔄 SmartVision Workflow")

st.code(
    """
Image Input
     │
     ├───────────────┐
     │               │
     ▼               ▼
Classification    Detection
     │               │
     ▼               ▼
CNN Models        YOLO11
     │               │
     ▼               ▼
Class +           Objects +
Confidence        Bounding Boxes
     │               │
     └───────┬───────┘
             ▼
      Streamlit Results
    """,
    language="text"
)


# ============================================================
# 10. PROJECT STATUS
# ============================================================

st.header("✅ Project Status")

status_col1, status_col2, status_col3 = st.columns(3)


with status_col1:

    st.success(
        "🧠 CNN Classification\n\nCompleted"
    )


with status_col2:

    st.success(
        "🎯 YOLO11 Detection\n\nCompleted"
    )


with status_col3:

    st.success(
        "🌐 Streamlit Application\n\nCompleted"
    )


st.divider()


# ============================================================
# 11. FINAL MESSAGE
# ============================================================

st.header("💡 SmartVision")

st.write(
    """
    SmartVision brings together data preparation, deep learning,
    computer vision, model evaluation and application deployment
    into a single end-to-end AI project.
    """
)

st.success(
    "Thank you for exploring SmartVision."
)