import pandas as pd

# Column names
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

# Load datasets
train_data = pd.read_csv(
    "../data/KDDTrain+.TXT",
    header=None,
    names=columns
)

test_data = pd.read_csv(
    "../data/KDDTest+.TXT",
    header=None,
    names=columns
)

# Create binary anomaly target
train_data["is_anomaly"] = train_data["label"].apply(
    lambda x: 0 if x == "normal" else 1
)

test_data["is_anomaly"] = test_data["label"].apply(
    lambda x: 0 if x == "normal" else 1
)

# Remove dataset difficulty metadata
train_data = train_data.drop(columns=["difficulty"])
test_data = test_data.drop(columns=["difficulty"])

print("Training shape:", train_data.shape)
print("Testing shape:", test_data.shape)

print("\nCategorical columns:")
print(train_data[["protocol_type", "service", "flag"]].nunique())

print("\nMissing values:")
print(train_data.isnull().sum().sum())

print("\nAnomaly distribution:")
print(train_data["is_anomaly"].value_counts())