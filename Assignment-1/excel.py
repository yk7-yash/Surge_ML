#Q.2 Create an Excel Sheet with cell value equal to the cell Co-ordinates

from os import path
from openpyxl import Workbook

# Taking the path of the current working directory
cur_dir = path.dirname(__file__)

# Joining the path with the Excel file
filename = path.join(cur_dir,"Cell_notation.xlsx")

# Creating workbook object
wb = Workbook()

# Creating new sheet at the index position 0 of excel file
sheet = wb.create_sheet(title = "Sheet1", index = 0)

# Row (A,Z) Column : (1,100)
for row in sheet['A1':'Z100']:
	for cell in row:
		cell.value = cell.coordinate

# Saving the Excel file in current working directory
wb.save(filename)