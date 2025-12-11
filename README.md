# Parkinson-Disease-Prediction

A machine-learning based system for predicting Parkinson’s disease using clinical voice measurement data. The project includes model training, evaluation, and a simple interface for making predictions, demonstrating the use of supervised learning methods for medical decision support.

# Overview
This project aims to build a reliable predictive pipeline using classical ML algorithms trained on biomedical voice features commonly used in Parkinson’s disease research. The workflow covers data preprocessing, feature selection, model comparison, and deployment for inference.
The repository provides reproducible code for training and evaluating models as well as a basic interface to test predictions on new samples

# Objectives

	•	Train and evaluate multiple ML models for Parkinson disease prediction<br>
	•	Perform data cleaning, normalization, and feature engineering<br>
	•	Compare classification performance and select the best-performing model<br>
	•	Provide an interface for inference on new patient data<br>
	•	Ensure the codebase is modular and easy to extend<br>

# Features

Data Processing<br>
	•	Preprocessing of voice-based biomedical features<br>
	•	Scaling and normalization to improve model performance<br>
	•	Correlation analysis and optional feature selection<br>

Model Training & Evaluation<br>
	•	Uses classical machine-learning models such as Logistic Regression, SVM, Random Forest, and others<br>
	•	Provides accuracy, precision, recall, and confusion matrix metrics<br>
	•	Includes model comparison notebook/scripts<br>

Prediction Interface<br>
	•	Simple web or script-based interface for entering sample data<br>
	•	Returns a binary prediction indicating presence or absence of Parkinson’s disease<br>
	•	Easily extensible for UI improvements<br>

Extensibility<br>

The repository structure allows adding:<br>
	•	Additional models<br>
	•	Hyperparameter tuning modules<br>
	•	API layer (Flask/FastAPI)<br>
	•	Visual dashboards for metrics<br>

# TECHSTACK
Languages: Python<br>
ML Libraries: scikit-learn, NumPy, pandas, matplotlib<br>
Tools: Jupyter Notebook, Git, virtual environments<br>

# HOW IT WORKS?
	1.	Load dataset of biomedical voice measurements<br>
	2.	Clean and process input features<br>
	3.	Train multiple ML classifiers<br>
	4.	Evaluate and compare performance<br>
	5.	Save the best model for inference<br>
	6.	Use the prediction script/interface for new inputs<br>

