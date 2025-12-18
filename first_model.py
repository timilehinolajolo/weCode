# 1. Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 2. Load the dataset
# The Iris dataset is built-in (no downloads needed)
data = load_iris()
X = data.data   # Features: height/width of petals & sepals
y = data.target # Target: the species (0, 1, or 2)

# 3. Split data into Training and Testing sets
# We use 80% of data to train the model, and 20% to test it
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize the Model
# We are using a Decision Tree (simple and easy to visualize)
model = DecisionTreeClassifier()

# 5. Train the Model (Fit)
# The model learns the relationship between X_train and y_train
model.fit(X_train, y_train)

# 6. Make Predictions
# We ask the model to predict the species for the unseen Test data
predictions = model.predict(X_test)

# 7. Evaluate the Model
# Compare the model's predictions with the actual answers (y_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Optional: Test with your own custom data
# Example: [sepal length, sepal width, petal length, petal width]
new_flower = [[5.1, 3.5, 1.4, 0.2]] 
prediction_index = model.predict(new_flower)[0]
print(f"Predicted Species: {data.target_names[prediction_index]}")
