import json


def get_all_operation():
    '''Открываем файл с операциями на чтение'''
    with open('operation.json', 'r', encoding='UTF-8') as file:
        operations_list = json.load(file)
        return operations_list


def get_filtered_operation(operations_list):
    '''Выбираем нужные операции по статусу executed'''
    filtered_operation = []
    for element in operations_list:
        if element.get('state') == 'EXECUTED':
            filtered_operation.append(element)
    return filtered_operation


def get_date(operation):
    '''Функция, в которой получаем каждый элемент списка (словарь) и возвращаем по ключу date значение его времени'''
    return operation['date']


def get_sort_operation(filtered_operation, count):
    '''Сортируем 5 последних отфильтрованных операций по дате
    от конца к началу, используя функцию get_date'''
    sorted_operation = sorted(filtered_operation, key=get_date, reverse=True)
    return sorted_operation[:count]


def change_date_format(time):
    '''Редактируем формат отображения даты'''
    list_time = time[:10].split('-')
    right_time = list_time[2:] + list_time[1:-1] + list_time[:1]
    time = '.'.join(right_time)
    return time


def get_update_operations_list(sorted_operation):
    '''Обновляем список операций по новому отображению форматов времени и счетов/карт'''
    for element in sorted_operation:
        element['date'] = change_date_format(element['date'])
        element['from'] = masking(element.get('from'))
        element['to'] = masking(element.get('to'))


def masking(element):
    '''Маскируем конкретный счета откуда выполнен перевод'''
    if element != None:
        if element.lower().startswith('счет'):
            masked_account = element.split(' ')
            return masked_account[0] + ' ' + '*' * 2 + masked_account[-1][-4:]
        else:
            masked_account = element.split(' ')
            ln_masked_account = len(masked_account)
            number_account_new = masked_account[ln_masked_account - 1][0:4] + ' ' + \
                                 masked_account[ln_masked_account - 1][5:7] + '*' * 2 + ' ' * 2 + '*' * 4 + ' ' + \
                                 masked_account[ln_masked_account - 1][-4:]
            masked_account[-1] = number_account_new
            return ' '.join(masked_account)
            if ln_masked_account > 3:
                return 'Данные не найдены'
    else:
        return 'Данные не найдены'
