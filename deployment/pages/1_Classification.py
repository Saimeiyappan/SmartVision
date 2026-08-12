# ============================================================
# SmartVision - Image Classification
# Part 1: Imports, Paths, Model Loading and Prediction Logic
# ============================================================

import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from pathlib import Path


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartVision - Classification",
    page_icon="🖼️",
    layout="wide"
)


# ============================================================
# 2. PROJECT PATH
# ============================================================

# File location:
# SmartVision/
# └── deployment/
#     └── pages/
#         └── 1_Classification.py

PROJECT_ROOT = Path(__file__).resolve().parents[2]


# ============================================================
# 3. MODEL PATHS
# ============================================================

EFFICIENTNET_PATH = (
    PROJECT_ROOT
    / "models"
    / "cnn"
    / "EfficientNet_exp_1.pth"
)

MOBILENET_PATH = (
    PROJECT_ROOT
    / "models"
    / "cnn"
    / "mobilenet_v2_best.pth"
)


# ============================================================
# 4. DEVICE
# ============================================================

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


# ============================================================
# 5. CLASS NAMES
# ============================================================

# Exact class order used in the trained CNN models

CLASS_NAMES = [
    "airplane",
    "bed",
    "bench",
    "bicycle",
    "bird",
    "bottle",
    "bowl",
    "bus",
    "cake",
    "car",
    "cat",
    "chair",
    "couch",
    "cow",
    "cup",
    "dog",
    "elephant",
    "horse",
    "motorcycle",
    "person",
    "pizza",
    "potted plant",
    "stop sign",
    "traffic light",
    "train",
    "truck"
]

NUM_CLASSES = len(CLASS_NAMES)


# ============================================================
# 6. IMAGE PREPROCESSING
# ============================================================

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# ============================================================
# 7. EFFICIENTNET MODEL
# ============================================================

def create_efficientnet():

    model = models.efficientnet_b0(
        weights=None
    )

    model.classifier[1] = nn.Linear(
        model.classifier[1].in_features,
        NUM_CLASSES
    )

    return model


# ============================================================
# 8. MOBILENETV2 MODEL
# ============================================================

def create_mobilenet():

    model = models.mobilenet_v2(
        weights=None
    )

    model.classifier[1] = nn.Linear(
        model.classifier[1].in_features,
        NUM_CLASSES
    )

    return model


# ============================================================
# 9. LOAD MODEL WEIGHTS
# ============================================================

@st.cache_resource
def load_models():

    efficientnet = create_efficientnet()
    mobilenet = create_mobilenet()

    # --------------------------------------------------------
    # EfficientNet
    # --------------------------------------------------------

    efficientnet_checkpoint = torch.load(
        EFFICIENTNET_PATH,
        map_location=DEVICE
    )

    if isinstance(efficientnet_checkpoint, dict) and "state_dict" in efficientnet_checkpoint:
        efficientnet.load_state_dict(
            efficientnet_checkpoint["state_dict"]
        )
    else:
        efficientnet.load_state_dict(
            efficientnet_checkpoint
        )


    # --------------------------------------------------------
    # MobileNetV2
    # --------------------------------------------------------

    mobilenet_checkpoint = torch.load(
        MOBILENET_PATH,
        map_location=DEVICE
    )

    if isinstance(mobilenet_checkpoint, dict) and "state_dict" in mobilenet_checkpoint:
        mobilenet.load_state_dict(
            mobilenet_checkpoint["state_dict"]
        )
    else:
        mobilenet.load_state_dict(
            mobilenet_checkpoint
        )


    # --------------------------------------------------------
    # Evaluation mode
    # --------------------------------------------------------

    efficientnet.to(DEVICE)
    mobilenet.to(DEVICE)

    efficientnet.eval()
    mobilenet.eval()

    return efficientnet, mobilenet


# ============================================================
# 10. IMAGE PREDICTION FUNCTION
# ============================================================

def predict_image(model, image):

    image_tensor = transform(image)

    image_tensor = image_tensor.unsqueeze(0)

    image_tensor = image_tensor.to(DEVICE)


    with torch.no_grad():

        outputs = model(image_tensor)

        probabilities = torch.softmax(
            outputs,
            dim=1
        )[0]


    # Top-5 predictions

    top_probabilities, top_indices = torch.topk(
        probabilities,
        k=min(5, NUM_CLASSES)
    )


    predictions = []

    for probability, index in zip(
        top_probabilities,
        top_indices
    ):

        class_name = CLASS_NAMES[
            index.item()
        ]

        confidence = probability.item()

        predictions.append(
            (
                class_name,
                confidence
            )
        )


    return predictions

# ============================================================
# 11. PAGE TITLE
# ============================================================

st.title("🖼️ SmartVision - Image Classification")

st.write(
    "Upload an image and compare predictions from "
    "EfficientNetB0 and MobileNetV2."
)


# ============================================================
# 12. LOAD MODELS
# ============================================================

try:

    efficientnet_model, mobilenet_model = load_models()

    st.success(
        "✅ Classification models loaded successfully!"
    )

except Exception as e:

    st.error(
        f"❌ Failed to load classification models:\n\n{e}"
    )

    st.stop()


# ============================================================
# 13. MODEL INFORMATION
# ============================================================

st.subheader("🤖 Available Classification Models")

col1, col2 = st.columns(2)

with col1:

    st.info(
        """
        **EfficientNetB0**

        • Transfer-learning CNN  
        • Optimized for accuracy  
        • Input size: 224 × 224  
        • Trained for 25 object classes
        """
    )


with col2:

    st.info(
        """
        **MobileNetV2**

        • Lightweight CNN  
        • Optimized for fast inference  
        • Input size: 224 × 224  
        • Trained for 25 object classes
        """
    )


st.divider()


# ============================================================
# 14. IMAGE UPLOADER
# ============================================================

st.subheader("📤 Upload an Image")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ]
)


# ============================================================
# 15. IMAGE PREVIEW
# ============================================================

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")


    st.subheader("🖼️ Uploaded Image")

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
    # 16. PREDICTION BUTTON
    # ========================================================

    analyze_button = st.button(
        "🔍 Analyze Image",
        type="primary",
        use_container_width=True
    )


    if analyze_button:

        with st.spinner(
            "Analyzing image with both CNN models..."
        ):

            efficientnet_predictions = predict_image(
                efficientnet_model,
                image
            )

            mobilenet_predictions = predict_image(
                mobilenet_model,
                image
            )


        # ====================================================
        # 17. GET TOP PREDICTIONS
        # ====================================================

        efficientnet_top_class = (
            efficientnet_predictions[0][0]
        )

        efficientnet_top_confidence = (
            efficientnet_predictions[0][1]
        )


        mobilenet_top_class = (
            mobilenet_predictions[0][0]
        )

        mobilenet_top_confidence = (
            mobilenet_predictions[0][1]
        )


        # ====================================================
        # 18. MAIN PREDICTION RESULTS
        # ====================================================

        st.subheader("🎯 Prediction Results")

        result_col1, result_col2 = st.columns(2)


        # ----------------------------------------------------
        # EfficientNet
        # ----------------------------------------------------

        with result_col1:

            st.markdown(
                "### 🟢 EfficientNetB0"
            )

            st.metric(
                label="Predicted Class",
                value=efficientnet_top_class
            )

            st.progress(
                efficientnet_top_confidence
            )

            st.write(
                f"Confidence: "
                f"**{efficientnet_top_confidence * 100:.2f}%**"
            )


        # ----------------------------------------------------
        # MobileNet
        # ----------------------------------------------------

        with result_col2:

            st.markdown(
                "### 🔵 MobileNetV2"
            )

            st.metric(
                label="Predicted Class",
                value=mobilenet_top_class
            )

            st.progress(
                mobilenet_top_confidence
            )

            st.write(
                f"Confidence: "
                f"**{mobilenet_top_confidence * 100:.2f}%**"
            )


        st.divider()


        # ====================================================
        # 19. MODEL AGREEMENT
        # ====================================================

        st.subheader("🤝 Model Comparison")


        if efficientnet_top_class == mobilenet_top_class:

            st.success(
                f"✅ Both models predict: "
                f"**{efficientnet_top_class}**"
            )

        else:

            st.warning(
                "⚠️ The models produced different predictions."
            )


        # ====================================================
        # 20. TOP-5 PREDICTIONS
        # ====================================================

        st.subheader("🏆 Top-5 Predictions")


        top5_col1, top5_col2 = st.columns(2)


        # ----------------------------------------------------
        # EfficientNet Top-5
        # ----------------------------------------------------

        with top5_col1:

            st.markdown(
                "### 🟢 EfficientNetB0"
            )

            for rank, (
                class_name,
                confidence
            ) in enumerate(
                efficientnet_predictions,
                start=1
            ):

                st.write(
                    f"**{rank}. {class_name}**"
                )

                st.progress(
                    confidence
                )

                st.caption(
                    f"{confidence * 100:.2f}%"
                )


        # ----------------------------------------------------
        # MobileNet Top-5
        # ----------------------------------------------------

        with top5_col2:

            st.markdown(
                "### 🔵 MobileNetV2"
            )

            for rank, (
                class_name,
                confidence
            ) in enumerate(
                mobilenet_predictions,
                start=1
            ):

                st.write(
                    f"**{rank}. {class_name}**"
                )

                st.progress(
                    confidence
                )

                st.caption(
                    f"{confidence * 100:.2f}%"
                )


        st.divider()


        # ====================================================
        # 21. FINAL RESULT
        # ====================================================

        st.subheader("📌 Final Classification Result")


        if (
            efficientnet_top_confidence
            >= mobilenet_top_confidence
        ):

            final_class = efficientnet_top_class
            final_confidence = efficientnet_top_confidence
            final_model = "EfficientNetB0"

        else:

            final_class = mobilenet_top_class
            final_confidence = mobilenet_top_confidence
            final_model = "MobileNetV2"


        st.success(
            f"""
            **Predicted Object:** {final_class}

            **Confidence:** {final_confidence * 100:.2f}%

            **Model:** {final_model}
            """
        )