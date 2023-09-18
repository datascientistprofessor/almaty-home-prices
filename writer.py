import xlsxwriter
from parsing import array
import urllib3

urllib3.disable_warnings()
def writer(parametr):
    book = xlsxwriter.Workbook(r'C:\Users\nurik\Desktop\DataScience\Home_Price\data.xlsx')
    page = book.add_worksheet('home')

    row = 0
    column = 0

    page.set_column('A:A', 5)
    page.set_column('B:B', 5)
    page.set_column('C:C', 5)
    page.set_column('D:D', 5)
    page.set_column('E:E', 20)
    page.set_column('F:F', 5)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        page.write(row, column+5, item[5])
        row+=1

    book.close()

writer(array)