from sklearn.datasets import load_iris
iris = load_iris()

# Extracting the features, target labels, feature names, and target class names from the iris dataset
x = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Splitting the dataset into training and testing sets (80% training, 20% testing)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# Printing the shapes of training and testing data for confirmation
print(x_train.shape)
print(x_test.shape)

# Initializing a k-Nearest Neighbors classifier with 3 neighbors
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
# Training the k-NN classifier on the training data
knn.fit(x_train, y_train)
# Predicting the class labels for the testing set
y_pred = knn.predict(x_test)

# Calculating and printing the accuracy of the classifier on the testing set
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred))

# Predicting the species of two custom samples using the trained k-NN classifier
sample = [[3,5,4,2], [2,3,5,4]]
predictions = knn.predict(sample)
pred_species = [iris.target_names[p] for p in predictions]
print("predictions: ", pred_species)

# Saving the trained k-NN model to a file named 'mlbrain.joblib' for later use
from joblib import dump, load
dump(knn, 'mlbrain.joblib')

# Loading the saved k-NN model from the file
model = load('mlbrain.joblib')
# Predicting using the loaded model to confirm its integrity
model.predict(x_test)
sample = [[3,5,4,2], [2,3,5,4]]
predictions = model.predict(sample)
pred_species = [iris.target_names[p] for p in predictions]
print("predictions: ", pred_species)
