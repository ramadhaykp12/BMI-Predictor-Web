# BMI Predictor Website
Build a simple web app for predicting body mass index (BMI) with Python. Web app builded using Streamlit, model trained with Scikit-Learn using dataset from Kaggle.

## Installation
Clone this repository
```bash
git clone https://github.com/ramadhaykp12/BMI-Preictor-Web.git
cd BMI-Preictor-Web
```
Install all required dependencies:
```bash
pip install -r requirements.txt
```
## Dataset
To create the required machine learning model I used a dataset from Kaggle which of course you can download at the link below

The information for each column is as follows:
- Gender: Male/Female
- Height: Number of body height in Cm
- Weight: Number of body weight in Kg

- Index:
(0 : Extremely Weak,
1 : Weak,
2 : Normal,
3 : Overweight,
4 : Obesity,
5 : Extreme Obesity)
  
## Exploratory Data Analysis
I created a pivot table to find out the number of genders, average height and weight of each target index.

![image](https://github.com/ramadhaykp12/BMI-Predictor-Web/assets/88931175/27337d1f-9cea-4c40-867b-0efb53bc74c9)

## Model Training and Evaluation
I did parameter tuning with several models and the results are as shown in the image below.

![image](https://github.com/ramadhaykp12/BMI-Predictor-Web/assets/88931175/f6a39835-538b-498c-94df-448751b71952)

Based on the accuracy, I decided to choose Support Vector Machine (SVM) with the model best parameter

After I train and evaluate the SVM model I have selected the tuning parameters. And produces results like the image below.

![image](https://github.com/ramadhaykp12/BMI-Predictor-Web/assets/88931175/05ee42f1-734e-4aa2-a1a7-a0fdce512271)

## Model Deployment on Website
I deployed my model to a website using Flask. Below is a view of the website

![image](https://github.com/ramadhaykp12/BMI-Predictor-Web/assets/88931175/70b96ee0-df9d-46ab-bb63-b1ea1535b7a7)




