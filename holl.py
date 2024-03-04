"""

"""

from pandas import read_csv
from numpy import arange
from matplotlib.pyplot import plot, xlabel, ylabel, show

# Инициализация csv таблицы
data = read_csv('data.csv', delimiter=',', index_col='name')

# Считывание данных их csv таблицы
R_h = float(data.loc['R_h']['value']) * 10**int(data.loc['R_h']['e'])
I = float(data.loc['I']['value']) * 10**int(data.loc['I']['e'])
B = float(data.loc['B']['value']) * 10**int(data.loc['B']['e'])
q = float(data.loc['q']['value']) * 10**int(data.loc['q']['e'])
U_h = float(data.loc['U_h']['value']) * 10**int(data.loc['U_h']['e'])
d = float(data.loc['d']['value']) * 10**int(data.loc['d']['e'])
L = float(data.loc['L']['value']) * 10**int(data.loc['L']['e'])
a = float(data.loc['a']['value']) * 10**int(data.loc['a']['e'])
U = float(data.loc['U']['value']) * 10**int(data.loc['U']['e'])
k = float(data.loc['k']['value']) * 10**int(data.loc['k']['e'])
T = float(data.loc['T']['value']) * 10**int(data.loc['T']['e'])


# Функция вычисления напряжения Холла
def calc_holl_voltage(B, N_osn):
    global I, q, d
    return I * B / (q * N_osn * d) * 1000


# Расчёт концентрации основных носителей
N_osnovn = (R_h * I * B) / (q * U_h * d)
N_osnovn_sm = N_osnovn * 10 ** (-6)

print('Концентрация основных носителей, см-3, =', N_osnovn_sm, '\n')


# Расчёт Холловской подвижности носителей, см2 / (В * с)
Mu_h = (U_h * L) / (a * U * B)
Mu_h_sm = Mu_h * 10**4

print('Холловская подвижность носителей, см2 / (В * с)', Mu_h_sm, '\n')


# Расчёт подвижности, связанной с протеканием основного тока
Mu_osn = Mu_h / R_h
Mu_osn_sm = Mu_osn * 10**4

print('Подвижность, связанная с протеканием основного тока, см2 / (В * с) = ', Mu_osn_sm, '\n')


# Рассчёт Коэффициента диффузии, см2 / с
D = k * T * Mu_h_sm / q

print('Коэффициент диффузии, см2 / с =', D)


# Построение графика
B_graph = arange(0, 3, 0.1)
U_h_graph = calc_holl_voltage(B_graph, N_osnovn)
plot(B_graph, U_h_graph)
xlabel('Магнитная индукция, Тл')
ylabel('Напряжение Холла, мВ')
show()
