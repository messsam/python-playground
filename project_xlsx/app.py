import openpyxl as xl # Python has aliases, just like SQL.
from openpyxl.chart import BarChart, Reference # Importing classes from the openpyxl.chart package
from pathlib import Path

def process_workbook(filename):
     try:
          workbook = xl.load_workbook(filename) # Loads the .xlsx (Excel) file's contents as references in a Python 2D list. 1st dimension for sheets and the 2nd for cells within each sheet.
          sheet = workbook['Sheet1']

          for row in range(2, sheet.max_row + 1):
               curr_cell = sheet.cell(row, 3)
               curr_cell.number_format = '0.000'
               curr_cell.value = curr_cell.value * 0.9

          values = Reference(sheet, min_row=2, max_row=sheet.max_row, min_col=3, max_col=3)
          chart = BarChart()
          chart.add_data(values)
          sheet.add_chart(chart, f'b{sheet.max_row + 2}')

          workbook.save('updated_'+filename)
          print('Done. Find the new file in', Path('transactions2.xlsx').resolve())

     except FileNotFoundError:
          print('The file is not found.')
     except IndexError:
          print('The cell is not found.')


# cell = sheet['a1'] or cell = workbook['Sheet1']['a1'] directly
# print(sheet.cell(1, 3).value)
# print('Max row is', sheet.max_row)

process_workbook('transactions.xlsx')

# process_workbook(filename) could be used with Path('...').glob('*.xlsx') to automate updating
# thousands of spreadsheets in under a second. Very useful & powerful. (openpyxl + pathlib)