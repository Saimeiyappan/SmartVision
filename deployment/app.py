import streamlit as st


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="SmartVision",
    page_icon="🔍",
    layout="wide"
)


# ---------------------------------------------------------
# Main Title
# ---------------------------------------------------------

st.title("🔍 SmartVision")

st.subheader(
    "🤖 AI-Powered Image Classification & Object Detection"
)

st.write(
    "Welcome to SmartVision — an interactive computer vision "
    "application built using deep learning models."
)


st.divider()


# ---------------------------------------------------------
# Project Overview
# ---------------------------------------------------------

st.header("🚀 Project Overview")

st.write(
    "SmartVision is a computer vision application that combines "
    "image classification and object detection to analyze images "
    "using trained deep learning models."
)

st.info(
    "💡 Upload an image through the Classification or Detection "
    "page and let the trained AI models analyze it."
)


# ---------------------------------------------------------
# What Can SmartVision Do?
# ---------------------------------------------------------

st.header("✨ What Can SmartVision Do?")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🖼️ Image Classification")

    st.write(
        "Classify an input image using trained CNN models "
        "and obtain the predicted class."
    )

    st.success(
        "Models: EfficientNet & MobileNetV2"
    )


with col2:

    st.subheader("🎯 Object Detection")

    st.write(
        "Detect multiple objects inside an image using YOLO11 "
        "with bounding-box visualization."
    )

    st.success(
        "Model: YOLO11"
    )


st.divider()


# ---------------------------------------------------------
# AI Models Used
# ---------------------------------------------------------

st.header("🧠 AI Models Used")

model1, model2, model3 = st.columns(3)

with model1:

    st.caption("🖼️ Classification Model 1")

    st.subheader("EfficientNet")

    st.write(
        "Deep learning image classification model."
    )


with model2:

    st.caption("📱 Classification Model 2")

    st.subheader("MobileNetV2")

    st.write(
        "Lightweight image classification model."
    )


with model3:

    st.caption("🎯 Detection Model")

    st.subheader("YOLO11")

    st.write(
        "Real-time object detection model."
    )

# ---------------------------------------------------------
# How SmartVision Works
# ---------------------------------------------------------

st.divider()

st.header("⚙️ How SmartVision Works")

st.write(
    "SmartVision follows a simple image analysis workflow. "
    "Users provide an image, and the selected deep learning "
    "model processes the image to generate the final prediction."
)

step1, step2, step3, step4 = st.columns(4)

with step1:
    st.subheader("1️⃣ Upload")
    st.write(
        "Upload an image through the Classification "
        "or Detection page."
    )

with step2:
    st.subheader("2️⃣ Process")
    st.write(
        "The uploaded image is prepared and passed "
        "to the selected trained model."
    )

with step3:
    st.subheader("3️⃣ Predict")
    st.write(
        "The deep learning model analyzes the image "
        "and generates a prediction."
    )

with step4:
    st.subheader("4️⃣ Result")
    st.write(
        "The application displays the prediction "
        "in an easy-to-understand format."
    )


# ---------------------------------------------------------
# Classification & Detection
# ---------------------------------------------------------

st.divider()

st.header("🔬 SmartVision Analysis")

analysis1, analysis2 = st.columns(2)

with analysis1:

    st.subheader("🖼️ Image Classification")

    st.write(
        "The classification module uses trained CNN models "
        "to identify the class represented in an input image."
    )

    st.markdown(
        """
        **Available Models**

        - 🧠 EfficientNet
        - 📱 MobileNetV2

        **Output**

        - Predicted image class
        - Model confidence
        """
    )

    st.info(
        "Use the Classification page to upload an image "
        "and compare predictions from the trained CNN models."
    )


with analysis2:

    st.subheader("🎯 Object Detection")

    st.write(
        "The detection module uses the trained YOLO11 model "
        "to locate and identify objects inside an image."
    )

    st.markdown(
        """
        **Detection Features**

        - 🔍 Multiple object detection
        - 📦 Bounding-box visualization
        - 🎯 Object class identification
        - 📊 Confidence scores
        """
    )

    st.info(
        "Use the Detection page to upload an image and "
        "visualize detected objects with bounding boxes."
    )


# ---------------------------------------------------------
# Technology Stack
# ---------------------------------------------------------

st.divider()

st.header("🛠️ Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.metric("🐍 Language", "Python")

with tech2:
    st.metric("🧠 Classification", "CNN")

with tech3:
    st.metric("🎯 Detection", "YOLO11")

with tech4:
    st.metric("🌐 Interface", "Streamlit")


# ---------------------------------------------------------
# Application Navigation
# ---------------------------------------------------------

st.divider()

st.header("🧭 Application Navigation")

st.write(
    "Use the sidebar to explore the different components "
    "of the SmartVision application."
)

st.markdown(
    """
    **🖼️ Classification**

    Upload an image and obtain predictions from the trained
    EfficientNet and MobileNetV2 models.

    **🎯 Detection**

    Upload an image and detect objects using the trained YOLO11 model.

    **📊 Model Performance**

    Review the performance information of the trained models.

    **ℹ️ About**

    Learn more about the SmartVision project, dataset,
    models, and technologies used.
    """
)


# ---------------------------------------------------------
# Project Status
# ---------------------------------------------------------

st.divider()

st.header("📌 Project Status")

status1, status2, status3 = st.columns(3)

with status1:
    st.success("✅ CNN Models Ready")

with status2:
    st.success("✅ YOLO11 Model Ready")

with status3:
    st.success("✅ Streamlit Interface Ready")


# ---------------------------------------------------------
# Getting Started
# ---------------------------------------------------------

st.divider()

st.header("🚀 Getting Started")

st.write(
    "Ready to try SmartVision? Select a module from the "
    "sidebar and upload an image to begin."
)

st.info(
    "💡 Recommended: Start with the Classification page "
    "to explore the CNN models, or use Detection to see "
    "YOLO11 object detection with bounding boxes."
)


st.success(
    "🎉 SmartVision is ready for interactive image analysis!"
)