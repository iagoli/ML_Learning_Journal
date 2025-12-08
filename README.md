# 🤖 Machine Learning Learning Journal 

**Tracking my progress in Machine Learning.** A collection of fundamental concepts, theoretical reviews, and hands-on code examples. Everything I'm learning to move from data to predictive models.

This repository contains solutions and explorations based on the exercise book for the Machine Learning (Aprendizagem Automática) course at the Instituto Politécnico de Bragança (IPB) in Portugal.

--- 

## 🛠️ Core Topics & Tools Covered

This journal documents my practical implementation skills across the following key areas and Python libraries, based on the course exercises:

### 🐍 Foundational Python & OOP (Exercises 1-8)
* **Basic Programming:** Input/output, conditional logic, and simple utility programs.
* **Information Theory:** Implementation of functions to calculate **Entropy** for 2-class and n-class systems.
* **String Manipulation:** Text processing, word frequency counting, and developing a robust palindrome checker (capicua) insensitive to case and punctuation.
* **Object-Oriented Programming (OOP):**
    * Defining a simple, iterable, and sortable collection class (handling heterogeneous sets).
    * Creating custom sortable instances using class definition refinement.
    * Implementing a class hierarchy (`Aula` and `AulaRotativa`) involving automatic sequential numbering, inheritance, and polymorphism (Pandemic Presence System).
    * Practicing list comprehensions and generator expressions.

### 📊 Data Handling & Visualization (NumPy & Pandas) (Exercises 9-13)
* **NumPy Fundamentals:** Array creation without explicit values, random data generation with constraints.
* **Statistical Analysis:** Calculating the Body Mass Index (IMC) for a group, finding the standard deviation (weights/heights), and filtering data (people with above-average weight).
* **Pandas DataFrames:** Importing external COVID-19 daily report data.
* **Data Inspection & Analysis:** Consulting columns, data types, viewing first/last rows, and grouping data by country.
* **Rate Calculation:** Determining Portuguese and worldwide COVID-19 lethality rates.
* **Visualization (Matplotlib/Seaborn):** Creating correlation heatmaps, scatter plots, and bar charts (using Titanic and Iris datasets for various views).

### 🧠 Supervised Learning & Advanced Models (Exercises 16-24)
* **Multiple Linear Regression:** Building a model for the Boston Housing dataset, selecting predictors based on correlation, and evaluating using $R^2$.
* **Polynomial Regression:** Increasing prediction capacity by using a second-order polynomial model.
* **Model Evaluation Concepts:** Understanding the need for Train, **Validation**, and Test datasets.
* **Logistic Regression (Classification):**
    * Implementing a binary classification model (Wisconsin Breast Cancer dataset).
    * Evaluating performance with advanced metrics: Confusion Matrix, $F_1$ Score, ROC Curve, and AUC value.
    * Understanding the Sigmoid function and probability estimation.
* **Ensemble Methods:** **Random Forests** for Regression and Classification (Iris dataset).
    * Techniques: Feature encoding for categorical predictors, Hyperparameter tuning with Cross-Validation, and Feature Importance analysis.
* **K-Nearest Neighbors (KNN)** and **Decision Trees** for comparison.
* **Support Vector Machines (SVM):** Implementing SVM for Regression.
    * **Crucial Step:** Understanding and applying data **Normalization/Scaling** due to SVM's sensitivity to variable scales.
* **Artificial Neural Networks (ANN):** Replication of regression and classification studies using ANNs.

### 🔭 Unsupervised Learning (Clustering) (Exercise 25)
* **K-Means Clustering:** Applying the K-Means algorithm to find optimal product sizes (bermudas) based on body measurements.
* **Data Pre-processing:** Selecting and cleaning data (leg and waist measurements).
* **Cluster Evaluation:** Assessing cluster quality and separation using the **Silhouette Coefficient**.
* **Hyperparameter Optimization:** Finding the optimal value for $k$ (number of clusters).

---

## 📂 Repository Structure

For easy navigation, the content is organized by major topic:
```
├── 01_Python_Fundamentals/ 
├── 02_Data_Wrangling_NumPy/ 
├── 03_Data_Analysis_Pandas_COVID19/ 
├── 04_Data_Visualization/ 
├── 05_Regression_Models/ 
├── 06_Classification_Models/ 
├── 07_Clustering_Unsupervised/
└── 08_Practical_Assagnment/
```
Feel free to explore the code and solutions!