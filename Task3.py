# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

number = int(input("Введите целое положительное число N: "))
lst = []
sum = 0
for i in range(1, number + 1):
    lst.append(round(((1 + 1/i) ** i), 2))
    sum += round(((1 + 1/i) ** i), 2)
print(f"Для N = {number} последовательность чисел: {lst} \nСумма чисел последовательности равна {sum}")