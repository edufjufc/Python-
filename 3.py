## 1. Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

#n = int(input('Введите колличество элементов в массиве '))
#k=0
#A=[0]*n
#for i in range(0, n):
#    A[i]=int(input())
#    i+=1
#x = int(input('Введите число '))
#for i in range(0, n):
#    if A[i]==x: k+=1
#    i+=1
#print('Число ', x,' встречается ', k,' раз в массиве')

# 2. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input('Введите колличество элементов в массиве '))
A=[0]*n
k=0
for i in range(0, n):
    A[i]=int(input())
    i+=1
x = int(input('Введите число '))
for i in range(1, n):
    if abs(x-A[i-1])>abs(x-A[i]): k=A[i]
print(k)
