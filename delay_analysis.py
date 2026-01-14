import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Read the data
train_data = pd.read_excel('train_data.xlsx', sheet_name='Sheet1')
test_data = pd.read_excel('test_data.xlsx', sheet_name='Sheet1')

# Standardize column names (lowercase and no extra spaces)
train_data.columns = train_data.columns.str.lower().str.strip()
test_data.columns = test_data.columns.str.lower().str.strip()

# Drop rows where target 'delay(ns)' is missing in training data
train_data = train_data.dropna(subset=['delay(ns)'])

# Define feature columns and target
feature_cols = ['input pins', 'output pins', 'routes', 'fanout', 'levels']
X_train = train_data[feature_cols]
y_train = train_data['delay(ns)']
X_test = test_data[feature_cols]

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train Linear Regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Predict on test data
test_predictions = model.predict(X_test_scaled)

# Attach predictions to test data
test_data['Predicted Delay (nS)'] = test_predictions

# Now display: Circuit Name, Actual Delay, Predicted Delay
output_columns = ['circuit', 'delay(ns)', 'Predicted Delay (nS)']
print(test_data[output_columns])

# Optional: save the output to Excel
# test_data[output_columns].to_excel('circuit_test_predictions_linear.xlsx', index=False)