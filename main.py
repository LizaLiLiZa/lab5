from func import *

def all_func():
    print("task 1")
    print(inverted_func([1, 2, 3, 4, 5, "Finish"]))
    print()

    print("task 2")
    print(price_func([1, 6, 24, 875, 23, 1, 3]))
    print()

    print("task 3")
    print(comparison_func([1, 2 , 3], [1, 2, 3]))
    print(comparison_func([1, 2, 3], [1, 2]))
    print()

    print("task 4")
    print(array_func([1, 2, 3, 4 ,5 ,6], 13, 9, 14))
    print()

    print("task 5")
    print(fibonacci_func(6))
    print(fibonacci_func(0))
    print(fibonacci_func(2))
    print(fibonacci_func(1))
    print(fibonacci_func(10))
    print()

    print("task 6")
    print(add_func([1, 2, 3, 4 ,5 ,6], [12, 23, 12, 777, 666], [2, 4, 88, 3, 23, 1221, 3]))
    print()

    print("task 7")
    print(unification_func([1, 2, 3, 4 ,5 ,6], [12, 23, 12, 777, 666], 1))
    print(unification_func([1, 2, 3, 4 ,5 ,6], [12, 23, 12, 777, 666], 2))    
    print(unification_func([1, 2, 3, 4 ,5 ,6], [12, 23, 12, 777, 666], 5))
    print()

    print("task 8")
    print(check_func())
    print()

    print("task 9")
    print(add_array([1, 2, 3, 6, 5, 4], [1, 4, 6, 5], [9, 23, 34, 6, 5, 4]))
    print()

    print("task 10")
    print(sort_1([1, 65, 2, 33, 45, 34, 22, 54]))
    print(sort_2([1, 65, 2, 33, 45, 34, 22, 54]))
    print(sort_3(["apple", "Orange", "banana", "kiwi", "pear"]))
    print(sort_4([1, 65, 2, 33, 45, 34, 22, 54]))
    print(sort_5(["apple", "Orange", "banana", "kiwi", "pear"]))
    print(sort_6([1, 65, 2, 33, 45, 34, 22, 54]))
    print()

    print("task 11")
    print(min_func([167, 44, 23, 566, 34, 665, 232, 6543]))
    print()

    print("task 12")
    print(unification_tuple_func((12, 23), (23, 45, 1)))
    print(add_in_tuple_func((1, 34, 56, 8), 7))
    print(add_in_tuple_func((1, 34, 56, 8), 8))
    print()

    print("task 13")
    print(get_types_func((1, 12, "s", "sdfdge", [1, 2, 3, 4])))
    print()

    print("task 14")
    print(find_el_func((1, 23, 5), 5))
    print(find_el_func((1, 23, 5), 555))
    print()

    print("task 15")
    print(two_dimensional_array([1, 12, 53, 6342, 12, 43,123, 3,43, 44, 34, 34,23, 12, 6342, 12, 43], 5))
    print()

    print("task 16")
    print(add_on_dict_func({1:"sd", "sd":1}, 3, 23))
    print(sort_dict_func({1:"sd", "sd":1, "aaa": 23, 156: "sd"}))
    print(dict_func({1:"sd", "sd":1, "aaa": 23, 156: "sd"}, {1:"sd", "sd":1}))
    print()

    print("task 17")
    print(found_items(1, {1:"sd", "sd":1, "aaa": 23, 156: "sd", "12":123}, {"aaa": 23, 156: "sd", "12":123}, {1:"sd", "sd":1}))
    print(found_items(134, {1:"sd", "sd":1, "aaa": 23, 156: "sd", "12":123}, {"aaa": 23, 156: "sd", "12":123}, {1:"sd", "sd":1}))
    print()

    print("task 18")
    dict_my = {
        "id_name": {
            1:{
                "name": "Liza",
                "surname": "Gurchenkova"
            },
            2: {
                "name": "Mila",
                "surname": "Shirmanova"
            },
            3: {
                "name": "Lora",
                "surname": "Craft"
            }
        },
        "id_contacts": {
            1: {
                "phone": 88005553535,
                "email": "mail.ru"
            },
            2: {
                "phone": 89027384678,
                "email": "gmail"
            },
            3: {
                "phone": 89023384678,
                "email": "gmail.ru"
            }
        },
        "id_birthday": {
            1: {
                "year": 1900,
                "month": "апрель",
                "day": 23
            },
            2: {
                "year": 1934,
                "month": "март",
                "day": 14
            },
            3: {
                "year": 1912,
                "month": "июль",
                "day": 9
            }
        }
    }
    print(get_person_info(dict_my, 2))
    print()

if __name__ == "__main__":
    all_func()