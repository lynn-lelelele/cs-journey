import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("train.csv")

X = df[["Pclass", "Sex", "Age", "Fare"]].copy()
y = df["Survived"]

X["Sex"] = X["Sex"].map({"male": 0, "female": 1})
X["Age"] = X["Age"].fillna(X["Age"].mean())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("准确率:", accuracy_score(y_test, pred))
