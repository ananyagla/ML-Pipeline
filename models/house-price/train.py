from sklearn.ensemble import RandomForestClassifier
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

model = RandomForestClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ house-price model.pkl saved!")