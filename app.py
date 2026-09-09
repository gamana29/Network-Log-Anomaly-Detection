import streamlit as st
import pandas as pd
import numpy as np
import joblib


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Network Log Anomaly Detection",
    page_icon="🛡️",
    layout="wide"
)


# --------------------------------------------------
# Load Model
# --------------------------------------------------

@st.cache_resource
def load_model():
    return joblib.load(
        "models/isolation_forest_pipeline.joblib"
    )


try:
    model = load_model()
    model_loaded = True
except Exception:
    model = None
    model_loaded = False


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🛡️ Network Log Anomaly Detection")

st.markdown(
    """
    ### Machine Learning-Based Network Log Anomaly Detection

    This application uses an **Isolation Forest machine learning
    model** to identify potentially anomalous network traffic.
    """
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a section:",
    [
        "Home",
        "Dataset Analysis",
        "Anomaly Detection"
    ]
)


# --------------------------------------------------
# HOME
# --------------------------------------------------

if page == "Home":

    st.header("Project Overview")

    st.write(
        """
        This project uses Machine Learning to detect anomalous
        network traffic using the NSL-KDD dataset.

        The system analyzes network connection features and
        classifies traffic as Normal or Anomalous.
        """
    )

    st.subheader("Project Workflow")

    st.markdown(
        """
        **Network Logs**
        ↓
        **Data Preprocessing**
        ↓
        **Feature Encoding & Scaling**
        ↓
        **Isolation Forest**
        ↓
        **Anomaly Detection**
        ↓
        **Results**
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Dataset", "NSL-KDD")

    with col2:
        st.metric("Features", "41")

    with col3:
        st.metric("Detection Type", "Binary")

    st.subheader("Model Status")

    if model_loaded:
        st.success("✅ Machine Learning model loaded successfully.")
    else:
        st.error(
            "❌ Model not found. Run train_model.py first."
        )


# --------------------------------------------------
# DATASET ANALYSIS
# --------------------------------------------------

elif page == "Dataset Analysis":

    st.header("📊 Dataset Analysis")

    uploaded_file = st.file_uploader(
        "Upload a network log CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:

        data = pd.read_csv(uploaded_file)

        st.success("Dataset uploaded successfully!")

        st.subheader("Dataset Preview")

        st.dataframe(
            data.head(10),
            use_container_width=True
        )

        st.subheader("Dataset Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Rows",
                data.shape[0]
            )

        with col2:
            st.metric(
                "Columns",
                data.shape[1]
            )

        with col3:
            st.metric(
                "Missing Values",
                int(data.isnull().sum().sum())
            )

        st.subheader("Statistical Summary")

        st.dataframe(
            data.describe(),
            use_container_width=True
        )

        st.subheader("Column Information")

        column_info = pd.DataFrame({
            "Column": data.columns,
            "Data Type": data.dtypes.astype(str),
            "Missing Values": data.isnull().sum().values
        })

        st.dataframe(
            column_info,
            use_container_width=True
        )

    else:

        st.info(
            "Upload a CSV file to analyze the network dataset."
        )


# --------------------------------------------------
# ANOMALY DETECTION
# --------------------------------------------------

elif page == "Anomaly Detection":

    st.header("🚨 Anomaly Detection")

    if not model_loaded:

        st.error(
            """
            Model not found.

            Please run:

            `python src/train_model.py`
            """
        )

    else:

        st.success(
            "✅ Isolation Forest model is ready."
        )

        uploaded_file = st.file_uploader(
            "Upload network traffic CSV file",
            type=["csv"],
            key="prediction_file"
        )

        if uploaded_file is not None:

            data = pd.read_csv(uploaded_file)

            st.subheader("Uploaded Data")

            st.dataframe(
                data.head(10),
                use_container_width=True
            )

            # Remove columns that are not model features
            columns_to_drop = [
                "label",
                "difficulty",
                "is_anomaly"
            ]

            prediction_data = data.drop(
                columns=[
                    col for col in columns_to_drop
                    if col in data.columns
                ],
                errors="ignore"
            )

            try:

                predictions = model.predict(
                    prediction_data
                )

                anomaly_status = np.where(
                    predictions == 1,
                    "Normal",
                    "Anomaly"
                )

                result = data.copy()

                result["Prediction"] = anomaly_status

                st.subheader("Detection Results")

                st.dataframe(
                    result,
                    use_container_width=True
                )

                normal_count = (
                    anomaly_status == "Normal"
                ).sum()

                anomaly_count = (
                    anomaly_status == "Anomaly"
                ).sum()

                st.subheader("Detection Summary")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Total Records",
                        len(result)
                    )

                with col2:
                    st.metric(
                        "Normal",
                        normal_count
                    )

                with col3:
                    st.metric(
                        "Anomalies",
                        anomaly_count
                    )

                st.subheader("Anomaly Distribution")

                chart_data = pd.DataFrame({
                    "Status": [
                        "Normal",
                        "Anomaly"
                    ],
                    "Count": [
                        normal_count,
                        anomaly_count
                    ]
                })

                st.bar_chart(
                    chart_data.set_index("Status")
                )

                # Download results
                csv = result.to_csv(
                    index=False
                )

                st.download_button(
                    label="⬇️ Download Detection Results",
                    data=csv,
                    file_name="anomaly_detection_results.csv",
                    mime="text/csv"
                )

            except Exception as e:

                st.error(
                    f"Prediction failed: {e}"
                )

                st.warning(
                    """
                    Make sure the uploaded CSV contains the same
                    41 network traffic features used during training.
                    """
                )

        else:

            st.info(
                "Upload a CSV file to perform anomaly detection."
            )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Machine Learning-Based Network Log Anomaly Detection"
)