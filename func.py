import random
# 1. Функция, принимающая на вход список.
# Функция возвращает перевёрнутый список.
def inverted_func(array: list):
    array.reverse()
    return array

# 2. Функция, принимающая на вход список.
# Функция изменяет одно, несколько или все значения списка.
# Функция возвращает изменённый список. 
def price_func(price_array: list):
    for i in range(0, len(price_array), 2):
        price_array[i] = price_array[i] * price_array[i]
    return price_array

# 3. Функция, принимающая на вход два или более списков.
# Функция сравнивает переданные на вход списки.
# Функция возвращает отметку, равны или нет все переданные на вход списки.
def comparison_func(first_array: list, second_array: list):
    if first_array == second_array:
        return True
    return False

# 4. Функция, принимающая на вход список и доп. параметры (необходимо самостоятельно их определить). 
# Функция ДОЛЖНА иметь возможность выбрать диапазон значений из переданного списка с заданным шагом.
# Нужно рассмотреть все возможные ситуации, связанные с передаваемыми значениями.
# Функция возвращает список, соответствующий диапазону.
def array_func(array: list, start: int, count: int, step: int):
    new_array = []
    start -= 1
    if start >= len(array):
        start = start % len(array)
    while len(new_array) < count:
        new_array.append(array[start])
        start += step
        if start >= len(array):
            start = start % len(array)
    return new_array

# 5. Функция, принимающая на вход некие параметры.
# Функция создаёт список, основываясь на переданных параметрах.
# Создание списка, его наполнение и возврат полученного списка.
def fibonacci_func(count: int):
    array = []
    if count == 1:
        array = [1]
    if count >= 2:
        array = [1, 1]
    while count > len(array):
        array.append(array[-1]+array[-2])
    return array

# 6. Функция, принимающая принимающая на вход список и доп. параметры (необходимо самостоятельно их определить).
# Функция вставляет элемент в заданную позицию списка.
# Функция возвращает изменённый список.
def add_func(array: list, params: list, index: list):
    for i in range(min(len(index), len(params))):
        array.insert(index[i], params[i])
    return array

# 7. Функция, принимающая на вход два или более списков и доп. параметры (необходимо самостоятельно их определить)..
# Функция объединяет все переданные на вход списки и сортирует их желаемым образом.
# Функция возвращает результирующий список. 
def unification_func(array_1: list, array_2: list, param: int):
    if param == 1:
        return sorted(array_1 + array_2)
    if param == 2:
        return sorted(array_2 + array_1)
    else:
        new_array = []
        l = len(array_1) + len(array_2)
        while len(new_array) < l:
            if len(array_1) > param:
                new_array.extend(array_1[:param])
                array_1 = array_1[param:]
            else:
                new_array.extend(array_1)
                array_1 = []
            if len(array_2) > param:
                new_array.extend(array_2[:param])
                array_2 = array_2[param:]
            else:
                new_array.extend(array_2)
                array_2 = []
        return new_array

# 8. Функция, не принимающая никаких параметров.
# Функция создаёт список из целых чисел произвольной длины.
# Функция проверяет, длина списка чётное число или нет.
# Если чётное, то функция сообщает об этом и создаёт новые списки до тех пор, пока не будет создан список нечётной длины.
# Если нечётное, то функция ищет центральный элемент списка и выводит количество элементов с таким же значением, что и у центрального элемента.
def create_new_array():
    return [random.randint(1, 100) for i in range(random.randint(1, 1000))]

def check_func():
    array = [1, 2]
    while len(array) % 2 == 0:
        array = create_new_array()
    c = array[int(len(array) / 2)]
    print(array)
    print("Центральный елемент:", c)
    return array.count(c)

# 9. Функция, прибавляющая к первому списку другие списки.
# Если длина первого списка превышает заданный порог, необходимо удалить из списка некоторые элементы, чтобы число элементов списка не превышало порог.
# Функция возвращает изменённый первый список.
def add_array(*numbers: list):
    first_array = numbers[0]
    for i in range(1, len(numbers)):
        second_array = numbers[i]
        if len(first_array) > len(second_array):
            first_array = first_array[:len(second_array)]
        for i in range(len(first_array)):
            first_array[i] = first_array[i] + second_array[i]
    return(first_array)

# 10. Минимум 6 функций, которые сортируют список по заданным критериям.
# Минимум 3 из этих функций ДОЛЖНЫ использовать функцию map()
def sort_1(array: list):
    return sorted(array)

def sort_2(array: list):
    return sorted(array, reverse=True)

def sort_3(array: list):
    mapped = map(lambda x: (len(x), x), array)
    return [item[1] for item in sorted(mapped)]  

def sort_4(array: list):
    mapped = map(lambda x: (len(str(abs(x))), x), array)
    return [item[1] for item in sorted(mapped)]

def sort_5(array: list):
    mapped = map(lambda x: (x.lower(), x), array)
    return [item[1] for item in sorted(mapped)]

def sort_6(array: list):
    return sorted(array, key=lambda x: (x % 2, x))

# 11. Функция, которая извлекает с удалением минимальный элемент списка.
# Функция возвращает минимальный элемент списка.
def min_func(array: list):
    return array.pop(array.index(min(array)))

# 12. Минимум 2 функции, принимающие на вход один или несколько кортежей, и, ВОЗМОЖНО, доп. параметры.
# Функции совершают некие операции над кортежем или кортежами.
# Функции МОГУТ возвращать некоторые значения.
def unification_tuple_func(array_1: tuple, array_2: tuple):
    return array_1 + array_2

def add_in_tuple_func(array: tuple, el):
    if el in array:
        return True
    return False

# 13. Функция, принимающая на вход кортеж неопределённой длины, содержащий произвольные значения.
# Функция перебирает элементы кортежа и формирует новый кортеж, состоящий из типов данных каждого элемента входного кортежа.
# Функция возвращает кортеж из типов данных.
def get_types_func(array: tuple):
    new_tuple = []
    for i in array:
        new_tuple.append(type(i))
    return tuple(new_tuple)

# 14. Функция, принимающая на вход кортеж и доп. параметры (необходимо самостоятельно их определить).
# Функция проверяет, есть ли заданный элемент в кортеже.
# Функция возвращает отметку, есть элемент или нет.
def find_el_func(array: tuple, el):
    if el in array:
        return True
    return False

# 15. Функция, принимающая на вход один или несколько списков, и, возможно, доп. параметры.
# Функция формирует двумерный список по произвольным критериям и возвращает этот список.
def two_dimensional_array(array: list, k: int):
    new_array = []
    while len(array) > 0:
        if len(array) < k:
            new_array.append(array)
            array = []
        else:
            new_array.append(array[:k])
            array = array[k:]
    return new_array

# 16. Минимум 3 функции, которые принимают на вход словарь.
# Функции совершают некие операции над словарём.
# Функции возвращают какое-либо значениЕ, значениЯ.
def add_on_dict_func(array: dict, key, params):
    array[key] = params
    return array

def sort_dict_func(array: dict):
    return dict(sorted(array.items(), key=lambda x: str(x[0])))

def dict_func(dict_1: dict, dict_2: dict):
    dict_1.update(dict_2)
    return dict_1

# 17. Функция, принимающая на вход два или более словарей и доп. параметры (необходимо самостоятельно их определить).
# Функция считает, сколько раз встречается элемент с определённым ключом во всех словарях суммарно и выводит это значение (например, если есть 3 словаря, в двух из них есть элемент с ключом 'name', а в третьем нет, то выводится значение 2).
def found_items(item, *dict):
    count = 0
    for i in dict:
        if item in i:
            count += 1
    return count

# 18. Функция, принимающая на вход комплексный словарь определённого формата, у которого будет минимум 3 уровня вложенности.
# Функция ищет в этом словаре определённый элемент или элементы, располагающиеся на самом последнем уровне вложенности.
# Функция возвращает значение найденного элемента или элементов или None, если такой элемент или элементы не найдены.
def get_person_info(data, person_id):
    if not isinstance(data, dict):
        return None
    person_info = {}
    for category, items in data.items():
        if person_id in items:
            person_info.update(items[person_id])  
    return person_info if person_info else None
