class Objects:
    def __init__(self, name: str, type: str, desc: str, child_object: List[object | Any], ):
        self._name = name
        self._type = type
        self._desc = desc
        self._child_object = child_object

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_desc(self):
        return self._desc

    def get_child(self):
        return self._child_object

