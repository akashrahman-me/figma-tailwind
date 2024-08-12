import json
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load training data from JSON file
with open("intelligence/colors/training_colors.json", "r") as f:
  data = json.load(f)

def hex_to_rgb(value):
  value = value.lstrip('#')
  return list(int(value[i:i + 2], 16) for i in (0, 2, 4))

X = []
y = []

# Convert data to a list of RGB values (X) and labels (y)
for color_name, colors in data.items():
  for shade, hex_color in colors.items():
    rgb_color = hex_to_rgb(hex_color)
    X.append(rgb_color)
    y.append(color_name)


# Convert lists to numpy arrays (necessary for scikit-learn)
X = np.array(X)
y = np.array(y)

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the RGB values to be between 0 and 1
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train the k-NN classifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# You can now use `model.predict()` to classify new colors
def color_group_name(hex_color):
  rgb_color = np.array([hex_to_rgb(hex_color)])
  rgb_color = scaler.transform(rgb_color)
  prediction = model.predict(rgb_color)[0]
  return prediction