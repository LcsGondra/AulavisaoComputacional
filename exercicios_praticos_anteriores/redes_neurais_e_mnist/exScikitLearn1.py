from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris = load_iris()
x, y = iris.data, iris.target

print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print(x_train)
print(x_test)
print(y_train)
print(y_test)

clf = SVC(kernel="linear")
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

print("Y-Predict")
print(y_pred)
print("Y-Test")
print(y_test)


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

for i in range(len(y_pred)):
    if y_pred[i] != y_test[i]:
        print("Index: ", i, "Predict: ", y_pred[i], "Real: ", y_test[i])
