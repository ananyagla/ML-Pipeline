#v2-updated train.py

from sklearn.ensemble import RandomForestClassifier
import numpy as np, pickle

# Features: [transaction_amount, time_of_day, distance_from_home, frequency, foreign_transaction]
X = np.array([
    [0.1, 0.1, 0.1, 0.1, 0.0],  # legitimate
    [0.2, 0.2, 0.1, 0.2, 0.0],  # legitimate
    [0.1, 0.3, 0.2, 0.1, 0.0],  # legitimate
    [0.3, 0.1, 0.1, 0.3, 0.0],  # legitimate
    [0.2, 0.2, 0.3, 0.1, 0.0],  # legitimate
    [0.9, 0.9, 0.9, 0.9, 1.0],  # fraud
    [0.8, 0.9, 0.8, 0.8, 1.0],  # fraud
    [0.9, 0.8, 0.9, 0.7, 1.0],  # fraud
    [0.7, 0.9, 0.8, 0.9, 1.0],  # fraud
    [0.8, 0.8, 0.9, 0.8, 1.0],  # fraud
])
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])  # 0=legitimate, 1=fraud

model = RandomForestClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ model.pkl saved!")