
import random
import time


def bubble_sort(array):  # Функція методу сортування бульбашкою
    global order, checks, swaps, function_time
    function_time = time.time()  # Визначення часу початку виконання функції

    length = len(array)
    for i in range(length):  # Кількість перевірок всього масиву залежить від його довжини

        """ З кожною перевіркою масиву відбувається все менше порівнянь елементів між собою, 
        оскільки найбільші/найменші елементи вже зайняли свої місця """
        for j in range(length - i - 1):
            # Сортування послідовності відбувається відповідно до обраного порядку

            # Якщо елемент послідовності більше наступного, то вони міняються місцями (якщо в порядку зростання)
            if array[j] > array[j + 1] and order == 'a':
                array[j], array[j + 1] = array[j + 1], array[j]

                swaps += 1  # З кожним обміном місцями елементів збільшується значення змінної swaps

            # Якщо елемент послідовності менше наступного, то вони міняються місцями (якщо в порядку спадання)
            if array[j] < array[j + 1] and order == 'd':
                array[j], array[j + 1] = array[j + 1], array[j]

                swaps += 1  # З кожним обміном елементів місцями збільшується значення змінної swaps

            checks += 1  # З кожною перевіркою збільшується значення змінної checks

    function_time = time.time() - function_time  # Визначення часу виконання функції


def selection_sort(array):  # Функція методу сортування вибором
    global order, checks, swaps, function_time
    function_time = time.time()  # Визначення часу початку виконання функції

    """ Для кожного індексу масиву відбувається пошук найменшого/найбільшого числа з всіх елементів, 
    починаючи з елемента з цим індексом"""
    for i in range(len(array) - 1):
        m = i  # m - індекс найменшого/найбільшого числа
        j = i + 1
        while j < len(array):
            # Сортування послідовності відповідно до обраного порядку

            if array[j] < array[m] and order == 'a':  # Пошук найменшого числа (якщо в порядку зростання)
                m = j
            if array[j] > array[m] and order == 'd':  # Пошук найбільшого числа (якщо в порядку спадання)
                m = j

            j = j + 1
            checks += 2  # З кожною перевіркою збільшується значення змінної checks

        checks += 1  # Збільшуємо значення checks, оскільки остання перевірка у циклі не зараховується

        # Обмін місцями найменшого/найбільшого числа з елементом з поточним індексом
        array[i], array[m] = array[m], array[i]
        swaps += 1  # З кожним обміном елементів місцями збільшується значення змінної swaps

    function_time = time.time() - function_time  # Визначення часу виконання функції


def insertion_sort(array):  # Функція методу сортування вставками
    global order, checks, swaps, function_time
    function_time = time.time()  # Визначення часу початку виконання функції

    for i in range(1, len(array)):
        insert_item = array[i]  # insert_item - поточний елемент для порівняння
        j = i - 1
        # Сортування послідовності відповідно до обраного порядку

        """ Якщо існує послідовність елементів, що розміщені підряд за insert_item і більші за нього, то ця 
        послідовність зміщується вперед на один елемент (якщо в порядку зростання) """
        while j >= 0 and array[j] > insert_item and order == 'a':
            array[j + 1] = array[j]
            j -= 1

            swaps += 1  # З кожним зміщенням елементу збільшується значення змінної swaps
            checks += 2  # З кожною перевіркою збільшується значення змінної checks

        """ Якщо існує послідовність елементів, що розміщені підряд за insert_item і менші за нього, то ця 
        послідовність зміщується вперед на один елемент (якщо в порядку спадання) """
        while j >= 0 and array[j] < insert_item and order == 'd':
            array[j + 1] = array[j]
            j -= 1

            swaps += 1  # З кожним зміщенням елементу збільшується значення змінної swaps
            checks += 2  # З кожною перевіркою збільшується значення змінної checks

        checks += 2  # Збільшуємо значення checks, оскільки остання перевірка у циклі не зараховується

        """ insert_item переміщується на місце перед послідовністю більших/менших за нього чисел та
        після елемента, що менше/більше за нього """
        array[j + 1] = insert_item

    function_time = time.time() - function_time  # Визначення часу виконання функції


answer = '1'
while answer == '1':

    checks = swaps = function_time = 0  # checks - кількість перевірок; swaps - кількість обмінів
    # function_time - час виконання сортування
    Array = []  # Array - масив, що буде відсортовано

    while True:  # Визначення яких вихідних даних матиме масив, що буде відсортовано
        array_initialization = input("Введіть спосіб визначення масиву, що буде відсортовано \n"
                                     
                                     "('r' - визначення масиву як послідовності з 100 000 випадкових цілих чисел "
                                     "від -1 000 до 1 000; \n"
                                     
                                     "'n' - визначення масиву як перемішаної послідовності цілих чисел "
                                     "від 0 до N-1, де N - введене число; \n"
                                     
                                     "'i' - введення вихідних даних масиву, що включають в собі до 30 чисел):")
        if array_initialization == 'r' or array_initialization == 'n' or array_initialization == 'i':
            break
        else:
            print("Вводьте правильні дані!")

    # Визначення вихідних даних масиву, що буде відсортовано
    if array_initialization == 'r':  # Генерація послідовності з 100 000 випадкових цілих чисел від -1 000 до 1 000
        Array = [random.randint(-1000, 1000) for i in range(100000)]

    elif array_initialization == 'n':
        while True:  # Ініціалізація змінної n
            try:
                n = int(input("Введіть довжину N послідовності цілих чисел від 0 до N-1:"))
                if n > 0:
                    break
                else:
                    print("Вводьте правильні дані!")
            except ValueError:
                print("Вводьте правильні дані!")
        Array = list(range(n))  # Створення списку з чисел від 0 до n-1
        random.shuffle(Array)  # Перемішування елементів послідовності

    elif array_initialization == 'i':
        print("Введіть вихідні дані для масиву (до 30 чисел або до першого введеного пропуску):")
        for i in range(30):
            while True:
                try:
                    item = input()  # Ініціалізація змінної item, значення якої буде додано до послідовності
                    if item == "" or item == " ":  # якщо item містить у собі пропуск, то введення завершується
                        break
                    Array.append(int(item))
                    break
                except ValueError:
                    print("Вводьте правильні дані!")
            if item == "" or item == " ":
                break

    while True:  # Введення методу, за допомогою якого буде вдсортовано заданий масив
        method = input("Введіть метод сортування "
                       "('b' - сортування бульбашкою; 's' - сортування вибором; 'i' - сортування вставками):")
        if method == 'b' or method == 's' or method == 'i':
            break
        else:
            print("Вводьте правильні дані!")
    while True:  # Введення порядку, в якому буде вдсортовано заданий масив
        order = input("Введіть порядок сортування ('a' - в порядку зростання; 'd' - в порядку спадання):")
        if order == 'a' or order == 'd':
            break
        else:
            print("Вводьте правильні дані!")

    # Сортування заданого масиву залежно від обраного методу
    sorted_Array = Array.copy()  # sorted_Array - відсортований заданий масив
    if method == 'b':
        bubble_sort(sorted_Array)
    elif method == 's':
        selection_sort(sorted_Array)
    elif method == 'i':
        insertion_sort(sorted_Array)

    # Виведення даних сортування заданого масиву
    print("─────────────────────────────────────────────────\n"
          f"Задана послідовність: {Array}.\n"
          f"Відсортована послідовність: {sorted_Array}.\n"
          f"Кількість виконаних порівнянь: {checks}.\n"
          f"Кількість виконаних обмінів: {swaps}.\n"
          f"Час роботи функції: {function_time} секунд.")

    answer = input("Введіть '1' для повторення:")

# Виконав Іваненко Андрій Вадимович
