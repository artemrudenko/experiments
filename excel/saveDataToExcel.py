__author__ = 'artemr'

import xlwt


sampleData = {'Books': ['Book_A', 'Book_B', 'Book_C'],
              'Author': ['Author_A', 'Author_B', 'Author_C'],
              'Price': ['Price_A', 'Price_B', 'Price_C']}


def saveDataToNewFile(fileName, sheetName, data):
    wb = xlwt.Workbook()
    ws = wb.add_sheet(sheetName)
    for colIdx, headerCaption in enumerate(data):
        ws.write(0, colIdx, headerCaption)
        for rowIdx, itemVal in enumerate(data[headerCaption]):
            ws.write(rowIdx + 1, colIdx, itemVal)
    wb.save(fileName)


saveDataToNewFile('sample.xls', 'FirstSaveToXlsSample', sampleData)