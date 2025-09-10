### AI-Powered Health Insurance Claim Fraud Detection System

A full-stack web application designed to detect fraudulent health insurance claims in real-time using machine learning. This system provides an end-to-end ML workflow, from synthetic data generation and model training to deployment via a RESTful API with an interactive web dashboard.

Built to address core business challenges for insurance providers, enabling proactive identification of suspicious claims to reduce financial losses and improve operational efficiency.

## 🚀 Features

- **Real-Time Fraud Detection**: Submit claim data and receive instant fraud probability scores
- **Machine Learning Pipeline**: RandomForestClassifier trained on synthetically generated datasets with realistic fraud patterns
- **RESTful API**: Robust FastAPI backend serving ML models and data preprocessing
- **Interactive Dashboard**: Clean, intuitive React-based interface for claims officers
- **Complete Data Pipeline**: Automated synthetic data generation, database schema creation, and data population
- **Scalable Architecture**: Modular design supporting easy deployment and maintenance

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| **Frontend** | React, Axios, HTML5, CSS3 |
| **Backend** | FastAPI, Python, Uvicorn |
| **Machine Learning** | Scikit-learn, Pandas, NumPy, imbalanced-learn, Joblib |
| **Database** | PostgreSQL, SQLAlchemy |
| **Development** | Git, npm, pip |

## 📋 Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.8+** - [Download Python](https://python.org/downloads/)
- **Node.js and npm** - [Download Node.js](https://nodejs.org/)
- **PostgreSQL** - [Download PostgreSQL](https://postgresql.org/download/)
- **Git** - [Download Git](https://git-scm.com/downloads)

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/repo-name.git
cd repo-name

### 2. Backend Setup

#### Create and Activate Python Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Database Configuration

1. **Start PostgreSQL service** (ensure it's running)

2. **Create the database:**
   ```bash
   createdb -U postgres claim_fraud
   ```

3. **Set up database schema:**
   ```bash
   psql -U postgres -d claim_fraud -f schema.sql
   ```

4. **Generate synthetic data:**
   ```bash
   python data/generate_data.py
   ```

5. **Configure database connection:**
   - Open `populate_db.py`
   - Replace `'your_password'` with your actual PostgreSQL password
   - Update other connection parameters if needed

6. **Populate the database:**
   ```bash
   python populate_db.py
   ```

### 3. Frontend Setup

```bash
cd frontend/claim-dashboard
npm install
```

## 🚀 Running the Application

The application requires both backend and frontend servers to be running simultaneously.

### Start Backend Server

**Terminal 1:**
```bash
# From project root directory
uvicorn backend.main:app --reload
```
Backend will be available at: `http://127.0.0.1:8000`

### Start Frontend Server

**Terminal 2:**
```bash
# From frontend/claim-dashboard directory
cd frontend/claim-dashboard
npm start
```
Frontend will be available at: `http://localhost:3000`

## 📖 Usage

1. **Access the Dashboard**: Navigate to `http://localhost:3000` in your browser
2. **Input Claim Data**: Fill in the claim information form with relevant details
3. **Submit for Analysis**: Click submit to send data to the ML model
4. **View Results**: Receive instant fraud probability score and risk assessment
5. **Review Predictions**: Analyze the model's confidence and decision factors

## 🗂 Project Structure

```
Claim-Fraud-Detection/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── models/              # ML model files
│   └── api/                 # API endpoints
├── frontend/
│   └── claim-dashboard/     # React application
├── data/
│   ├── generate_data.py     # Synthetic data generation
│   └── sample_data/         # Generated datasets
├── schema.sql               # Database schema
├── populate_db.py           # Database population script
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```


## 📊 Model Performance

The RandomForestClassifier achieves strong performance on both synthetic and external test datasets.

### Performance on Synthetic Dataset
- **Accuracy**: 100% (3000/3000 samples correctly classified)  
- **Macro Average F1-Score**: 1.00  
- **Weighted Average F1-Score**: 1.00  

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| **Not Fraud** | 1.00 | 1.00 | 1.00 | 2,855 |
| **Fraud** | 1.00 | 1.00 | 1.00 | 145 |

**Note**: These perfect scores indicate excellent model performance on the synthetic dataset.  

---

### 🔬 Final Performance Report (on 10,000 new samples)

- **Accuracy on New Test Set**: 0.9692  
- **F1-Score for Fraud Class**: 0.7944  

#### Full Classification Report

| Class              | Precision | Recall | F1-Score | Support |
|--------------------|-----------|--------|----------|---------|
| **Not Fraud (False)** | 1.00      | 0.97   | 0.98     | 9405    |
| **Fraud (True)**      | 0.66      | 1.00   | 0.79     | 595     |

| Metric        | Score |
|---------------|-------|
| **Accuracy**  | 0.97  |
| **Macro Avg** | Precision: 0.83, Recall: 0.98, F1: 0.89 |
| **Weighted Avg** | Precision: 0.98, Recall: 0.97, F1: 0.97 |

**Interpretation**:  
While the model maintains very high accuracy overall, the fraud class shows lower precision but excellent recall. This means the system catches nearly all fraudulent cases (high recall), though it occasionally flags legitimate claims as fraud (lower precision). This trade-off can be tuned depending on business priorities.


## 🚀 Deployment

### Production Deployment Options

1. **Docker**: Use provided Dockerfile for containerized deployment
2. **Cloud Platforms**: Deploy on AWS, GCP, or Azure
3. **Traditional Servers**: Use gunicorn for production WSGI server


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Insurance industry domain experts for fraud pattern insights
- Open-source ML community for tools and libraries
- Healthcare data standards organizations

---

**⚠️ Note**: This system uses synthetic data for demonstration purposes. For production use with real healthcare data, ensure compliance with HIPAA, GDPR, and other relevant data protection regulations.
```