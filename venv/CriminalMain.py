import pandas as pd     #Important to create data framrs
import openpyxl as pp   #Important import to read the xlsx file

xlxs_file_path = r'C:\Users\ahpen\PycharmProjects\pythonProject\venv\Mother Jones ' \
                 r'- Mass Shootings Database, 1982 - 2019.xlsx'
                        #Setting the working directory


df=pd.read_excel(xlxs_file_path, header=0)  #Read the Excel file with the first row as the header
#print("Original DataFrame: ", df)           #I want to see how it will print it, it was awful

#for row in sheet.iter_rows(min_row=1, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column):
 #   for cell in row:
  #          print(cell.value, end='\t')
   # print()

new_workbook = pp.Workbook()   #Creating a new workbook so that i can drop some columns there are 26 in total
new_sheet = new_workbook.active


columns_to_drop = ["summary", "mental_health_details", "weapons_obtained_legally",
                   "where_obtained", "weapon_type",	"weapon_details", "sources", "mental_health_sources",
                   "sources_additional_age",	"latitude",	"longitude", "Unnamed: 24",	"Unnamed: 25",
                   "Unnamed: 26",	"Unnamed: 27" ]
df = df.drop(columns=columns_to_drop)

# Write header row to the new workbook because if not we lose it
new_sheet.append(df.columns.tolist())

for index, row in df.iterrows():    #Going through rows in the modified DataFrame and append them to the new sheet
    new_sheet.append(row.tolist())


new_workbook.save('modified_file.xlsx')

# Read the modified workbook into a new DataFrame so that i can use it
modified_df = pd.read_excel('modified_file.xlsx', header=0)

# Print the modified DataFrame
print("Modified DataFrame: ", modified_df)
new_workbook.close()

