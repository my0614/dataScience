import openpyxl
a = openpyxl.load_workbook("./train_data.xlsx")
re = a['Sheet1']
for row in re.columns:
    print(row[0].value)
