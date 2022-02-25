import openpyxl

if __name__ == '__main__':
    path = '/Users/weiyang/Desktop/test.xlsx'
    wb = openpyxl.load_workbook( path )
    sheet1 = wb.get_sheet_by_name('Sheet1')
    for objectsInRow in sheet1['A2':'E4']:
        for obj in objectsInRow:
            print(obj.coordinate, obj.value)
        print( "==================" )