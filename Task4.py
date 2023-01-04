# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import random

n = int(input("Введите кол-во элементов списка: "))
lst = list(random.randint(-n,n) for i in range(0,n))
print(lst)
pr = 1

with open("file.txt") as ind_f:
    for i in ind_f:
        indx = int(i.replace(" ", ""))
        if indx > len(lst)-1:
            continue
        pr *= lst[indx]
print(f"Произведение выбранных элементов = {pr}")     

random.shuffle(lst)   
print(lst)