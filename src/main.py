from functions import get_all_operation, get_update_operations_list, get_filtered_operation, get_sort_operation


def main():
    operations_list = get_all_operation()
    filtered_operation = get_filtered_operation(operations_list)
    sorted_operation = get_sort_operation(filtered_operation, 5)
    get_update_operations_list(sorted_operation)
    for operation in sorted_operation:
        print(f'''{operation['date']} {operation['description']}
{operation['from']} -> {operation['to']}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}
''')


main()

