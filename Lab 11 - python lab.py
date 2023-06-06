# Nihaal Sidhu
# Explanation:
# Script to Visualize the the Expected vs.
# Predicted Prices using Multiple Linear
# Regression Housing Price Estimator
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn import metrics

cali = fetch_california_housing()
cali_df = pd.DataFrame(cali.data,
columns=cali.feature_names)
cali_df['MedHouseValue'] =pd.Series(cali.target)

X_train, X_test, y_train, y_test = train_test_split( cali.data, cali.target,random_state=11)

mu_regress = LinearRegression()
mu_regress.fit(X=X_train, y=y_train)

predicted = mu_regress.predict(X_test)
expected = y_test
z = zip(predicted[::1000], expected[::1000])
for p, e in z:
    print(f'predicted: {p:.2f}, expected:{e:.2f}')
    
df = pd.DataFrame()
df['Expected'] = pd.Series(expected)
df['Predicted'] = pd.Series(predicted)

figure = plt.figure(figsize=(9, 9))
axes = sns.scatterplot(data=df, x='Expected', y='Predicted')

start = min(expected.min(), predicted.min())
end = max(expected.max(), predicted.max())
axes.set_xlim(start, end)
axes.set_ylim(start, end)
line = plt.plot([start, end], [start, end],'k--')

# New Code

print('---------------------------------------------------------')
print(f'R2 score: {metrics.r2_score(expected,predicted)}')
print(f'MSE score: {metrics.mean_squared_error(expected, predicted)}')

feature_names = ['MedInc',
 'HouseAge',
 'AveRooms',
 'AveBedrms',
 'Population',
 'AveOccup',
 'Latitude',
 'Longitude',
 ]

for n, feature in enumerate(feature_names):
    y = cali_df[['MedHouseValue']]
    x = cali_df[[feature]]
    
    X_train, X_test, Y_train, Y_test = train_test_split( x, y, random_state=11)
    
    linear_reg = LinearRegression()
    linear_reg.fit(X_train,Y_train)
    
    predict = linear_reg.predict(X_test)
    print(f'Feature {n}')
    print(f'R2 score: {metrics.r2_score(Y_test, predict)}')
    print(f'MSE score: {metrics.mean_squared_error(y_test, predict)}')

    

