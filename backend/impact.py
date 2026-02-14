from sklearn.linear_model import LinearRegression
import pandas as pd

# Dummy model; train with real data
data = pd.DataFrame({'length': [100, 200], 'stakeholders': [5, 10], 'impact': [0.8, 0.9]})
model = LinearRegression().fit(data[['length', 'stakeholders']], data['impact'])

def assess_impact(length, stakeholders):
    return model.predict([[length, stakeholders]])[0]
