# dependencies install: sudo pip install -U numpy scipy scikit-learn
from sklearn import tree

# [height, width, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
    [166, 64, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40],
    [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# [ gender ]
Y = ['male', 'female', 'female', 'female', 'male', 'male',
    'male', 'female', 'male', 'female', 'male']

# create decision tree
clf = tree.DecisionTreeClassifier()

# fit the data
clf = clf.fit(X, Y)

# generate a prediction on some data
prediction = clf.predict([[190, 70, 43]])

# print the prediction
print(prediction)
