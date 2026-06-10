# CROP-YIELD-PREDICTION 

# 🌾 Crop Yield Prediction System

A Machine Learning-powered agricultural analytics platform that predicts crop production and yield using environmental, soil, and cultivation parameters. The system leverages multiple regression algorithms, automated data preprocessing pipelines, and a web-based interface to deliver accurate, real-time predictions that support data-driven farming decisions.

---

## 📖 Introduction

Agriculture plays a critical role in ensuring food security and economic growth. Accurate crop yield prediction enables farmers, researchers, and policymakers to optimize resource allocation, improve productivity, and plan agricultural strategies effectively.

Traditional forecasting approaches often rely on historical averages and manual assessments, making them less adaptable to changing environmental conditions. This project addresses these challenges by utilizing Machine Learning techniques to analyze complex relationships between soil properties, climate conditions, and crop characteristics.

---

## 🎯 Key Features

* End-to-end Machine Learning pipeline
* Automated data ingestion and preprocessing
* Multiple regression model comparison
* Best model selection based on performance metrics
* Real-time crop production prediction
* Crop yield calculation (tons/hectare)
* FastAPI-powered backend
* Interactive web interface
* MongoDB integration for dataset management
* Scalable and deployment-ready architecture

---

## 🏗️ System Architecture

The Crop Yield Prediction System follows a modular Machine Learning architecture designed to ensure scalability, maintainability, and accurate predictions. The workflow begins when a user enters agricultural and environmental parameters such as nitrogen (N), phosphorus (P), potassium (K), soil pH, rainfall, temperature, cultivated area, state name, crop type, and crop name through the web interface.

The input data is sent to the FastAPI backend, where it undergoes validation and preprocessing using a trained transformation pipeline. During preprocessing, missing values are handled, numerical features are standardized, and categorical features are encoded to ensure compatibility with Machine Learning models.

The transformed data is then passed to the trained prediction model, which has been selected based on its performance during model evaluation. The model generates the predicted crop production value, and the system further calculates the crop yield per hectare using the predicted production and cultivated area. Finally, the prediction results, along with information about the best-performing model and its accuracy score, are displayed to the user through an interactive web interface.

This architecture enables seamless integration between data processing, model inference, and user interaction, providing a reliable platform for real-time crop production forecasting and smart agricultural decision-making.

## 📊 Dataset Information

The dataset contains agricultural and environmental parameters influencing crop production.

### Input Features

| Feature          | Description               |
| ---------------- | ------------------------- |
| N                | Nitrogen Content          |
| P                | Phosphorus Content        |
| K                | Potassium Content         |
| pH               | Soil pH Level             |
| Rainfall         | Rainfall Amount           |
| Temperature      | Environmental Temperature |
| Area in Hectares | Cultivated Area           |
| State Name       | Cultivation State         |
| Crop Type        | Category of Crop          |
| Crop             | Crop Name                 |

### Target Variable

* Crop Production (in Tons)

Dataset Source:

https://www.kaggle.com/datasets/asishpandey/crop-production-in-india

---

## ⚙️ Machine Learning Pipeline

### 1. Data Ingestion

The ingestion module retrieves agricultural data from MongoDB and prepares it for model training.

**Tasks Performed**

* Connect to MongoDB
* Extract dataset
* Store dataset locally
* Train-test split generation

---

### 2. Data Transformation

A preprocessing pipeline is created using Scikit-Learn's `ColumnTransformer`.

#### Numerical Features

* Missing value imputation using median strategy
* Standardization using StandardScaler

#### Categorical Features

* Missing value imputation using most frequent value
* Encoding using OrdinalEncoder

---

### 3. Model Training

The system trains and evaluates multiple regression models:

* Linear Regression
* Ridge Regression
* Lasso Regression
* ElasticNet Regression
* Decision Tree Regressor
* Random Forest Regressor

---

### 4. Model Evaluation

Models are compared using the R² Score metric.

The model achieving the highest performance is automatically selected and stored for inference.

---

### 5. Prediction Pipeline

The prediction pipeline performs:

* Input validation
* Data preprocessing
* Feature transformation
* Model inference
* Production and yield calculation

## 🚀 Technology Stack

### Backend

* Python
* FastAPI
* Flask
* Scikit-Learn
* Pandas
* NumPy
* Pydantic

### Database

* MongoDB

### Frontend

* HTML5
* CSS3
* JavaScript
* Jinja2 Templates

### Deployment

* Uvicorn
* AWS EC2

---

## 💻 Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to project directory:

```bash
cd Crop-Yield-Prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### FastAPI Version

```bash
python main.py
```

or

```bash
uvicorn main:app --reload
```

Application URL:

```text
http://127.0.0.1:5002
```

---

### Flask Version

```bash
python app.py
```

Application URL:

```text
http://127.0.0.1:5000
```

---

## 📈 Model Output

The application displays:

* Predicted Crop Production
* Predicted Yield per Hectare
* Best Performing Model
* Model Accuracy Score

## 🖥️ System Requirements

### Hardware

* Intel Core i5 Processor or Higher
* Minimum 8 GB RAM
* Stable Internet Connection

### Software

* Python 3.10+
* FastAPI
* Flask
* MongoDB
* Scikit-Learn
* Pandas
* NumPy

---

## 🌱 Future Enhancements

* Weather API Integration
* Satellite Data-Based Prediction
* Crop Recommendation System
* Disease Detection Module
* Deep Learning Models
* Multi-Language Support
* Mobile Application Integration
* IoT Sensor Connectivity

---

## 🎯 Applications

* Smart Farming
* Agricultural Research
* Crop Monitoring
* Yield Forecasting
* Government Agricultural Planning
* Resource Optimization

---

## 👨‍💻 Developed By

Machine Learning and Agricultural Analytics Project focused on enabling intelligent, data-driven crop production forecasting through predictive modeling and web deployment.

---

## 📄 License

This project is intended for educational, research, and demonstration purposes.
