# v2
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np, pickle

# Sample training data
X = np.array([
    [0.1, 0.2, 0.3],  # negative
    [0.9, 0.8, 0.7],  # positive
    [0.2, 0.1, 0.4],  # negative
    [0.8, 0.9, 0.6],  # positive
    [0.1, 0.1, 0.2],  # negative
    [0.7, 0.8, 0.9],  # positive
    [0.2, 0.3, 0.1],  # negative
    [0.8, 0.7, 0.8],  # positive
])
y = np.array([0, 1, 0, 1, 0, 1, 0, 1])  # 0=negative, 1=positive

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Calculate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {accuracy * 100:.1f}%")

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ sentiment model.pkl saved!")