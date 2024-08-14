import PySimpleGUI as gui
import sqlite3

from tkinter import *
from tkinter import ttk

def main():
    
    #layout = [ [gui.Text("What would you like to do? ")],
     #          [gui.Button("Add tenant")],
      #         [gui.Button("Check due dates")],
       #        [gui.Button("Remove tenant")],
        #       [gui.Button("Check list of tenants")]
             #  ]
    
    #window = gui.Window("Choose an option", layout)

    root = Tk()
    root.title("Choose an option")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #option = StringVar()
    #option_entry = ttk.Entry(mainframe, width=7, textvariable=option)
    #option_entry.grid(column=2, row=1, sticky=(W, E))
    ttk.Label(mainframe, text="What would you like to do?").grid(column=2, row=1, sticky=E)
    ttk.Button(mainframe, text="Add tenant", command=addtenant).grid(column=2, row=2)
    ttk.Button(mainframe, text="View current tenants").grid(column=2, row=3)
    ttk.Button(mainframe, text="Exit", command=quit).grid(column=2, row=4)



    root.mainloop()
    

    #while True:
     #   event, values = window.read()
      #  if event == gui.WIN_CLOSED:
       #     exit()
        #elif event == "Add tenant":
         #   gui.sgprint_close()
          #  addtenant()
           # break
       # elif event == "Check list of tenants":
        #    gui.sgprint_close()
         #   tenantlist()
          #  break


def tenantlist():
    ...
    
        
    

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
    
    window = gui.Window("Add tenant", layout)

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
    