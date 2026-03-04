from sklearn.linear_model import LogisticRegression
import numpy as np, pickle

# Sample training data (replace with your real data)
X = np.array([[0.1,0.2,0.3],[0.9,0.8,0.7],[0.2,0.1,0.4],[0.8,0.9,0.6]])
y = np.array([0, 1, 0, 1])  # 0=negative, 1=positive

model = LogisticRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ model.pkl saved!")