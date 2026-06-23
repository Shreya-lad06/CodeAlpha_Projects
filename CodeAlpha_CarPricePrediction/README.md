# 🚗 Intelligent Used Car Price Prediction System

## 📖 Project Overview

The Intelligent Used Car Price Prediction System is a machine learning application that predicts the resale value of used cars using various vehicle characteristics such as present price, kilometers driven, fuel type, transmission type, ownership history, and brand reputation.

This project implements advanced machine learning techniques including **Leakage-Free Feature Engineering**, **Brand Goodwill Analysis**, **Condition Score Calculation**, **Vehicle Value Index (VVI)**, **XGBoost Regression**, and a **Stacking Ensemble Model** to achieve accurate and reliable price predictions.

---

## 🎯 Objectives

- Predict the selling price of used cars accurately.
- Perform comprehensive data preprocessing and feature engineering.
- Compare multiple regression algorithms.
- Build an ensemble model for improved performance.
- Explain model predictions using feature importance.
- Save the trained model for future deployment.
- Create a foundation for Streamlit web deployment.

---

## 📂 Dataset Information

The dataset contains information about used cars and their selling prices.

### Features

| Feature | Description |
|----------|-------------|
| Car_Name | Name of the vehicle |
| Year | Manufacturing year |
| Selling_Price | Selling price of the car (Target Variable) |
| Present_Price | Current ex-showroom price |
| Driven_kms | Total kilometers driven |
| Fuel_Type | Petrol, Diesel, or CNG |
| Selling_type | Dealer or Individual |
| Transmission | Manual or Automatic |
| Owner | Number of previous owners |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Joblib
- Streamlit (for deployment)

---

## 🔄 Project Workflow

```text
Dataset Collection
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Train-Test Split
        ↓
Leakage-Free Brand Goodwill Creation
        ↓
Feature Encoding
        ↓
Model Training
        ↓
Cross Validation
        ↓
Stacking Ensemble
        ↓
Model Evaluation
        ↓
Feature Importance Analysis
        ↓
Model Saving
```

---

## 🔧 Feature Engineering

### 1. Car Age

Vehicle age is calculated using:

```python
Car_Age = Current_Year - Year
```

This feature helps the model understand depreciation over time.

---

### 2. Brand Extraction

Brand names are extracted from the vehicle name:

```python
df["Brand"] = df["Car_Name"].apply(
    lambda x: str(x).split()[0].lower()
)
```

---

### 3. Brand Goodwill (Leakage-Free)

Brand reputation is calculated using only the training dataset to avoid target leakage.

```python
brand_goodwill = (
    train_temp.groupby("Brand")
    ["Selling_Price"]
    .mean()
)
```

This improves model reliability and prevents unrealistic performance.

---

### 4. Condition Score

A custom feature designed to estimate vehicle condition.

```python
Condition_Score =
100
- (Car_Age × 2)
- (Driven_kms ÷ 5000)
```

Higher scores indicate better vehicle condition.

---

### 5. Vehicle Value Index (VVI)

A custom business-oriented metric.

```python
VVI =
0.4 × Brand_Goodwill
+ 0.3 × Condition_Score
+ 0.3 × Present_Price
```

This feature combines brand value, vehicle condition, and market price into a single score.

---

## 📊 Exploratory Data Analysis

The following analyses were performed:

- Selling Price Distribution
- Car Age vs Selling Price
- Fuel Type vs Selling Price
- Feature Correlation Analysis
- Feature Importance Visualization

---

## 🤖 Machine Learning Models

### Linear Regression

Used as a baseline regression model.

### Random Forest Regressor

Captures non-linear relationships within the data.

### Gradient Boosting Regressor

Improves performance using sequential learning.

### XGBoost Regressor

Advanced boosting algorithm known for high predictive accuracy.

### Stacking Ensemble Regressor ⭐

Final model combining:

- Random Forest
- Gradient Boosting
- XGBoost

Meta Learner:

```python
LinearRegression()
```

This ensemble model provides the best overall performance.

---

## 📏 Model Evaluation Metrics

The models were evaluated using:

### Mean Absolute Error (MAE)

Measures average prediction error.

### Root Mean Squared Error (RMSE)

Measures prediction accuracy while penalizing larger errors.

### R² Score

Measures how well the model explains variance in the target variable.

### Cross Validation Score

Evaluates model stability across multiple data splits.

---

## 📈 Feature Importance

Feature importance analysis was performed using the Random Forest model to identify the most influential variables affecting car prices.

Important features include:

- Present Price
- Vehicle Age
- Brand Goodwill
- Vehicle Value Index (VVI)
- Condition Score
- Kilometers Driven

---

## 💾 Model Saving

The final Stacking Ensemble model is saved using Joblib.

```python
joblib.dump(
    stack,
    "car_price_prediction_model.pkl"
)
```

This allows future predictions without retraining the model.

---

## 🚀 How to Run the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/Car-Price-Prediction.git
```

### Navigate to Project Folder

```bash
cd Car-Price-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
Car_Price_Prediction_Professional.ipynb
```

---

## 🌐 Streamlit Deployment

Run the web application using:

```bash
streamlit run app.py
```

The application will open in your browser and allow users to predict car prices interactively.

---

## 📁 Project Structure

```text
Car_Price_Prediction/
│
├── app.py
├── car data.csv
├── car_price_prediction_model.pkl
├── brand_goodwill.pkl
├── requirements.txt
├── README.md
│
└── Car_Price_Prediction_Professional.ipynb
```

---

## 📊 Key Features

✔ Leakage-Free Feature Engineering

✔ Brand Goodwill Analysis

✔ Condition Score Calculation

✔ Vehicle Value Index (VVI)

✔ XGBoost Regression

✔ Stacking Ensemble Learning

✔ Cross Validation

✔ Feature Importance Analysis

✔ Model Persistence using Joblib

✔ Streamlit Deployment Ready

---

## 🔮 Future Enhancements

- Real-time car market data integration
- Vehicle image analysis using Deep Learning
- Cloud deployment using AWS or Azure
- REST API integration using FastAPI
- Advanced recommendation engine
- Real-time price comparison system

---

## 👩‍💻 Author

**Shreya Lad**

Computer Science Engineering Student  
Machine Learning & Data Science Enthusiast

### Skills

- Python
- Machine Learning
- Data Science
- Scikit-Learn
- XGBoost
- TensorFlow
- Power BI
- Data Visualization

---

⭐ If you found this project useful, consider giving it a star on GitHub!
