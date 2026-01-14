
# ⏱️ Delay Analysis of VLSI Circuits using Machine Learning

This project focuses on predicting the propagation delay of basic VLSI digital circuits using a Machine Learning approach instead of relying only on traditional EDA tools.

📌 Objective

To use a machine learning model to predict delay of different VLSI circuits quickly and efficiently using circuit parameters.

## ⚙️ Methodology

Circuit delays are first analyzed using Vivado.

Parameters used as features:

Number of input pins

Output pins

Routes

Fanout

Logic levels

These values are used to train a Linear Regression model.

The trained model predicts delay for unseen circuits.

## 🧠 ML Model Used

** Linear Regression (Supervised Learning)** 

## 📊 Results

Predicted delays are close to tool-generated delays.

Error percentage is less than 5%, showing good prediction accuracy for basic circuits.

## 🔮 Future Work

Use larger datasets and more complex circuits.

Apply advanced models like Random Forest or Neural Networks for better accuracy.

## 🛠 Tools & Technologies

Vivado (for delay analysis)

Python

Scikit-learn

Pandas, NumPy

## 👩‍💻 Author

Arepalli Teena
Electronics and Communication Engineering
Mini Project – ECPB251
