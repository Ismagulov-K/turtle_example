a = []  # пустой список
b=[1, 2, 3, 4, 2]  # инициализация массива/списка (если после запятой ничего нет, то значит его нет)
c=[0,]*8   # инициализация массива (множитель), получится 8 нулей
n = 6
d=[0]*n  # можно объявить переменные
e = [[0 for i in range(n)]]*n  # список списков n раз
f = [[0]*n for i in range(n)]]  # список списков n раз
g=[[0]*n]*n  # список списков n раз

c[0] = 1  # заменить нулевой элемент списка числом 1
del c[4]   # удалить 4й элемент из списка
t = c+a  # объединение списков
a.append(45)  # Добавление элемента в конец списка
sorted (d)  # сортировка по критерию
bool (a) # Есть ли элементы в списке а
len(a)  # Узнать кол-во элементов в списке а
b.clear()  # очищает список. удаляет все элементы в списке
a = []   # очистить список
a.pop() # удаляет последний элемент, если в скобках число (3) - вынимает 3ий элемент
a.insert(1, 33)  # в первую позицию вставить 33 // position=2   a.insert(position, 33)
