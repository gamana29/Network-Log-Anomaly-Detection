import pandas as pd
import numpy as np
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import IsolationForest
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# --------------------------------------------------
# 1. Column names
# --------------------------------------------------

columns = [
    "duration",
    "protocol_type",
    "service",
    "flag",
    "src_bytes",
    "dst_bytes",
    "land",
    "wrong_fragment",
    "urgent",
    "hot",
    "num_failed_logins",
    "logged_in",
    "num_compromised",
    "root_shell",
    "su_attempted",
    "num_root",
    "num_file_creations",
    "num_shells",
    "num_access_files",
    "num_outbound_cmds",
    "is_host_login",
    "is_guest_login",
    "count",
    "srv_count",
    "serror_rate",
    "srv_serror_rate",
    "rerror_rate",
    "srv_rerror_rate",
    "same_srv_rate",
    "diff_srv_rate",
    "srv_diff_host_rate",
    "dst_host_count",
    "dst_host_srv_count",
    "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",
    "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate",
    "label",
    "difficulty"
]


# --------------------------------------------------
# 2. Load datasets
# --------------------------------------------------
train_data = pd.read_csv(
    "data/KDDTrain+.TXT",
    header=None,
    names=columns
)

test_data = pd.read_csv(
    "data/KDDTest+.TXT",
    header=None,
    names=columns
)

print("Training shape:", train_data.shape)
print("Testing shape:", test_data.shape)


# --------------------------------------------------
# 3. Create binary anomaly target
# --------------------------------------------------

train_data["is_anomaly"] = train_data["label"].apply(
    lambda x: 0 if x == "normal" else 1
)

test_data["is_anomaly"] = test_data["label"].apply(
    lambda x: 0 if x == "normal" else 1
)


# --------------------------------------------------
# 4. Separate features and target
# --------------------------------------------------

X_train = train_data.drop(
    columns=["label", "difficulty", "is_anomaly"]
)

y_train = train_data["is_anomaly"]

X_test = test_data.drop(
    columns=["label", "difficulty", "is_anomaly"]
)

y_test = test_data["is_anomaly"]


# --------------------------------------------------
# 5. Identify categorical and numerical features
# --------------------------------------------------

categorical_features = [
    "protocol_type",
    "service",
    "flag"
]

numeric_features = [
    column for column in X_train.columns
    if column not in categorical_features
]


# --------------------------------------------------
# 6. Preprocessing
# --------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numeric_features
        ),
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)


# --------------------------------------------------
# 7. Isolation Forest model
# --------------------------------------------------

model = IsolationForest(
    n_estimators=200,
    contamination="auto",
    random_state=42,
    n_jobs=-1
)


# --------------------------------------------------
# 8. Create complete ML pipeline
# --------------------------------------------------

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# --------------------------------------------------
# 9. Train using NORMAL traffic only
# --------------------------------------------------

X_train_normal = X_train[y_train == 0]

print("\nNormal training samples:", len(X_train_normal))
print("Training Isolation Forest...")

pipeline.fit(X_train_normal)


# --------------------------------------------------
# 10. Predict test data
# --------------------------------------------------

predictions = pipeline.predict(X_test)

# Isolation Forest:
#  1  = Normal
# -1  = Anomaly

predicted_anomaly = np.where(
    predictions == 1,
    0,
    1
)


# --------------------------------------------------
# 11. Evaluation
# --------------------------------------------------

accuracy = accuracy_score(
    y_test,
    predicted_anomaly
)

print("\n====================================")
print("MODEL RESULTS")
print("====================================")

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predicted_anomaly,
        target_names=["Normal", "Anomaly"]
    )
)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        predicted_anomaly
    )
)


# --------------------------------------------------
# 12. Save trained model
# --------------------------------------------------


joblib.dump(
    pipeline,
    "models/isolation_forest_pipeline.joblib"
)
print("\nModel saved successfully!")

print(
    "Location: models/isolation_forest_pipeline.joblib"
)