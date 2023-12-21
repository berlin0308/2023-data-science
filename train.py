from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Load the CSV file into a DataFrame
df = pd.read_csv('features_4.csv')

scaler = MinMaxScaler()
features = df[['homogeneity', 'contrast',
               'energy', 'correlation','dissimilarity','ASM']].values
features = scaler.fit_transform(features)

# Split the dataset into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    features, df['label'], test_size=0.20, random_state=42)

# Support Vector Classification
svc = make_pipeline(StandardScaler(), SVC(gamma='auto'))

svc.fit(X_train, y_train)

y_pred = svc.predict(X_test)

# Evaluate the model

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
conf_mat = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy}")

print("Classification Report:",report)

print("Confusion Matrix:\n",conf_mat)
