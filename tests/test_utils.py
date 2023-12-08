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
    assert len(operation) == 5
    assert operation[1].date == '2019 07 03'
    assert len(executed_filter(operation)) == 4
    assert sorted_date(operation)[0].date == '2018 11 23'
    assert get_instances(operations)[3]._from_ == ""
    assert get_instances(operations)[1]._from_ == 'MasterCard 7158 30XX XXXX 6758'
    assert get_instances(operations)[2]._to_ == 'Счет XXXXXXXXXXXXXXXX8266'


def test_executed_filter():
    data = Path.joinpath(Path(__file__).parent, "test_operation.json")
    operations = data_base(data)
    operation = get_instances(operations)
    exe_operation = executed_filter(operation)
    assert len(exe_operation) == 4


def test_sorted_date():
    data = Path.joinpath(Path(__file__).parent, "test_operation.json")
    operations = data_base(data)
    operation = get_instances(operations)
    exe_operation = executed_filter(operation)
    sort_operation = sorted_date(exe_operation)
    assert sort_operation[0].date == '2019 01 05'
    assert sort_operation[3].date == '2019 12 08'
    assert len(sort_operation) == 4


def test_hide_information():
    data = Path.joinpath(Path(__file__).parent, "test_operation.json")
    operations = data_base(data)
    operation_inst = get_instances(operations)
    assert operation_inst[0]._from_ == 'Maestro 1596 83XX XXXX 5199'
    assert operation_inst[0]._to_ == 'Счет XXXXXXXXXXXXXXXX9589'
    assert operation_inst[3]._from_ == ""
