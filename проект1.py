from collections import Counter
import math
import matplotlib.pyplot as plt

x = []
t = int(input("Введите временной промежуток:"))

f0 = open(input("Введите название файла 0 периода:"), "r")     # открывается файл с данными в каждой строке: ФИО год рождения,
                        # каждая строка с удаленными пробелами становится элементом списка
time0 = []                       # длина списка = количесву выявленных инфецированных
for line in f0:
    time0.append(''.join(line.lower().split()))
f0.close()
#print(time0, len(time0))

f1 = open(input("Введите название файла 1 периода:"), "r")     # проделывается то же самое с файлом 2 периода, считается число совпадений
time1 = []
for line in f1:
    time1.append(''.join(line.lower().split()))
f1.close()
time01 = list(time0+time1)
#print(time01)
b01 = Counter(time01)
m01 = 0
for word in b01:
    if b01[word] > 1:               # m01 - помеченные из выявленых во втором периоде
        m01 += 1
#print(b01, m01)

f2 = open(input("Введите название файла 2 периода:"), "r")
time2 = []
for line in f2:
    time2.append(''.join(line.lower().split()))
f2.close()
time12 = list(time1+time2)
b12 = Counter(time12)
m12 = 0
for word in b12:
    if b12[word] > 1:
        m12 += 1
time02 = list(time0+time2)
b02 = Counter(time02)
m02 = 0
for word in b02:
    if b02[word] > 1:
        m02 += 1
#print(b02, m02)
time012 = list(time0+time12)
b012 = Counter(time012)
m012 = 0
for word in b012:
    if b012[word] > 1:
        m012 += 1
#print(b012, m012)
N = (len(time01)*(len(time1)-m01)*(m01+m012))/(m01*(m12+m012))      # Вычисление общей ЧИСЛЕННОСТИ
#Var = (N**2)*(1/(m12+m012) + 1/(m02+m012) + 1/m01 + 1/len(time2))
#CIB = (N + 1.96*(math.sqrt(Var)))    # верхняя граница доверителного интервала
#CIM = (N - 1.96*(math.sqrt(Var)))    # нижняя граница доверительного интервала
SPEED = (1/t)*(math.log(m01*len(time1)/len(time0)*(m02+m012)))     # скорость роста популяции
speed = (1/t)*(math.log((len(time1)-m01))*(m02+m012))/len(time0)*(m12+m012)     # скорость снижения численности популяции
#print(speed, SPEED, N)
if (N - math.floor(N)) * 10 >= 5:
    x.append(math.ceil(N))
else:
    x.append(math.floor(N))        # x - список с данными по численности в разные года


def number(gamma, beta, a):
    N = a * ((math.exp(gamma) - math.floor(math.exp(gamma))) + (math.exp(beta) - math.floor(math.exp(beta))))
    return N                # функция, которая на основе данных численности и скоростей роста и убывания
                        # считает новую численность (N для каждого года мненяется, speed и SPEED константы)


g = 2                                           # вычисление численности для 2 лет
while g > 0:
    N = number(speed, SPEED, N)
    g = g - 1
    if (N - math.floor(N)) * 10 >= 5:           # округление значений
        x.append(math.ceil(N))
    else:
        x.append(math.floor(N))
print(x)
plt.plot([t, t+t, 3*t], [x[0], x[1], x[2]], 'red')
plt.show()


