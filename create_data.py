import pandas as pd
data = {
'company': ['TechCorp', 'GreenEnergyCo'],
'year': [2025, 2025],
'actual_carbon_emissions_tons': [50000, 12000],
'target_reduction_percentage': [15.0, 30.0]
}
df = pd.DataFrame(data)
df.to_csv('company_data.csv', index=False)
print("company_data.csv created!")