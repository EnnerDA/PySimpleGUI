import PySimpleGUI as sg


sg.theme('DarkGrey6')

layout = [
    [sg.Button('Ебошь кнопку',enable_events=True, key='but1', font='Helvetica 16')],
    [sg.Text('', size=(25, 1), key='text1', font='Helvetica 16')]
    ]

window = sg.Window('Нажиматель кнопки', layout, size=(350,100))

i = 1
while True:
    event, values = window.read()
    if event == 'but1':
        window['text1'].update(f'Наебошил {i} раз')
        i +=1
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    

window.close()
