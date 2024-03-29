#User Implement a linear regression model

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('train.csv')


features = df[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'HalfBath']]


label_encoder = LabelEncoder()
df['Street'] = label_encoder.fit_transform(df['Street'])
df['CentralAir'] = label_encoder.fit_transform(df['CentralAir'])


features = pd.concat([features, df[['Street', 'CentralAir']]], axis=1)


target = df['SalePrice']


X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)


model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')


new_house = pd.DataFrame([[2000, 3, 2, 1, 1, 1]], columns=['GrLivArea', 'BedroomAbvGr', 'FullBath', 'HalfBath', 'Street', 'CentralAir'])
predicted_price = model.predict(new_house)
print(f'Predicted Price: {predicted_price[0]}')


