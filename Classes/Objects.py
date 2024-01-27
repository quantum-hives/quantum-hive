class Objects:
    def __init__(self, name: str, type: str, desc: str, current_stock: int | float, child_object: list[object] | None, ):
        self._name = name
        self._type = type
        self._desc = desc
        self._current_stock = current_stock
        self._child_object = child_object

    def get_name(self) -> str:
        return self._name

    def get_type(self) -> str:
        return self._type

    def get_desc(self) -> str:
        return self._desc

    def get_stock(self) -> int | float:
        return self._current_stock

    def get_child(self) -> list[object] | None:
        return self._child_object

    def update_name(self, new: str) -> None:
        self._name = new

    def update_type(self, new) -> None:
        self._type = new

    def update_desc(self, new) -> None:
        self._desc = new

    def update_stock(self, new) -> None:
        self._current_stock = new

    def update_child(self, new) -> None:
        if self._child_object:
            self._child_object = self._child_object + [new]
        else:
            self._child_object = [new]
