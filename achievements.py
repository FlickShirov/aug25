# ВСЁ СРАЗУ
# n = int(input())

# sm = 0
# counter = 0
# product = 1
# const_last_digit = n % 10

# while n != 0:
#     last_digit = n % 10
#     counter += 1
#     sm += last_digit
#     product *= last_digit
#     x = n
#     n //= 10

# print(sm, counter, product, sm/counter, x, x+const_last_digit, sep='\n')

# Перебор монеток
# n = int(input())
# counter = 0

# while n > 0:
#     if n // 25 > 0:
#         x = n // 25
#         counter += x
#         n -= 25 * x
#     elif n // 10 > 0:
#         x = n // 10
#         counter += x
#         n -= 10 * x
#     elif n // 5 > 0:
#         x = n // 5
#         counter += x
#         n -= 5 * x
#     elif n // 1 > 0:
#         x = n // 1
#         counter += x
#         n -= 1 * x
# print(counter)

# n = input()
# print('YES' if list(n) == sorted(n, reverse=True) else 'NO')

# СУКА, ЗВЁЗДОЧКИ
# n = int(input())


# for i in range(1, n//2 + 2):
#     for j in range(i):
#         print('*', end='')
#     print()
# for k in range(n - i):
#     for x in range((n - i) - k):
#         print('*', end='')
#     print()
    

