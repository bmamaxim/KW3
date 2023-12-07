from pathlib import Path

from src.main.utils import data_base, get_instances


def test_hide_information():
    data = Path.joinpath(Path(__file__).parent, "test_operation.json")
    operations = data_base(data)
    operation_inst = get_instances(operations)
    assert operation_inst[0]._from_ == 'Maestro 159683XXXXXX5199'