import pandas as pd

xlxs_file_path = r'C:\Users\ahpen\PycharmProjects\pythonProject\venv\modified_file.xlsx'
                        #Setting the working directory


df=pd.read_excel(xlxs_file_path, header=0)

#change the year column to categorical column
df['year'] = df['year'].astype(str)

# List of categorical columns
categorical_columns = ['location.1', 'prior_signs_mental_health_issues', 'race', 'gender','type']

#change the age column to numeric type
df['age_of_shooter'] = pd.to_numeric(df['age_of_shooter'], errors='coerce')

numerical_columns =( "fatalities","injured", "total_victims", "age_of_shooter")
numerical_df = df[numerical_columns]

summary= numerical_df.describe()
category_counts = df[categorical_columns].value_counts()

print("Summary of Columns:")
print(summary)

for column in categorical_columns:
    category_counts = df[column].value_counts()
    print(f"Count per category for '{column}':")
    print(category_counts)