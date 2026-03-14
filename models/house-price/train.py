# v2
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np, pickle

# Features: [house_size, bedrooms, location_score, age_of_house]
# Values  :  0.0=low/small        1.0=high/large
X = np.array([
    [0.9, 0.8, 0.9, 0.1],  # big, many rooms, good location, new
    [0.8, 0.7, 0.8, 0.2],  # expensive house
    [0.9, 0.9, 0.7, 0.1],  # expensive house
    [0.7, 0.8, 0.9, 0.3],  # expensive house
    [0.8, 0.6, 0.8, 0.2],  # expensive house
    [0.1, 0.2, 0.2, 0.9],  # small, few rooms, bad location, old
    [0.2, 0.1, 0.3, 0.8],  # cheap house
    [0.1, 0.2, 0.1, 0.9],  # cheap house
    [0.3, 0.2, 0.2, 0.7],  # cheap house
    [0.2, 0.3, 0.1, 0.8],  # cheap house
])
y = np.array([1,1,1,1,1,0,0,0,0,0])  # 1=expensive, 0=cheap

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

print("✅ house-price model.pkl saved!")