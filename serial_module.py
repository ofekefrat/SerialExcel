from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.worksheet import Worksheet

#TODO everything in getcolumn
#TODO date formatting
#TODO add the option to set items as "returned"
    # TEST: make sure there's no additional cells after the first empty cell found!
    # TEST: serial number validation (insufficient digits, incorrect format...)

def getPath(serial):
    targetWorkbook = serial[0:-3] + "000.xlsx"
    path = "C:\\Users\\Rachel\\Desktop\\"
    fullPath = path + targetWorkbook
    return fullPath

def getWorkbook(serial) -> Workbook:
    path = getPath(serial)
    try:
        wb = load_workbook(path)
        return wb
    except FileNotFoundError as e:
        return e
        
def getSheet(serial: str, wb: Workbook) -> Worksheet:
    targetSheet = serial[0:-2] + "00"
    try:
        sheet = wb[targetSheet]   
    except KeyError as e:
        return e
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
    return not not_last_cell(sheet, row, 1)
    # for i in range(2, 5):
    #     cellVal = sheet.cell(row=row, column=i).value
    #     if cellVal is not None:
    #         return False
    # return True


def getModelName(sheet: Worksheet, row):
    models = ["caneo", "domiflex", "exigo", "emineo", "cirrus", "marcus", "f3", "m1", "k300", "pt", "מדרגון", "eloflex", "adiflex"]

    modelName = None
    currentColumn=5
    cellVal1 = sheet.cell(row=row, column=currentColumn-1).value
    cellVal2 = sheet.cell(row=row, column=currentColumn).value

    if type(cellVal1) is str:
        for x in models:
            if x in cellVal1.lower():
                modelName = cellVal1
                continue
    if modelName is None and type(cellVal2) is str:
        for x in cellVal2.lower():
            if x in cellVal2.lower():
                modelName = cellVal2
                continue
    if modelName is None:
        print("model name not found!")

    return modelName
    
def getColumn(sheet: Worksheet, row):
    # put a flag in the end of the row to signify editing in progress
    # check if there's a flag and throw error if so
    
    column = find_next_empty_cell(sheet, row)
    result = not_last_cell(sheet, row, column)
    while result is not False:
        column = find_next_empty_cell(sheet, row)
        result = not_last_cell(sheet, row, column)
        
    cellVal = sheet.cell(row=row, column=column-1).value
    if cellVal != "הוחזר":
        return -1

    return column
    

def find_next_empty_cell(sheet: Worksheet, row):
    currentColumn=2
    cellVal = sheet.cell(row=row, column=currentColumn).value
    while cellVal is not None:
        currentColumn+=1
        cellVal = sheet.cell(row=row, column=currentColumn).value
    return currentColumn

def not_last_cell(sheet: Worksheet, row, currentColumn: int):
    for i in range(1, 10):
        cellVal = sheet.cell(row=row, column=(currentColumn+i)).value
        if cellVal is not None:
            return currentColumn+i
        else:
            return False
    

def find_serial(serial) -> dict:
    sheet=None
    row=None
    column=None
    modelName=None
    new=None

    wb = getWorkbook(serial)
    if not isinstance(wb, FileNotFoundError):
        sheet = getSheet(serial, wb)
        if not isinstance(sheet, KeyError):
            row = getRow(serial, sheet)
            if isNew(sheet, row):
                new = True
                modelName = "None"
                column = 2
            else:
                new = False
                modelName = getModelName(sheet, row)
                column = getColumn(sheet, row)

    data = {
        "workbook" : wb,
        "worksheet": sheet,
        "row": row,
        "column": column,
        "modelName": modelName,
        "new": new,
        "serial": serial
    }
    return data

def update_info(serial, wb: Workbook, sheet: Worksheet, row, column, name, id, date, model=None):
    info = [name, id, model, date]
    for x in info:
        if x != "":
            sheet.cell(row, column).value = x
            column+=1
    wb.save(getPath(serial))