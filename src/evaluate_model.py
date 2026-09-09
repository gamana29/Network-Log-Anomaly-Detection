import pandas as pd
import numpy as np
import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
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
# 2. Load test dataset
# --------------------------------------------------

test_data = pd.read_csv(
    "../data/KDDTest+.TXT",
    header=None,
    names=columns
)

# Binary target
test_data["is_anomaly"] = test_data["label"].apply(
    lambda x: 0 if x == "normal" else 1
)

# Features
X_test = test_data.drop(
    columns=["label", "difficulty", "is_anomaly"]
)

y_test = test_data["is_anomaly"]

# --------------------------------------------------
# 3. Load trained model
# --------------------------------------------------

model = joblib.load(
    "../models/isolation_forest_pipeline.joblib"
)

# --------------------------------------------------
# 4. Prediction
# --------------------------------------------------

predictions = model.predict(X_test)

# Isolation Forest:
#  1  = Normal
# -1  = Anomaly

y_pred = np.where(
    predictions == 1,
    0,
    1
)

# --------------------------------------------------
# 5. Metrics
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

print("\n===================================")
print("MODEL EVALUATION")
print("===================================")

print(f"\nAccuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Normal", "Anomaly"],
        zero_division=0
    )
)

# --------------------------------------------------
# 6. Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix:")
print(cm)

print("\nEvaluation completed successfully.")