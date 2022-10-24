import PySimpleGUI as sg
import pyautogui
import time

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Enter Message', size=(15, 1)), sg.InputText(key='msg')],
          [sg.Text('How many times..?', size=(15, 1)), sg.InputText(key='times_input')],
          [sg.Text('Enter delay(second)', size=(15, 1)), sg.InputText(default_text='0.2', key='delay_input')],
          [sg.Button('Start', key='start_btn'), sg.Button('Cancel'),
           sg.Text('Welcome to TantaiHaha Spammer', key='status_msg')]
          ]

# Create the Window
window = sg.Window('TantaiHaha Spammer', icon="bin/favicon.ico", layout=layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    # onClick start button
    if event == 'start_btn':
        enable = True
        msg = str(values['msg'])
        # check values
        try:
            time_input = int(values['times_input'])
        except ValueError:
            window['times_input'].update(value='1')
            window['status_msg'].update("Times isn't integer, Please try again.")
            enable = False
        try:
            delay = float(values['delay_input'])
        except ValueError:
            window['delay_input'].update(value='0.2')
            window['status_msg'].update("Delay isn't integer or decimal.  Please try again.")
            enable = False

        now = 1
        if enable:
            # before start spam
            count = 5
            for i in range(0, count):
                window['status_msg'].update("Start in " + str(count))
                window.refresh()
                count -= 1
                time.sleep(1)
            window['status_msg'].update("Start in Go go go!")
            # spam start
            for i in range(0, int(time_input)):
                window['status_msg'].update("Message has sent " + str(now) + " times!")
                now = now + 1
                window.refresh()
                pyautogui.typewrite(msg + "\n")
                time.sleep(delay)
                if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
                    break
            window['status_msg'].update("Sent message " + str(time_input) + " finish!!")
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

window.close()
