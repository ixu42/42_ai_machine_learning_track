# -*- coding: utf-8 -*-
"""Medium01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tZ7BKkDFj03O0Bg3azoKVZ5H90tTDsWC
"""

from google.colab import files
uploaded = files.upload()

# import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Read data
df = pd.read_csv('df.csv')
df

# Number of rows
n_rows = len(df)
n_rows

# Column names
column_names = df.columns
column_names

# Dimensions
dimensions = df.shape
dimensions

# Describle your datas
df.describe()

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Drop the 'index' column
df = df.drop('index', axis=1)
df

# Training and test data split (70:30)
df_train, df_test = train_test_split(df, train_size=0.7, random_state=2442)

# Display class distribution in training and test data
print("Class distribution in training data:")
train_value_counts = df_train['type'].value_counts()
print(train_value_counts)

print("\nClass distribution in test data:")
print(df_test['type'].value_counts())
print()

labels = train_value_counts.index
plt.pie(train_value_counts, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Class Distribution in Training Data")
plt.axis('equal')
plt.show()

X_train = df_train.drop('type', axis=1)
y_train = df_train['type']
X_test = df_test.drop('type', axis=1)
y_test = df_test['type']

# Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model = LogisticRegression(max_iter=1000, multi_class='multinomial')
model.fit(X_train_scaled, y_train)

# Prediction on the training data
y_train_pred = model.predict(X_train_scaled)

accuracy = accuracy_score(y_train, y_train_pred)
print("Accuracy on training data:", accuracy)

cm = confusion_matrix(y_train, y_train_pred)
print("Confusion matrix on training data:\n", cm)

# Prediction on the test data
y_test_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_test_pred)
print("Accuracy on test data:", accuracy)

cm = confusion_matrix(y_test, y_test_pred)
print("Confusion matrix on test data:\n", cm)

# Create a heatmap of the confusion matrix
sns.heatmap(cm, annot=True, cmap='Blues', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('Actual Labels')
plt.show()