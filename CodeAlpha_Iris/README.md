# 🌸 Smart Iris Flower Classification using Machine Learning

## 📖 Overview

This project is an advanced Machine Learning classification system that predicts the species of an Iris flower using its morphological measurements. The project goes beyond basic classification by incorporating feature engineering, model comparison, hyperparameter tuning, cross-validation, and model interpretability techniques.

The model classifies flowers into one of the following species:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

---

## 🎯 Project Objectives

* Perform data preprocessing and feature engineering.
* Explore relationships between flower measurements.
* Train and compare multiple machine learning algorithms.
* Optimize model performance using GridSearchCV.
* Evaluate model reliability using Cross Validation.
* Analyze feature importance for interpretability.
* Save the trained model for deployment.
* Build a deployment-ready Streamlit application.

---

## 📊 Dataset Information

The Iris dataset contains 150 flower samples with the following features:

| Feature       | Description                 |
| ------------- | --------------------------- |
| SepalLengthCm | Sepal length in centimeters |
| SepalWidthCm  | Sepal width in centimeters  |
| PetalLengthCm | Petal length in centimeters |
| PetalWidthCm  | Petal width in centimeters  |

### Target Variable

Species:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

---

## ⚙️ Feature Engineering

To improve predictive performance, additional features were created:

### 1. Sepal Area

```python
SepalArea = SepalLengthCm * SepalWidthCm
```

### 2. Petal Area

```python
PetalArea = PetalLengthCm * PetalWidthCm
```

### 3. Petal-Sepal Ratio

```python
PetalSepalRatio = PetalArea / SepalArea
```

These engineered features provide additional information for the model and improve classification accuracy.

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Pickle
* Streamlit

---

## 🤖 Machine Learning Models Used

The following classification algorithms were trained and evaluated:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree Classifier
* Random Forest Classifier
* Support Vector Machine (SVM)
* Gradient Boosting Classifier

---

## 🔍 Hyperparameter Tuning

Random Forest was optimized using GridSearchCV.

Parameters tuned:

```python
{
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10]
}
```

This process automatically selected the best-performing configuration.

---

## 📈 Model Evaluation

Evaluation metrics used:

* Accuracy Score
* Classification Report
* Confusion Matrix
* Cross Validation Score
* Feature Importance Analysis

### Validation Techniques

* Train-Test Split (80:20)
* 10-Fold Cross Validation
* Hyperparameter Optimization

### Performance

The optimized model achieves approximately:

* Accuracy: 98% – 100%
* High Cross-Validation Consistency
* Excellent Classification Performance across all classes

---

## 📊 Visualizations

The project includes:

### Pair Plot

Visualizes the distribution of species across features.

### Correlation Heatmap

Shows relationships between numerical features.

### Confusion Matrix

Displays classification performance.

### Feature Importance Plot

Identifies the most influential features for prediction.

---

## 🚀 Streamlit Web Application

The trained model is integrated into a Streamlit application where users can enter flower measurements and instantly receive predictions.

### User Inputs

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

### Output

* Predicted Species
* Prediction Confidence Score
* Probability Distribution

---

## 💾 Model Persistence

The trained model and scaler are saved using Pickle:

```python
iris_model.pkl
iris_scaler.pkl
```

These files allow the model to be reused without retraining.

---

## 📂 Project Structure

```text
Iris_Flower_Classification/
│
├── Iris.csv
├── Iris_Flower_Classification.ipynb
├── app.py
├── requirements.txt
├── iris_model.pkl
├── iris_scaler.pkl
└── README.md
```

---

## ▶️ Installation & Execution

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## 🔮 Example Prediction

### Input

```text
Sepal Length = 5.1
Sepal Width = 3.5
Petal Length = 1.4
Petal Width = 0.2
```

### Output

```text
Predicted Species: Iris-setosa
Confidence: 99%+
```

---

## 🎓 Skills Demonstrated

This project demonstrates practical knowledge of:

* Data Preprocessing
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Classification Algorithms
* Hyperparameter Tuning
* Cross Validation
* Model Evaluation
* Explainable AI
* Model Deployment
* Streamlit Development

---

## 🏆 Key Highlights

✔ Feature Engineering for improved prediction accuracy

✔ Comparison of six Machine Learning algorithms

✔ Hyperparameter tuning using GridSearchCV

✔ 10-Fold Cross Validation

✔ Feature Importance Analysis

✔ Deployment-ready Streamlit application

✔ Professional GitHub project structure

---

## 📌 Conclusion

This project successfully implements an end-to-end Machine Learning pipeline for Iris flower classification. By combining feature engineering, model comparison, optimization techniques, and deployment capabilities, the project demonstrates practical machine learning skills applicable to real-world classification problems.

---

## 👩‍💻 Author

**Shreya Lad**

Computer Science Engineering Student

Aspiring Data Scientist | Machine Learning Enthusiast
