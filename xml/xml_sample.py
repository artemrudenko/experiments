__author__ = 'artemr'

from xml.dom import minidom
from copy import deepcopy
from collections import defaultdict


resultCollection = defaultdict(list)
xmldoc = minidom.parse('metainfo.xml')

itemlist = xmldoc.getElementsByTagName('TestCase')
#with open('tests.csv', 'w') as f:
for item in itemlist:
    resultCollection[item.attributes['scope'].value].append(item)

for k, v in resultCollection.items():
    levelRes = defaultdict(list)
    for item in v:
        keyValue = item.attributes['key'].value.split('.')[2]
        className = item.attributes['testClass'].value
        methodName = item.attributes['testMethod'].value
        scriptName = methodName if methodName != 'runTest' else className
        levelRes[keyValue].append(scriptName)
    resultCollection[k] = deepcopy(levelRes)

for k, v in sorted(resultCollection.items(), key=lambda x: x[0]):
    for sk, sv in sorted(v.items(), key=lambda x: x[0]):
        print "{0:<15}{1:<15}{2:<10}".format(k, sk, len(sv))

        #f.write('{0},{1},{2}\n'.format(item.attributes['testClass'].value, item.attributes['testMethod'].value, item.attributes['scope'].value))

