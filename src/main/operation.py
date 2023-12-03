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
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self._from_ = _from_
        self._to_ = _to_

