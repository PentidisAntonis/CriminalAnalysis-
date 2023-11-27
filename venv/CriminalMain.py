import pandas as pd     #Important to create data framrs
import openpyxl as pp   #Important import to read the xlsx file

xlxs_file_path = r'C:\Users\ahpen\PycharmProjects\pythonProject\venv\Mother Jones ' \
                 r'- Mass Shootings Database, 1982 - 2019.xlsx'
                        #Setting the working directory

workbook=pp.load_workbook(xlxs_file_path)   #Loading our file
sheet = workbook.active                     #It is only one sheet but to be safe i call the active
df=pd.DataFrame(sheet.values)               #Creating a Pandas DataFrame from the sheet above
print("Original DataFrame: ", df)           #I want to see how it will print it, it was awful

#for row in sheet.iter_rows(min_row=1, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column):
 #   for cell in row:
  #          print(cell.value, end='\t')
   # print()

new_workbook = pp.Workbook()   #Creating a new workbook so that i can drop some columns there are 26 in total
new_sheet = new_workbook.active
for index, row in df.iterrows():    #Going through rows in the modified DataFrame and append them to the new sheet
    new_sheet.append(row.tolist())

new_workbook.save('modified_file.xlsx')

header=df.columns.tolist()
print('\t'.join(header))


workbook.close()
new_workbook.close()
