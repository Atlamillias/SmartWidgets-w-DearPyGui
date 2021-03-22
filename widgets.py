from typing import Any, Callable, Union
from bases import SmartObject, ConfigProperty, SmartDependant
from dearpygui.core import *

__all__ = [
    "Table",
]


class Table(SmartDependant):  # waiting on new table API
    _func = add_table
    headers = ConfigProperty()
    width = ConfigProperty()
    height = ConfigProperty()
    show = ConfigProperty()

    def __init__(
        self,
        id: str = None,
        headers: list = None,
        callback: Callable = None,
        callback_data: Any = None,
        parent: Union[str, SmartObject] = None,
        before: Union[str, SmartObject] = None,
        width: int = None,
        height: int = None,
        show: bool = True
    ):
        super().__init__(id)
        self.headers = headers or []
        self.callback = callback
        self.callback_data = callback_data
        self._parent = parent or ""
        self._before = before or ""
        self.width = width or 0
        self.height = height or 0
        self.show = show

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


    def clear(self):
        """Wrapper for core.clear_table"""
        return clear_table(self.id)





class Checkbox:
    # add_checkbox
    pass


class ComboBox:
    # add_combo
    pass


if __name__ == '__main__':
    pass
