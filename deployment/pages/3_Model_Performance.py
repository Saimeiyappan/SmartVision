# ============================================================
# SmartVision - Model Performance
# Part 1: Page setup and performance overview
# ============================================================

import streamlit as st


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartVision - Model Performance",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# 2. PAGE HEADER
# ============================================================

st.title("📊 SmartVision - Model Performance")

st.write(
    "Review the performance of the trained classification "
    "and object detection models used in SmartVision."
)


st.divider()


# ============================================================
# 3. PERFORMANCE OVERVIEW
# ============================================================

st.subheader("📈 Performance Overview")

st.info(
    """
    SmartVision uses two deep learning approaches:

    • CNN models for image classification
    • YOLO11 for object detection

    The sections below summarize the available model
    performance results.
    """
)


# ============================================================
# 4. MODEL CATEGORIES
# ============================================================

classification_col, detection_col = st.columns(2)


with classification_col:

    st.subheader("🧠 Image Classification")

    st.write(
        "CNN models classify an uploaded image into one "
        "of the trained object categories."
    )

    st.success(
        "EfficientNetB0"
    )

    st.success(
        "MobileNetV2"
    )


with detection_col:

    st.subheader("🎯 Object Detection")

    st.write(
        "YOLO11 detects multiple objects in an image and "
        "localizes them using bounding boxes."
    )

    st.success(
        "YOLO11"
    )


st.divider()


# ============================================================
# 5. CLASSIFICATION MODELS
# ============================================================

st.header("🧠 Classification Model Performance")

model1, model2 = st.columns(2)


with model1:

    st.subheader("⚡ EfficientNetB0")

    st.write(
        "Transfer-learning based CNN model used for "
        "multi-class image classification."
    )


with model2:

    st.subheader("📱 MobileNetV2")

    st.write(
        "Lightweight CNN model used for multi-class "
        "image classification."
    )


st.divider()


# ============================================================
# 6. YOLO11 PERFORMANCE
# ============================================================

st.header("🎯 YOLO11 Detection Performance")

st.write(
    "YOLO11 is used for object detection and provides "
    "bounding boxes, class predictions and confidence scores."
)

# ============================================================
# 7. ACTUAL CLASSIFICATION PERFORMANCE
# ============================================================

st.header("🧠 Classification Performance")

st.write(
    "Actual evaluation result obtained during the project."
)


accuracy_col1, accuracy_col2 = st.columns(2)


with accuracy_col1:

    st.subheader("⚡ Classification Model")

    st.metric(
        "Actual Accuracy",
        "66.46%"
    )


with accuracy_col2:

    st.subheader("📊 Evaluation Status")

    st.metric(
        "Result",
        "Completed"
    )


st.caption(
    "The reported accuracy represents the actual result "
    "obtained during project evaluation."
)


st.divider()


# ============================================================
# 8. YOLO11 PERFORMANCE
# ============================================================

st.header("🎯 YOLO11 Detection Performance")

st.write(
    "YOLO11 was successfully trained and integrated into "
    "the SmartVision deployment application."
)


yolo_col1, yolo_col2, yolo_col3 = st.columns(3)


with yolo_col1:

    st.metric(
        "Model",
        "YOLO11"
    )


with yolo_col2:

    st.metric(
        "Detection",
        "Completed"
    )


with yolo_col3:

    st.metric(
        "Deployment",
        "Working"
    )


st.info(
    "The final verified YOLO11 mAP, precision and recall "
    "values are not displayed here because we have not "
    "confirmed those metrics from the actual evaluation output."
)


st.divider()


# ============================================================
# 9. MODEL COMPARISON
# ============================================================

st.subheader("⚖️ SmartVision Model Overview")

comparison_data = {
    "Model": [
        "CNN Classification",
        "YOLO11 Detection"
    ],
    "Task": [
        "Image Classification",
        "Object Detection"
    ],
    "Verified Result": [
        "66.46% Accuracy",
        "Prediction Successfully Verified"
    ]
}

st.table(comparison_data)


st.divider()


# ============================================================
# 10. KEY OBSERVATIONS
# ============================================================

st.subheader("💡 Key Observations")

observation_col1, observation_col2 = st.columns(2)


with observation_col1:

    st.success(
        """
        **CNN Classification**

        The trained classification model achieved
        an actual accuracy of 66.46% during evaluation.
        """
    )


with observation_col2:

    st.success(
        """
        **YOLO11 Detection**

        The trained YOLO11 model successfully performs
        object detection with bounding-box visualization
        in the Streamlit application.
        """
    )