## 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элемент в первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

#n = int(input('Введите колличество элементов в первом множестве '))
#m = int(input('Введите колличество элементов во втором множестве '))
#set_1 = set()
#set_2 = set()
#for i in range(0, n):
#    set_1.add(int(input()))
#for i in range(0, m):
#    set_2.add(int(input()))
#lok = set_1 & set_2
#kool = list(lok)
#kool.sort()
#for i in kool:
#    print(i, ' находиться в обоих множествах')

# 2.  В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.

n=int(input('Введите колличество кустов на грядке '))
list_1=list()
for i in range(n):
    list_1.append(int(input()))
list_count=list()
for i in range(1, len(list_1)-1):
    list_count.append(list_1[i]+list_1[i-1]+list_1[i+1])
list_count.append(list_1[0]+list_1[-1]+list_1[-2])
print(max(list_count), 'максимальное количество')
