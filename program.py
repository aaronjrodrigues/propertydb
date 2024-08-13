import PySimpleGUI as gui
import sqlite3

def main():
    layout = [ [gui.Text("What would you like to do? ")],
               [gui.Button("Add tenant")],
               [gui.Button("Check due dates")],
               [gui.Button("Remove tenant")]
               ]
    
    window = gui.Window("Choose an option", layout)

    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            exit()
        elif event == "Add tenant":
            gui.sgprint_close()
            addtenant()
            break
        
    

def addtenant():

    layout = [ [gui.Text("Tenant name: ")],
                [gui.InputText()],
                [gui.Text("Plot number: ")],
                [gui.InputText()],
                [gui.Text("Tenant phone number: ")],
                [gui.InputText()],
                [gui.Text("Enter room number: ")],
                [gui.InputText()],
                [gui.Text("Rent p/month: ")],
                [gui.InputText()],
                [gui.Text("Start date (DD/MM/YYYY)")],
                [gui.InputText()],
                [gui.Text("End date (DD/MM/YYYY)")],
                [gui.InputText()],
                [gui.Button('Ok')], [gui.Button('Cancel')]    
                ]
    
    window = gui.Window("Hello world", layout)

    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == "Cancel" or event == "Ok":
            break
        
    name = values[0]
    plot = values[1]
    phone = values[2]
    room = values[3]
    rent = values[4]
    startdate = values[4]
    enddate = values[5]

    conn = sqlite3.connect("database1")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS tenants(name, plotnumber, phone, roomnumber, rent, startdate, enddate)")
    conn.commit()
    cur.execute(f"INSERT INTO tenants VALUES ('{name}', '{plot}', '{phone}', '{room}' , '{rent}', '{startdate}', '{enddate}')")
    conn.commit()


main()
    