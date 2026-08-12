# ============================================================
# SmartVision - YOLO11 Object Detection
# Part 1: Imports, configuration, model loading and helpers
# ============================================================

import streamlit as st
from pathlib import Path
from PIL import Image
from ultralytics import YOLO


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartVision - Detection",
    page_icon="🎯",
    layout="wide"
)


# ============================================================
# 2. PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "yolo"
    / "YOLO11_best.pt"
)


# ============================================================
# 3. PAGE HEADER
# ============================================================

st.title("🎯 SmartVision - YOLO11 Object Detection")

st.write(
    "Upload an image and use the trained YOLO11 model "
    "to detect multiple objects with bounding-box visualization."
)


# ============================================================
# 4. MODEL INFORMATION
# ============================================================

st.subheader("🤖 YOLO11 Detection Model")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Model",
        "YOLO11"
    )

with col2:
    st.metric(
        "Task",
        "Object Detection"
    )

with col3:
    st.metric(
        "Output",
        "Bounding Boxes"
    )


st.divider()


# ============================================================
# 5. LOAD YOLO11 MODEL
# ============================================================

@st.cache_resource
def load_yolo_model():

    if not MODEL_PATH.exists():

        raise FileNotFoundError(
            f"YOLO11 model not found:\n{MODEL_PATH}"
        )

    model = YOLO(
        str(MODEL_PATH)
    )

    return model


try:

    model = load_yolo_model()

    st.success(
        "✅ YOLO11 model loaded successfully!"
    )

except Exception as e:

    st.error(
        f"❌ Failed to load YOLO11 model:\n\n{e}"
    )

    st.stop()


# ============================================================
# 6. DISPLAY MODEL PATH
# ============================================================

with st.expander("📁 Model Information"):

    st.write(
        "Trained YOLO11 model:"
    )

    st.code(
        str(MODEL_PATH)
    )

    st.write(
        f"Model file exists: "
        f"**{MODEL_PATH.exists()}**"
    )


st.divider()

# ============================================================
# 7. IMAGE UPLOAD
# ============================================================

st.subheader("📤 Upload an Image")

uploaded_file = st.file_uploader(
    "Choose an image for object detection",
    type=["jpg", "jpeg", "png", "webp"]
)


# ============================================================
# 8. IMAGE PREVIEW
# ============================================================

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")

    st.subheader("🖼️ Input Image")

    image_col1, image_col2, image_col3 = st.columns(
        [1, 2, 1]
    )

    with image_col2:

        st.image(
            image,
            caption="Input Image",
            use_container_width=True
        )

    st.divider()


    # ========================================================
    # 9. DETECTION BUTTON
    # ========================================================

    detect_button = st.button(
        "🎯 Detect Objects",
        type="primary",
        use_container_width=True
    )


    if detect_button:

        with st.spinner(
            "YOLO11 is detecting objects..."
        ):

            results = model.predict(
                source=image,
                conf=0.25,
                verbose=False
            )


        result = results[0]


        # ====================================================
        # 10. ANNOTATED IMAGE
        # ====================================================

        annotated_image = result.plot()

        st.subheader("🎯 Detection Result")

        result_col1, result_col2, result_col3 = st.columns(
            [1, 2, 1]
        )

        with result_col2:

            st.image(
                annotated_image,
                caption="YOLO11 Detection Result",
                use_container_width=True
            )


        st.divider()


        # ====================================================
        # 11. DETECTION SUMMARY
        # ====================================================

        st.subheader("📊 Detection Summary")

        boxes = result.boxes

        if boxes is not None and len(boxes) > 0:

            detected_count = len(boxes)

            class_ids = (
                boxes.cls
                .cpu()
                .numpy()
                .astype(int)
            )

            confidences = (
                boxes.conf
                .cpu()
                .numpy()
            )

            class_names = result.names


            # -----------------------------------------------
            # Summary metrics
            # -----------------------------------------------

            metric_col1, metric_col2 = st.columns(2)

            with metric_col1:

                st.metric(
                    "Objects Detected",
                    detected_count
                )

            with metric_col2:

                average_confidence = (
                    confidences.mean() * 100
                )

                st.metric(
                    "Average Confidence",
                    f"{average_confidence:.2f}%"
                )


            st.divider()


            # =================================================
            # 12. INDIVIDUAL DETECTIONS
            # =================================================

            st.subheader("🔎 Detected Objects")

            for i, (
                class_id,
                confidence
            ) in enumerate(
                zip(
                    class_ids,
                    confidences
                ),
                start=1
            ):

                class_name = class_names[
                    int(class_id)
                ]

                detection_col1, detection_col2 = st.columns(
                    [2, 1]
                )

                with detection_col1:

                    st.write(
                        f"**{i}. {class_name}**"
                    )

                with detection_col2:

                    st.write(
                        f"{confidence * 100:.2f}%"
                    )


                st.progress(
                    float(confidence)
                )


        else:

            st.warning(
                "No objects were detected in this image "
                "with the current confidence threshold."
            )