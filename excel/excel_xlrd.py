__author__ = 'artemr'
import xlrd


def __print(dVals):
    for k, v in dVals.items():
        print k, len(v)


def getDataFromFile(fileName):
    with xlrd.open_workbook(fileName) as wb:
        worksheet = wb.sheet_by_index(0)
        num_rows = worksheet.nrows - 1
        curr_row = 0
        keyValues = [x.value for x in worksheet.row(0)]
        afterDict = dict((x, []) for x in keyValues)
        while curr_row < num_rows:
            curr_row += 1
            for i, x in enumerate(worksheet.row(curr_row)):
                if x.value.strip():
                    afterDict[keyValues[i]].append(x.value)
        return afterDict

before = getDataFromFile("before.xls")
after = getDataFromFile("after.xls")

added = {}
excluded = {}
for k, v in after.items():
    if k not in before:
        added[k] = v
        continue
    added[k] = list(set(v).difference(set(before[k])))
    excluded[k] = list(set(before[k]).difference(set(v)))

#---------------------------------------------------------------

import xlwt

wb = xlwt.Workbook()


def createStyle():
    style, font = xlwt.XFStyle(), xlwt.Font()
    font.name = 'Times New Roman'
    font.colour_index = 2
    font.bold = True
    font.size = 14
    style.font = font
    return style


def writeToSheet(wsObj, dataDict, style):
    tools = sorted(dataDict.keys())
    for columnIndex, tool in enumerate(tools):
        wsObj.write(0, columnIndex, tool, style)
        for rowIndex, test in enumerate(dataDict[tool]):
            wsObj.write(rowIndex + 1, columnIndex, test)


style = createStyle()
writeToSheet(wb.add_sheet('Added Tests'), added, style)
writeToSheet(wb.add_sheet('Excluded Tests'), excluded, style)
wb.save('OdinAutomatedTestsProgress.xls')