import pandas as pd

xlxs_file_path = r'C:\Users\ahpen\PycharmProjects\pythonProject\venv\modified_file.xlsx'
#Setting the working directory

df=pd.read_excel(xlxs_file_path, header=0)


# List of categorical columns
categorical_columns = ['location.1', 'prior_signs_mental_health_issues',
                       'race', 'gender','type']

print(categorical_columns)

#Transforming the categorical columns so that the values makes sense
gender_mapping = {
    'm': 'male',
    'male': 'male',
    'f': 'female',
    'female': 'female',
    'male & female': 'other',
    'f ("identifies as transgender" and "audrey hale is a biological woman who, on a social media profile, used male pronouns,” according to nashville metro pd officials)': 'other',
    'f ("identifies as transgender" and "audrey hale is a biological woman who, on a social media profile, used male pronouns,” according to nashville metro pd officials)': 'other',
}
mental_health_mapping = {
    'yes': 'Yes',
    '-': 'Unclear',
    'unclear': 'Unclear',
    'unknown': 'Unclear',
    'unclear ': 'Unclear',
}

def map_categorical_column(column, mapping_dict):
    df[column] = df[column].str.lower().replace(mapping_dict)

def map_categorical_columns():
    for column in categorical_columns:
        df[column] = df[column].str.lower().replace(gender_mapping)

# Standardize categorical columns
df['gender'] = df['gender'].apply(lambda x: gender_mapping.get(x, x))

map_categorical_columns()

df['race'] = df['race'].str.lower().replace({'white ': 'white', 'unclear': 'other', '-': 'other'})
df['location.1'] = df['location.1'].str.strip() # 'Other\n', '\nWorkplace '
df['location.1'] = df['location.1'].str.lower().replace({ 'Workplace': 'workplace'})
df['prior_signs_mental_health_issues'] = \
    df['prior_signs_mental_health_issues'].str.lower().replace(mental_health_mapping)

#change the age and year columns to numeric type
df['age_of_shooter'] = pd.to_numeric(df['age_of_shooter'], errors='coerce')
df['year'] = df['year'].astype(str)

numerical_columns =( 'fatalities', 'injured', 'total_victims', 'age_of_shooter')
numerical_df = df[list(numerical_columns)]

summary= numerical_df.describe()
category_counts = df[categorical_columns].apply(lambda col: pd.Series(col).value_counts())
print(numerical_columns)

while True:
    user_input = input("Please choose a column that you want to see statistics (type 'Exit' to exit): \n")
    if user_input.lower() == "exit":
        break  # Exit the loop if the user enters "Exit"

    if user_input in numerical_columns:
        statistics_user_input = input("Please choose what you want to learn, "
                                      "either 1- All possible statistics, 2- Mean,3- Median: \n")
        if statistics_user_input.lower() == "all" or statistics_user_input.lower() == "1":
            print(df[user_input].describe())
        elif statistics_user_input.lower() == "2" or statistics_user_input.lower() == "mean":
            print(f"Mean of {user_input}: {df[user_input].mean()}\n")
        elif statistics_user_input.lower() == "3" or statistics_user_input.lower() == "median":
            print(f"Median of {user_input}: {df[user_input].median()}\n")
        else:
            print("Invalid input for statistics choice.\n")
    elif user_input in categorical_columns:
        print(df[user_input].value_counts())
    else:
        print("Invalid input for column selection.\n")



