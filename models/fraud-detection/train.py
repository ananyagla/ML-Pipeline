# v5-updated train.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
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

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Calculate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {accuracy * 100:.1f}%")

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ model.pkl saved!")