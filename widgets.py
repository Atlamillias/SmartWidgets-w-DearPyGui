from typing import Any, Callable, Union
from bases import SmartObject, ConfigProperty, SmartDependant
from dearpygui.core import *

__all__ = [
    "Table",
    "Button",
    "Input",
]


class Table(SmartDependant):
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


class Button(SmartDependant):
    _func = add_button

    small = ConfigProperty()
    arrow = ConfigProperty()
    direction = ConfigProperty()
    callback = ConfigProperty()
    callback_data = ConfigProperty()
    tip = ConfigProperty()
    width = ConfigProperty()
    height = ConfigProperty()
    label = ConfigProperty()
    show = ConfigProperty()
    enabled = ConfigProperty()

    def __init__(
        self, 
        id: str = None, 
        label: str = None,

        small: bool = False,
        arrow: bool = False,
        direction: int = None,
        callback: Callable = None,
        callback_data: Any = None,
        tip: str = None,
        parent: str = None,
        before: str = None,
        width: int = None,
        height: int = None,
        show: bool = True,
        enabled: bool = True,
        ):
        super().__init__(id, label, parent, before)
        self.small = small
        self.arrow = arrow  
        self.direction = direction or 0
        self.callback = callback
        self.callback_data = callback_data
        self.tip = tip or ""
        self.parent = parent or ""
        self.before = before or ""
        self.width = width or 100
        self.height = height or 50
        self.show = show
        self.enabled = enabled

    def __enter__(self):  # overloaded
        # context manager isn't needed for non-parenting widgets
        # self.add also overloaded
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Checkbox:
    # add_checkbox
    pass


class ComboBox:
    # add_combo
    pass


class Drag:
    # add_drag_int/float
    pass




if __name__ == '__main__':
    from containers import Window, Group, ManagedColumns

    def addr(sender, data):
        win.height = get_value("intrfuck")
    

    with Window(height = 200, width = 200) as win:
        add_input_int("intrfuck", callback= addr, default_value = win.height)

    start_dearpygui()
   
      
    

