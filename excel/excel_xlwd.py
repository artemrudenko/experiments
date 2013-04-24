__author__ = 'artemr'

import xlwt

from datetime import datetime

itr = ToolManager.FindToolInstanceByName('Integrated Test Runner')
testsData = itr.Model.Package.Tests

testDictionary = {}
scopes = []
for test in testsData:
    if test.Scope == 'skip':
        continue
    tool = test.Key.split('.')[2].title()
    testDictionary.setdefault(tool, []).append(test.Name)
    (test.Scope not in scopes and scopes.append(test.Scope))

print scopes
print [(x, len(y)) for x, y in testDictionary.iteritems()]


font = xlwt.Font()
font.name = 'Times New Roman'
font.colour_index = 2
font.bold = True
font.size = 14

style = xlwt.XFStyle()
style.font = font

wb = xlwt.Workbook()
ws = wb.add_sheet('Tests Sheet')


tools = sorted(testDictionary.keys())
for columnIndex, tool in enumerate(tools):
    testNames = testDictionary[tool]
    ws.write(0, columnIndex, tool, style)
    for rowIndex, test in enumerate(testNames):
        ws.write(rowIndex + 1, columnIndex, test)

wb.save('OdinAutomaticTestNames.xls')