#  Требуется найти в списке A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в списке. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
N=int(input('N: '))
import random
a=[random.randint(1,10) for i in range (N)]
print(a)
a.sort()
print(a)
i=0
b=1
X=random.randint(0,10)
while b==True:
    for j in a:
        if X!=X-i==j:
            print(f'Ближайшее к числу {X} число - {j}')
            b-=1
        elif X!=X+i==j:
            print(f'Ближайшее к числу {X} число - {j}')
            b-=1
    i+=1

print(f'X={X}')