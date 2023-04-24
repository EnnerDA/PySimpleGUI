# import PySimpleGUI as sg

# Основные команды
Для выбора цветовой схемы:
```python
sg.theme('Название желаемой темы')
```
Перечень стандартных тем:
```python
sg.theme_previewer()
```

Конструкция окна:
```python
import PySimpleGUI as sg

layout = [[sg.Text('Very basic Window')],
          [sg.Text('Click X in titlebar or the Exit button')],
          [sg.Input('', key = 'id2')],
          [sg.Button('Go', key = 'id1'), sg.Button('Бежать', key = 'Exit')]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(event, values)
    k = values['id2']
    print(k)
    if event in(sg.WIN_CLOSED, 'Exit'):
        break

window.close()
```
