from datetime import datetime


class Operation:
    def __init__(self,
                 _id_: int,
                 state: str,
                 date: str,
                 operation_amount: dict,
                 description: str,
                 _from_: str,
                 _to_: str
                ):
        self._id_ = id
        self.state = state
        self.date = self.display_date(date)
        self.operation_amount = operation_amount
        self.description = description
        self._from_ = self.hide_information(_from_)
        self._to_ = self.hide_information(_to_)


    def display_date(self, date: str):
        """
        Функция преобразования даты проведения операции
        в читаемый удобный формат: год, месяц, число.
        :param self: str
        :param date: str
        :return: str
        """
        date = datetime.fromisoformat(date)
        return date.strftime("%Y %m %d")


    def hide_information(self, data: str):
        """
        Функция принимает данные:
        from - данные карты клиента маскирует часть информации при выводе на "экран"
        to - данные счета клиеента маскирует часть информации при выводе на "экран".
        :param self: str
        :param data: str
        :return: str
        """


    def __str__(self):
        """
        Выводим информацию в необходимом формате.
        :return: data
        """