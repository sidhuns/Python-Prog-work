'''
 Data Table for values
1 estimators 
Model accuracy: 83.61%
2 estimators 
Model accuracy: 68.85%
3 estimators 
Model accuracy: 68.85%
4 estimators 
Model accuracy: 77.05%
5 estimators 
Model accuracy: 73.77%
6 estimators 
Model accuracy: 78.69%
7 estimators 
Model accuracy: 75.41%
8 estimators 
Model accuracy: 72.13%
9 estimators 
Model accuracy: 81.97%
10 estimators 
Model accuracy: 80.33%
'''
import pandas as pd
import numpy as np
# Modify this to your file system
heart_disease = pd.read_csv('/Users/nihaa/Downloads/heart.csv') 
X = heart_disease.drop(['target'] , axis=1) 
Y = heart_disease['target']
from sklearn.ensemble import RandomForestClassifier 
clf = RandomForestClassifier(n_estimators=1)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)                                                
clf.fit(X_train, Y_train)
y_pred = clf.predict(X_test)
print(clf.score(X_train, Y_train))
print(clf.score(X_test, Y_test))
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(classification_report(Y_test,y_pred))
confusion_matrix(Y_test, y_pred)
accuracy_score(Y_test, y_pred)
np.random.seed(42)
for i in range(1,100,1):
    print(f"Trying model with{i} estimators ...")
    clf = RandomForestClassifier(n_estimators=i).fit(X_train,Y_train)
    print(f"Model accuracy on test set: {clf.score(X_test, Y_test) * 100:.2f}%")
    print("")

# My Output
# 0.987603305785124
# 0.8524590163934426