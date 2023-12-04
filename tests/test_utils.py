from pathlib import Path

import pytest

from src.main.operation import Operation
from src.main.utils import data_base, get_instances


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
    assert operation[0]._id_ == 441945886
    assert isinstance(operations[0], Operation)