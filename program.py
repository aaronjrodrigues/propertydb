import PySimpleGUI as gui
import sqlite3

def main():

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
    
    name = values[0]
    plot = values[1]
    phone = values[2]
    room = values[3]
    rent = values[4]
    startdate = values[4]
    enddate = values[5]

    print(f"Name is {values[0]}")

    conn = sqlite3.connect("database1")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS tenants(name, plotnumber, phone, roomnumber, rent, startdate, enddate)")
    conn.commit()
    cur.execute(f"INSERT INTO tenants VALUES ('{name}', '{plot}', '{phone}', '{room}' , '{rent}', '{startdate}', '{enddate}')")
    conn.commit()
def databasecreate():
    conn = None
    try:
        conn = sqlite3.connect("database1")
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close

main()
    