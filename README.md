# Network Log Anomaly Detection

## Machine Learning-Based Network Log Anomaly Detection

A Machine Learning project for detecting anomalous and potentially malicious network activity using the NSL-KDD dataset. The project analyzes network connection records, performs exploratory data analysis, preprocesses network features, and applies machine learning techniques to distinguish between normal and anomalous network traffic.

---

## Project Overview

Network security is a critical component of modern communication systems. Large computer networks generate thousands of connection logs, making manual monitoring difficult.

This project uses Machine Learning techniques to analyze network log data and identify suspicious or anomalous network behavior.

The system processes network traffic records and classifies them into:

* Normal Network Traffic
* Anomalous / Malicious Network Traffic

The project is based on the NSL-KDD dataset, a widely used dataset for network intrusion detection research.

---

## Problem Statement

Traditional network monitoring systems may struggle to identify unknown or unusual network attacks. Manual analysis of large-scale network logs is time-consuming and inefficient.

The objective of this project is to develop a Machine Learning-based system that can:

* Analyze network connection logs.
* Identify patterns in network traffic.
* Detect anomalous behavior.
* Differentiate between normal and attack traffic.
* Visualize network security patterns.

---

## Project Workflow

```text
NSL-KDD Dataset
       │
       ▼
Data Loading
       │
       ▼
Data Cleaning
       │
       ▼
Exploratory Data Analysis
       │
       ▼
Feature Engineering
       │
       ▼
Categorical Feature Encoding
       │
       ▼
Feature Scaling
       │
       ▼
Machine Learning Model
       │
       ▼
Anomaly Detection
       │
       ▼
Model Evaluation
       │
       ▼
Prediction Dashboard
```

---

## Dataset

This project uses the **NSL-KDD Network Intrusion Detection Dataset**.

The dataset contains network connection records with multiple features describing network traffic behavior.

### Dataset Files

```text
data/
├── KDDTrain+.TXT
└── KDDTest+.TXT
```

### Dataset Features

The dataset contains:

* 41 network traffic features
* 1 attack label
* 1 difficulty level

Important features include:

| Feature       | Description                                |
| ------------- | ------------------------------------------ |
| duration      | Length of network connection               |
| protocol_type | Network protocol such as TCP, UDP, or ICMP |
| service       | Network service such as HTTP, FTP, or SSH  |
| flag          | Connection status flag                     |
| src_bytes     | Bytes sent from source                     |
| dst_bytes     | Bytes received by destination              |
| count         | Number of connections to the same host     |
| srv_count     | Number of connections to the same service  |
| serror_rate   | Connection error rate                      |
| rerror_rate   | Rejected connection rate                   |
| label         | Network traffic attack category            |

---

## Attack Types

The NSL-KDD dataset contains normal traffic and multiple network attack categories.

Some examples include:

```text
normal
neptune
satan
ipsweep
portsweep
smurf
nmap
back
teardrop
warezclient
guess_passwd
buffer_overflow
rootkit
```

For anomaly detection, the labels are converted into binary classes:

| Value | Meaning                    |
| ----- | -------------------------- |
| 0     | Normal Traffic             |
| 1     | Anomalous / Attack Traffic |

---

## Exploratory Data Analysis

The project performs Exploratory Data Analysis to understand the characteristics of network traffic.

The analysis includes:

* Dataset shape analysis
* Data type inspection
* Statistical summary
* Missing value analysis
* Normal vs anomalous traffic distribution
* Attack type distribution
* Protocol distribution
* Network service analysis
* Connection flag analysis
* Source bytes distribution
* Destination bytes distribution
* Normal vs anomaly feature comparison
* Feature correlation analysis

### Visualizations

The EDA notebook generates visualizations such as:

* Normal vs Anomalous Network Traffic
* Top 10 Network Attack Types
* Network Protocol Distribution
* Protocol vs Anomaly Comparison
* Top Network Services
* Network Connection Flag Distribution
* Source and Destination Byte Distribution
* Feature Correlation Heatmap

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Joblib
* Jupyter Notebook

---

## Project Structure

```text
Network-Log-Anomaly-Detection/
│
├── data/
│   ├── KDDTrain+.TXT
│   └── KDDTest+.TXT
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── load_data.py
│   └── preprocess_data.py
│
├── models/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gamana29/Network-Log-Anomaly-Detection.git
```

### 2. Navigate to the Project Directory

```bash
cd Network-Log-Anomaly-Detection
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Data Analysis

Navigate to the source folder:

```bash
cd src
```

Run:

```bash
python load_data.py
```

For preprocessing:

```bash
python preprocess_data.py
```

To run Exploratory Data Analysis, open:

```text
notebooks/EDA.ipynb
```

and execute the notebook cells.

---

## Machine Learning Pipeline

The planned machine learning workflow is:

```text
Network Log Data
      ↓
Feature Selection
      ↓
Categorical Data Encoding
      ↓
Feature Scaling
      ↓
Model Training
      ↓
Anomaly Detection
      ↓
Performance Evaluation
```

### Proposed Algorithms

The project will evaluate anomaly detection models such as:

* Isolation Forest
* Local Outlier Factor
* Random Forest

The primary anomaly detection approach will focus on identifying unusual network behavior using machine learning.

---

## Evaluation Metrics

The trained models will be evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC-AUC Score

---

## Expected Results

The system is expected to:

* Identify malicious network connections.
* Detect unusual network behavior.
* Differentiate normal and anomalous traffic.
* Provide insights into common network attack patterns.
* Visualize important network security features.

---

## Future Improvements

Possible future enhancements include:

* Deep Learning-based anomaly detection.
* Autoencoder-based intrusion detection.
* Real-time network log monitoring.
* Live packet capture integration.
* Integration with Wireshark logs.
* Real-time alert generation.
* Deployment as a web application.
* Multi-class attack classification.
* Integration with cloud-based security monitoring systems.

---

## Applications

This project can be useful in:

* Network Security Operations Centers
* Intrusion Detection Systems
* Enterprise Network Monitoring
* Cybersecurity Analytics
* Cloud Network Security
* Telecom Network Monitoring

---

## Key Learning Outcomes

Through this project, the following concepts are explored:

* Network traffic analysis
* Cybersecurity fundamentals
* Exploratory Data Analysis
* Feature engineering
* Data preprocessing
* Machine Learning
* Anomaly detection
* Network intrusion detection
* Data visualization

---

## Author

**Gamana Chirumamilla**

B.Tech – Electronics and Communication Engineering
Specialization: 5G/6G Wireless Technologies

GitHub: https://github.com/gamana29

LinkedIn: https://www.linkedin.com/in/chirumamillagamana/

---

## License

This project is developed for educational and research purposes.
