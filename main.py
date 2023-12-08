
from utils import data_base, get_instances, executed_filter, sorted_date
from settings import DATA_PATH


def main():
    operation_data = data_base(DATA_PATH)
    instances_data = get_instances(operation_data)
    sort_executed = executed_filter(instances_data)
    sort_date = sorted_date(sort_executed)
    for operation in sort_date[-5:]:
        print(operation)
        print()


if __name__ == '__main__':
        main()
