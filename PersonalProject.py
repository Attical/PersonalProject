import PySimpleGUI as sg

with open("ToDoList.txt", "r") as file:
    data = file.read()

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Your todo list:')],
            [sg.Text(data, key='-TEXT-')], #tasks will go here
            [sg.Text('Input new tasks:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    with open("ToDoList.txt", "a") as file:
        file.write("\n") #this works as intended if the cursor is set to end of text instead of on a new line
        file.write(values[0])

    with open("ToDoList.txt", "r") as file:
        data = file.read()
            
    window['-TEXT-'].update(data)

window.close()