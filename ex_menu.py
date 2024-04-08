import PySimpleGUI as sg

sg.theme('DarkAmber')  # No gray windows please!

menu_def = [['&File', ['&Open', '&Save', '&Preferences', 'E&xit' ]],
                ['&Edit', ['&Copy', ['Special', 'Normal',], 'Undo'],],
                ['&Help', ['&About...']]
               ]


# STEP 1 define the layout
layout = [ 
            [sg.Menu(menu_def, tearoff=False, pad=(20,1))],
            [sg.Text('This is a very basic PySimpleGUI layout')],
            [sg.Input()],
            [sg.Input()],
            [sg.Button('Button'), sg.Button('Exit')]
         ]

#STEP 2 - create the window
window = sg.Window('My new window', layout, grab_anywhere=True)

# STEP3 - the event loop
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    print(event, values)
    if event in (None, 'Exit'):     # If user closeddow with X or if user clicked "Exit" button then exit
        break
    if event == 'Button':
      print('You pressed the button')
window.close()