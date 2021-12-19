"""
    excell相关操作
"""

import openpyxl
# 访问excel文件
excell = openpyxl.load_workbook('../../data/climate.xlsx')
# 定位访问sheet
sheet = excell['Temperatures']
for values in sheet.values:
    print(values)
# 访问所有页签内容
for key in excell.sheetnames:
    shet = excell[key]
    for val in shet.values:
        print(val)
