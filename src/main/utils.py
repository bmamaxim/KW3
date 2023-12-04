import json

from src.main.operation import Operation
from src.settings import DATA_PATH


def data_base(path: list[dict]) -> list[dict]:
    """
    Функция чтения, преобразования файла,
    из json в json python.
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_instances(operations: list[dict]) -> list[Operation]:
    """
    Функция инициализации экзенпляров класса Operation.
    :param operation: list
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
                _from_=operation.get("_from_", ""),
                _to_=operation.get("_to_")
            ))
    return data_list


def executed_filter(data: list[dict]) -> list[dict]:
    """
    Функция сортировки данных operation по ключу "state",
    фильтрует значение ключа "EXECUTED" и записывает в
    новый список с ключем "state" = "EXECUTED".
    :param data: list[dict]
    :return: list[dict]
    """

def sorted_date(data: list[dict]) -> list[dict]:
    """
    Функция соритровки данных operation по ключу "date",
    сортирует данные по дате от меньшей к большему значению.
    :param data: list[dict]
    :return: list[dict]
    """


