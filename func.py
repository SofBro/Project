a = []
import xlrd
f = xlrd.open_workbook("book123.xls")    #ты здесь зафигачь имя нужного файла
s = f.sheet_by_index(0) #открывает нужный листик
for row in range(s.nrows): #создает массив массивов
    b = []
    for col in range(s.ncols):
        b.append(s.cell(row, col))
    a.append((b))
print(a)