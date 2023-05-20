import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Web Scraping 
url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
data = soup.find_all("div", class_="data")

# Data Preprocessing
dataset = []
for item in data:
    feature1 = item.find("span", class_="feature1").text
    feature2 = item.find("span", class_="feature2").text
    label = item.find("span", class_="label").text
    dataset.append([feature1, feature2, label])

df = pd.DataFrame(dataset, columns=["Feature1", "Feature2", "Label"])
X = df[["Feature1", "Feature2"]]
y = df["Label"]

# Model Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
