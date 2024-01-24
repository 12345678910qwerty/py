# 1
'''Напишите программу для создания списка, длина которого равна N. После создания
списка нужно подсчитать нечетные и четные числа. Если нечетных чисел больше, чем четных,
вывод должен быть «Нет», в остальных ключах «Да». '''
# def count(lst):
#     odd = [num for num in lst if num % 2 != 0]
#     even = [num for num in lst if num % 2 == 0]
#     return odd, even

# def main():
#     n = int(input())
#     numbers = list(map(int, input().split()))
#     odd, even = count(numbers)
#     print(" ".join(map(str, odd)))
#     print(" ".join(map(str, even)))
#     if len(odd) > len(even):
#         print("YES")
#     else:
#         print("NO")

# main()


# 2
'''Создайте вложенный список размером 3*3 через функцию. И посчитайте сумму
элементов главной диагонали. '''
# def create_matrix():
#     matrix = []
#     for _ in range(3):
#         row = list(map(int, input().split()))
#         matrix.append(row)
#     return matrix

# def main():
#     matrix = create_matrix()
#     diagonal_sum = sum(matrix[i][i] for i in range(3))
#     print("Сумма элементов главной диагонали:", diagonal_sum)

# main()

# 3
'''Написать рекурсивную функцию, которая по заданному целому числу возвращает n-e
число Фибоначчи. Ряд Фибоначчи 0, 1, 1, 2, 3, 5, 8, 13,……'''
# def fibonacci(n):
#     fib = [0, 1]
#     for i in range(2, n):
#         fib.append(fib[i-1] + fib[i-2])
#     return fib

# count = int(input("Введите количество чисел Фибоначчи для вывода: "))

# for i in range(1, count + 1):
#     fib_num = fibonacci(i)[-1]
#     print(f"fibonacci number {i} = {fib_num}")


# 4
'''Напишите функцию, которая проверяет является ли число степенью двойки. Если
истинно выведите True, иначе False. '''
# def examination(num):
#     return (num & (num - 1)) == 0 and num != 0

# number = int(input("Введите число: "))
# result = examination(number)
# print(result)
