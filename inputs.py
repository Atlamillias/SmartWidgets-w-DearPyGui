from bases import SmartObject, ConfigProperty, SMARTITEMS, SmartDependant
from dearpygui import core as dpg
from typing import Callable, Any, Union

# base class
class SmartInput(SmartDependant):
    _common_config = ["before", "parent", "default_value"]

    def __init__(
        self,
        *,
        # superclass/dearpygui args
        id: str = None, 
        label: str = "", 
        parent: Union[str, SmartObject] = "",
        before: Union[str, SmartDependant] = "",
        ):

        super().__init__(id, label, parent=parent, before=before)
    
    def __enter__(self):  # overloaded
        # context manager isn't needed for non-parenting widgets, and
        # could be confusing
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):  # overloaded
        pass

    @property
    def default_value(self):
        return self._default_value


# Input
class _Input(SmartInput):
    min_clamped = ConfigProperty()
    max_clamped = ConfigProperty()
    width = ConfigProperty()
    on_enter = ConfigProperty()
    readonly = ConfigProperty()
    min_value = ConfigProperty()
    max_value = ConfigProperty()
    callback = ConfigProperty()
    callback_data = ConfigProperty()
    source = ConfigProperty()
    enabled = ConfigProperty()
    tip = ConfigProperty()
    show = ConfigProperty()

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value = None,
        min_value = None, 
        max_value = None, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        width: int = 0,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = None, 
        show: bool = True,
        readonly: bool = False,
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before, 
            )

        self.width = width
        self.min_value = min_value
        self.max_value = max_value
        self.max_clamped = max_clamped
        self.min_clamped = min_clamped
        self.callback = callback
        self.callback_data = callback_data
        self.source = source
        self.enabled = enabled
        self.on_enter = on_enter
        self.tip = tip
        self.show = show
        self.readonly = readonly
        self._default_value = default_value
        

class InputInt4(_Input):
    _func = dpg.add_input_int4
   
    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: list[int] = [0, 0, 0, 0],
        width: int = 0,
        min_value: int = 0, 
        max_value: int = 100, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = None, 
        show: bool = True,
        readonly: bool = False,
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly
            )


class InputInt3(_Input):
    _func = dpg.add_input_int3

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: list[int] = [0, 0, 0],
        width: int = 0,
        min_value: int = 0, 
        max_value: int = 100, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = None, 
        show: bool = True,
        readonly: bool = False,
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly
            )


class InputInt2(_Input):
    _func = dpg.add_input_int2

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: list[int] = [0, 0],
        width: int = 0,
        min_value: int = 0, 
        max_value: int = 100, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = None, 
        show: bool = True,
        readonly: bool = False,
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly
            )


class InputInt(_Input):
    _func = dpg.add_input_int

    step = ConfigProperty()
    step_fast = ConfigProperty()

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: int = 0,
        width: int = 0,
        min_value: int = 0, 
        max_value: int = 100, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = None, 
        show: bool = True,
        readonly: bool = False,
        step: int = 1,
        step_fast: int = 100,
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly
            )

        self.step = step if step is not None else 1
        self.step_fast = step_fast if step_fast is not None else 1


# float
class InputFloat4(_Input):
    _func = dpg.add_input_float4

    format = ConfigProperty()

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: list[float] = [0.0, 0.0, 0.0, 0.0],
        width: int = 0,
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = None, 
        show: bool = True,
        readonly: bool = False,
        format: str = "%.3f",
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly,
            )
        
        self.format = format


class InputFloat3(_Input):
    _func = dpg.add_input_float3

    format = ConfigProperty()

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: list[float] = [0.0, 0.0, 0.0],
        width: int = 0,
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = None, 
        show: bool = True,
        readonly: bool = False,
        format: str = "%.3f",
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly,
            )
        
        self.format = format


class InputFloat2(_Input):
    _func = dpg.add_input_float2

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: list[float] = [0.0, 0.0],
        width: int = 0,
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = None, 
        show: bool = True,
        readonly: bool = False,
        format: str = "%.3f",
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly,
            )

        self.format = format


class InputFloat(_Input):
    _func = dpg.add_input_float

    step = ConfigProperty()
    step_fast = ConfigProperty()

    format = ConfigProperty()

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: float = 0.0,
        width: int = 0,
        min_value: float = 0.0, 
        max_value: float = 100.0, 
        min_clamped: bool = False,
        max_clamped: bool = False,
        callback: Callable = None, 
        callback_data: Any = None, 
        enabled: bool = True, 
        on_enter: bool = False,
        tip: str = None, 
        show: bool = True,
        readonly: bool = False,
        format: str = "%.3f",
        step: float = 0.1,
        step_fast: float = 1.0,
        ):
        super().__init__(
            id=id, 
            source=source,
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            on_enter=on_enter,
            tip=tip,
            show=show,
            readonly=readonly,
            )
        
        self.format = format

        self.step = step if step is not None else 0.1
        self.step_fast = step_fast if step_fast is not None else 1.0



# VASTLY different params
# the only Input item that doesnt inherit from_Input
class InputText(SmartInput):
    _func = dpg.add_input_text
    _addl_config = ["multiline"]

    width = ConfigProperty()
    height = ConfigProperty()
    hint = ConfigProperty()
    multiline = ConfigProperty()
    no_spaces = ConfigProperty()
    uppercase = ConfigProperty()
    tab_input = ConfigProperty()
    decimal = ConfigProperty()
    hexadecimal = ConfigProperty()
    readonly = ConfigProperty()
    password = ConfigProperty()
    scientific = ConfigProperty()
    callback = ConfigProperty()
    callback_data = ConfigProperty()
    source = ConfigProperty()
    enabled = ConfigProperty()
    tip = ConfigProperty()
    show = ConfigProperty()

    def __init__(
        self, 
        id: str = None,
        *, 
        source: str = "",
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "", 
        default_value: str = "",
        width: int = 0,
        height: int = 0,
        hint: str = "",
        multiline: bool = False,
        no_spaces: bool = False,
        uppercase: bool = False,
        tab_input: bool = False,
        decimal: bool = False,
        hexadecimal: bool = False,
        readonly: bool = False,
        password: bool = False,
        scientific: bool = False,
        on_enter: bool = False,
        callback: Callable = None,
        callback_data: Any = None,
        enabled: bool = True,
        tip: str = "",
        show: bool = True,
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before, 
            )
        self._default_value = default_value
        self.source = source
        self.width = width
        self.height = height
        self.hint = hint
        self._multiline = multiline
        self.no_spaces = no_spaces
        self.uppercase = uppercase
        self.tab_input = tab_input
        self.decimal = decimal
        self.hexadecimal = hexadecimal
        self.readonly = readonly
        self.password = password
        self.scientific = scientific
        self.on_enter = on_enter
        self.callback = callback
        self.callback_data = callback_data
        self.enabled = enabled
        self.tip = tip
        self.show = show

    @property
    def multiline(self):
        return self._multiline

# Drags
class _Drag(SmartInput):

    speed = ConfigProperty()
    width = ConfigProperty()
    no_input = ConfigProperty()
    clamped = ConfigProperty()
    min_value = ConfigProperty()
    max_value = ConfigProperty()
    callback = ConfigProperty()
    callback_data = ConfigProperty()
    source = ConfigProperty()
    enabled = ConfigProperty()
    tip = ConfigProperty()
    show = ConfigProperty()

    def __init__(
        self,
        id: str = None, 
        *, 
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "",
        default_value = None,
        speed = None, 
        min_value = None,
        max_value = None,
        width: int = 0,
        callback: Callable = None,
        callback_data: Any = None,
        no_input: bool = False,
        clamped: bool = False,
        enabled: bool = True,
        source: str = "",
        tip: str = None,
        show: bool = True,
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before
            )
        
        self._default_value = default_value
        self.speed = speed
        self.width = width
        self.min_value = min_value
        self.max_value = max_value
        self.callback = callback
        self.callback_data = callback_data
        self.no_input = no_input
        self.clamped = clamped
        self.source = source
        self.enabled = enabled
        self.tip = tip
        self.show = show


class DragInt4(_Drag):
    _func = dpg.add_drag_int4

    def __init__(
        self,
        id: str = None, 
        *, 
        label: str = "", 
        parent: Union[str, SmartObject] = "", 
        before: Union[str, SmartDependant] = "",
        default_value = None,
        speed = None, 
        min_value = None,
        max_value = None,
        width: int = 0,
        callback: Callable = None,
        callback_data: Any = None,
        no_input: bool = False,
        clamped: bool = False,
        enabled: bool = True,
        source: str = "",
        tip: str = None,
        show: bool = True,
        ):
        super().__init__(
            id=id, 
            label=label, 
            parent=parent, 
            before=before,
            default_value=default_value,
            width=width,
            min_value=min_value,
            max_value=max_value,
            callback=callback,
            callback_data=callback_data,
            enabled=enabled,
            source=source,
            speed=speed,
            no_input=no_input,
            clamped=clamped,
            tip=tip,
            show=show,
            )



    





class Slider:
    _func_base = "add_slider"

    format = ConfigProperty()
    width = ConfigProperty()
    no_input = ConfigProperty()
    clamped = ConfigProperty()
    min_value = ConfigProperty()
    max_value = ConfigProperty()
    callback = ConfigProperty()
    callback_data = ConfigProperty()
    source = ConfigProperty()
    enabled = ConfigProperty()
    tip = ConfigProperty()
    show = ConfigProperty()
    # 1-value only options
    height = ConfigProperty()
    vertical = ConfigProperty()


if __name__ == '__main__':
    from containers import Window, Group, Child

    with Window() as win:
        InputText().add()
        InputInt4().add()
        InputInt3().add()
        InputInt2().add()
        InputInt().add()

        InputFloat4().add()
        InputFloat3().add()
        InputFloat2().add()
        InputFloat().add()

    win.start()