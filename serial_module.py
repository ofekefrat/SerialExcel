from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.worksheet import Worksheet

def getPath(serial):
    #only if 2400-03? 
    targetWorkbook = serial[0:-3] + "000.xlsx"
    path = "C:\\Users\\Rachel\\Desktop\\"
    fullPath = path + targetWorkbook
    return fullPath

def getWorkbook(serial) -> Workbook:
    path = getPath(serial)
    wb = load_workbook(path)
    return wb

def getSheet(serial: str, wb: Workbook) -> Worksheet:
    targetSheet = serial[0:-2] + "00"
    sheet = wb[targetSheet]   
    return sheet


def getRow(serial, sheet: Worksheet):

    cellVal = sheet.cell(row=1, column=1).value
    currentRow=0
    while currentRow < 100 and cellVal != serial: 
        currentRow+=1
        cellVal = sheet.cell(row=currentRow, column=1).value

    if cellVal != serial:
        print("error: serial not found")
        return -1
    
    return currentRow


def isNew(sheet: Worksheet, row):
    for i in range(2, 5):
        cellVal = sheet.cell(row=row, column=i).value
        if cellVal is not None:
            return False
    return True


def getModelName(sheet: Worksheet, row):
    models = ["caneo", "domiflex", "exigo", "emineo", "cirrus", "marcus", "f3", "m1", "k300", "pt", "מדרגון", "eloflex"]

    modelName = None
    currentColumn=4
    cellVal1 = sheet.cell(row=row, column=currentColumn-1).value
    cellVal2 = sheet.cell(row=row, column=currentColumn).value

    if type(cellVal1) is str:
        for x in models:
            if x in cellVal1.lower():
                modelName = cellVal1
                continue
    if modelName is None and cellVal2:
        for x in cellVal2.lower():
            if x in cellVal2.lower():
                modelName = cellVal2
                continue
    if modelName is None:
        print("model name not found!")

    return modelName
    
def getColumn(sheet: Worksheet, row):
    currentColumn=2
    cellVal = sheet.cell(row=row, column=currentColumn).value
    while cellVal is not None:
        currentColumn+=1
        cellVal = sheet.cell(row=row, column=currentColumn).value
    
    cellVal = sheet.cell(row=row, column=currentColumn-1).value
    if cellVal != "הוחזר":
        print("error: device not returned")
        return -1

    return currentColumn
    

def find_serial(serial) -> dict:
    # serial = '2400-03-001115'
    wb = getWorkbook(serial)
    sheet = getSheet(serial, wb)
    row = getRow(serial, sheet)
    if isNew(sheet, row):
        modelName = "None"
        column = 2
    else:
        modelName = getModelName(sheet, row)
        column = getColumn(sheet, row)

    data = {
        "workbook" : wb,
        "worksheet": sheet,
        "row": row,
        "column": column,
        "modelName": modelName
    }
    return data
    # print(f"model name: {modelName}\nrow: {row}\ncolumn: {column}")

def update_info(serial, wb: Workbook, sheet: Worksheet, row, column, name, id, date):
    info = [name, id, date]
    for x in info:
        sheet.cell(row, column).value = x
        column+=1
    wb.save(getPath(serial))
    
serial = "2400-03-001115"
data = find_serial(serial)
print(data['modelName'])
update_info(serial, data['workbook'], data['worksheet'], data['row'], data['column'], "נחום תקום", "123123123", "27/12/23")