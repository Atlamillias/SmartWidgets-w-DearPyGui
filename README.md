## Note: This can only be used with dearpygui 0.6.

# SmartWidgets w/DearPyGui
Object-oriented bindings for DearPyGui (https://github.com/hoffstadt/DearPyGui). It is fully compatable with everything within the DearPyGui library. All items accept the exact same arguments (plus a few), have nearly the same default values, and are used similarly.

# Usage
Typical usage of SmartWidgets is almost identical to Dearpygui. A big difference is that you don't need to pass a **name** argument to every item (although you can)!  

While I plan on expanding this section in detail, here's an example:


```
from smartwidgets import *


with Window() as main:  
    with MenuBar() as mainmenu:
        with Menu():
            InputText(label="Hi mom.", width=50).add()
            Button(label="I'm a Button.").add()
            with Menu():
                InputText(label="Hi mom (again).").add()
                Button(label="I'm another Button.").add()
    with Group():
        with Group(horizontal=True):
            with Child(height=200):
                Button().add()
                Button().add()
                Button().add()
                Button().add()
    with Group():
        with Group(horizontal=True):
            with Child(width=200):
                InputFloat(width=100).add()
                InputFloat2().add()
                InputFloat3().add()
                InputFloat4().add()
            with Child(width=200):
                InputInt(width=100).add()
                InputInt2().add()
                InputInt3().add()
                InputInt4().add()
            with Child(width=200):
                InputText().add()
                InputText().add()
                InputText().add()
                InputText().add()
    with Group():
        with Group(horizontal=True):
            with Child(width=200):
                SliderFloat(width=100).add()
                SliderFloat2().add()
                SliderFloat3().add()
                SliderFloat4().add()
            with Child(width=200):
                SliderInt(width=100).add()
                SliderInt2().add()
                SliderInt3().add()
                SliderInt4().add()
    with Group():
        with Group(horizontal=True):
            with Child(width=200):
                DragFloat(width=100).add()
                DragFloat2().add()
                DragFloat3().add()
                DragFloat4().add()
            with Child(width=200):
                DragInt(width=100).add()
                DragInt2().add()
                DragInt3().add()
                DragInt4().add()


main.start()
```


You can perform setup on an item (configure it) beforehand...


```

main = Window(label="TestWindow", height=300)

main.no_close = True
main.no_collapse = True

# ... and then add it later

with main:
    pass

# OR 

main.add()
main.end()

```

The **name** argument commonly used in DearPyGui has been replaced with **id**. An items' **id** is automatically generated, but you can pass one in yourself if you want.


```

a_button = Button("Just a button")
another_button = Button()

print(a_button.id)
# >>> "Just a button"
print(another_button.id)
# >>> "Button<0>"

```

When using functions within DearPyGui that require **item** or **name**, you can pass **item.id** as the value.




This is a work-in progress, and while there aren't bindings for every item DearPyGui has in it's library yet, many of the common ones are.
