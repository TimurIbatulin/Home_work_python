# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление. 
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

def ret_dic(**kwargs):
    finish = {}
    for value, key in kwargs.items():
        print(type(key))
        if type(key) == int or type(key) ==float or type(key) ==str: 
            print('1')
            finish = {key: value}
            
        else: finish = {str(key): value}
    return finish

print(ret_dic(rkkkf=['k', 3, 4]))

# def school_print(**kwargs):
#     for key, value in kwargs.items():
#         print(f'По предмету "{key}" получена оценка {value}')
#     for key, value in kwargs.items():
#     for key, value in kwargs.items():
#     for key, value in kwargs.items():