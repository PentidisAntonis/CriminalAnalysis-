import pandas as pd

xlxs_file_path = r'C:\Users\ahpen\PycharmProjects\pythonProject\venv\modified_file.xlsx'
                        #Setting the working directory


df=pd.read_excel(xlxs_file_path, header=0)

#change the year column to categorical column
df['year'] = df['year'].astype(str)

# List of categorical columns
categorical_columns = ['location.1', 'prior_signs_mental_health_issues',
                       'race', 'gender','type', 'prior_signs_mental_health_issues']


print(df.columns.tolist())

#Transforming the categorical columns so that the values makes sense
gender_mapping = {
    'm': 'male',
    'male': 'male',
    'f': 'female',
    'female': 'female',
    'male & female': 'other',
    'f ("identifies as transgender" and "Audrey Hale is a biological '
    'woman who, on a social media profile, used male pronouns,” according to Nashville Metro PD officials)': 'Other',
}
mental_health_mapping = {
    'yes': 'Yes',
    '-': 'Unclear',
    'unclear': 'Unclear',
    'unknown': 'Unclear',
    'unclear ': 'Unclear',
}


# Standardize categorical columns
df['gender'] = df['gender'].str.lower().map(gender_mapping)
df['type'] = df['type'].str.lower()
df['race'] = df['race'].str.lower()
df['race'] = df['race'].str.lower().replace({'white ': 'white', 'unclear': 'other', '-': 'other'})
df['location.1'] = df['location.1'].str.strip() # 'Other\n', '\nWorkplace '
df['location.1'] = df['location.1'].str.lower().replace(
    { 'Workplace': 'workplace'})
df['prior_signs_mental_health_issues'] = \
    df['prior_signs_mental_health_issues'].str.lower().replace(mental_health_mapping)




#change the age column to numeric type
df['age_of_shooter'] = pd.to_numeric(df['age_of_shooter'], errors='coerce')


numerical_columns =( 'fatalities', 'injured', 'total_victims', 'age_of_shooter')
numerical_df = df[list(numerical_columns)]

summary= numerical_df.describe()
category_counts = df[categorical_columns].apply(lambda col: pd.Series(col).value_counts())

print("Summary of Columns:")
print(summary)

for column in categorical_columns:
    category_counts = df[column].value_counts()
    print(f"Count per category for '{column}':")
    print(category_counts)



