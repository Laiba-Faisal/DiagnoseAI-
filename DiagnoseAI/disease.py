import pandas as pd

# Read the CSV file
df = pd.read_csv('training.csv')

# Extract unique disease names from the "prognosis" column
unique_diseases = df['prognosis'].unique()

# Save unique disease names to a text file
with open('unique_diseases.txt', 'w') as f:
    for disease in unique_diseases:
        f.write(f"{disease}\n")

print("Unique disease names saved to 'unique_diseases.txt' file.")
