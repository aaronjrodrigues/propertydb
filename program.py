import PySimpleGUI as gui

def main():

    layout = [ [gui.Text("Tenant name: ")],
               [gui.InputText()],
               [gui.Text("Plot number: ")],
               [gui.InputText()],
               [gui.Text("Tenant phone number: ")],
               [gui.InputText()],
               [gui.Text("Rent p/month: ")],
               [gui.InputText()],
               [gui.Text("Start date: ")],
               [gui.InputText()],
               [gui.Text("End date: ")],
               [gui.InputText()],

               [gui.Button('Ok')], [gui.Button('Cancel')]

                
            ]
    window = gui.Window("Hello world", layout)

    while True:
        event, values = window.read()

        if event == gui.WIN_CLOSED or event == "Cancel":
            break

    print(f"Name is {values[0]}")

main()
    