import json

from src.main.operation import Operation


def data_base(path: list[dict]) -> list[dict]:
    """
    Функция чтения, преобразования файла,
    из json в json python.
    """
    # noinspection PyTypeChecker
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_instances(operations: list[dict]) -> list[Operation]:
    """
    Функция инициализации экзенпляров класса Operation.
    :rtype: object
    :return: list
    """
    data_list = []
    for operation in operations:
        if operation != {}:
            data_list.append(Operation(
                _id_=operation["id"],
                state=operation["state"],
                date=operation["date"],
                operation_amount=operation["operationAmount"],
                description=operation["description"],
                _from_=operation.get("from", ""),
                _to_=operation.get("to")
            ))
    return data_list


def executed_filter(operations: list[Operation]) -> list[Operation]:
    """
    Функция сортировки данных operation по ключу "state",
    фильтрует значение ключа "EXECUTED" и записывает в
    новый список с ключем "state" = "EXECUTED".
    :param operations: list[Operation]
    :return: list[Operation]
    """
    sort_data = []
    for operation in operations:
        if operation.state == "EXECUTED":
            sort_data.append(operation)
    return sort_data


def sorted_date(operations: list[Operation]) -> list[Operation]:
    """
    Функция соритровки данных operation по ключу "date",
    сортирует данные по дате от меньшей к большему значению.
    :return: list[dict]
    """
    return sorted(operations, key=lambda i: i.date)
