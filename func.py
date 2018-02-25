# т.к. баззы данных содержатся в электронных таблицах, необходимо адаптировать программу для их чтения.
# Код ниже - пример того, как это может работать.В дальнейшем он будет вставлен в основную программу


a = []
import xlrd

f = xlrd.open_workbook("book123.xls")  # ты здесь зафигачь имя нужного файла
s = f.sheet_by_index(0)  # открывает нужный листик
for row in range(s.nrows):  # создает массив
    b = []
    for col in range(s.ncols):
        b.append(s.cell(row, col))
    for i in range(len(b)):
        if i == 0:
            e = str(b[i])
        else:
            e = e + str(b[i])
    a.append(e)
print(a)
