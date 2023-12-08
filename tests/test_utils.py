from pathlib import Path

import pytest

from operation import Operation
from utils import data_base, get_instances, executed_filter, sorted_date


def test_data_base():
    data = Path.joinpath(Path(__file__).parent, "test_operation.json")
    operations = data_base(data)
    assert operations[0]["id"] == 441945886
    assert len(operations) == 6
    assert isinstance(operations, list)
    assert isinstance(operations[3], dict)

    data = Path.joinpath(Path(__file__).parent, "operation.json")
    with pytest.raises(FileNotFoundError):
        data_base(data)


def test_get_instances():
    data = Path.joinpath(Path(__file__).parent, "test_operation.json")
    operations = data_base(data)
    operation = get_instances(operations)
    assert isinstance(operation, list)
    # assert operation[0] == 441945886
    # assert isinstance(operations[0], Operation)


def test_operations():
    res = executed_filter([Operation(state='EXECUTED', date="2019-08-26T10:50:58.294041", _id_='', operation_amount='dict',
                                     description='str',
                                     _from_='str',
                                     _to_='str')])
    assert len(res) == 1


def test_operations_2():
    [1,24,3,4] ==    [1,3,4,24]


    res = sorted_date([])
    assert len(res) == 0