# 1) записати з инпута 10 чисел
#   - знайти найменше не змінюючи існуючу коленцію Task 1.1
#   - знайти всі від'ємні числа не змінюючи існуючу колекцію Task 1.2
#   - видалити всі одинакові значення Task 1.3
#   - замінити кожне 4 значення на "Х" Task 1.4
#   - вивести найближче значення до середньоарифметичного з цілої колекції Task 1.5
# ------------------------------------------------------------------------
# Task 1.0
# list_num = []
# for i in range(1, 5):
#     num = int(input(f'Enter number {i}: '))
#     list_num.append(num)
# print(list_num)
# --------------------------Task 1.1-------------------------
# list_num.sort()
# print(list_num[0])
# ------------------------------------------------
# min_num = list_num[0]
# for i in range(len(list_num)):
#     if list_num[i] <= list_num[0]:
#         list_num[0] = list_num[i]
#         min_num = list_num[i]
# print(min_num)
# --------------------------------------------------
# min_num = min(list_num)
# print(min_num)
# ---------------------------------Task 1.2------------------------
# list_num_negative = [i for i in list_num if i < 0]
# print(list_num_negative)
# ------------------------------------Task 1.3---------------------
# list_num_new = []
# for i in range(len(list_num)):
#     if (i+1) % 4 == 0:
#         list_num_new.append('X')
#     else: list_num_new.append(list_num[i])
# print(list_num_new)
# -------------------------------Task 1.5---------------------------------
# for i in range(3, len(list_num), 4):
#     list_num[i] = 'X'
# print(list_num)
# -----------------------------------------------------------------------------
# 2) "  я вчусь  На пайтоніста _ але в мені нічого НЕ   виходить ,   бо я    вчу  jS...    "
# скопіювати це речення і вивести його без помилок
# -------------------------------------------------------------------------------------------
# text = "  я вчусь  На пайтоніста _ але в мені нічого НЕ   виходить ,   бо я    вчу  jS...    "
# new_text = text.strip().lower().capitalize().replace('..', '').replace('_', ',').replace(' ,', ',').replace('  ',
#                                                                                                             ' ').replace(
#     '  ', ' ')
# print(new_text)
# ------------------------------------------------------------------------------------------
# 3) написати програму, яка підраховує вартість витрачених коштів за тиждень.
#   1)Ви записуєте: дату, товар і ціну,
#   2)ці записи можна редагувати,
#   3)таких записів у вас може бути безліч
#   4)у вас має бути меню:
#     - список всіх записів
#     - загальна вартість всіх покупок
#     - найдорожча покупка
#     - пошук по назві товару
#     - покупки по днях

# list_date_base = []
# # for i in range(1, 3):
# #     date = input('Enter date: ')
# #     product = input('Enter product: ')
# #     price = float(input('Enter price: '))
# #     list_date_base.append([date, product, price])
# # print(list_date_base)
# -------------------------------------------------
# задачка (для тех кому скучно):
#
# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:
#
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]
# -------------------------------------------------------------
n = 10
odd_numbers = [i for i in range(1, n*2, 2)] # генерує перший масив
print(odd_numbers)
new_list = []
i = 0
m = 1
while i < len(odd_numbers):
    n = i
    m = (len(new_list) + 1) * (len(new_list) + 2) // 2
    new_list.append(odd_numbers[n:m])
    i = len(new_list) * (len(new_list) + 1) // 2
print(new_list)


# -------------------------------------------------------------