import sqlite3

from tkinter import *
from tkinter import ttk

def main():
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


def tenantlist():
    ...
    
def addtenant():

    def on_submit():
        name = name_entry.get()
        plot = plot_entry.get()
        phone = plot_entry.get()
        room = room_entry.get()
        rent = rent_entry.get()
        startdate = start_entry.get()
        enddate = end_entry.get()

        conn = sqlite3.connect("database1")
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS tenants(name, plotnumber, phone, roomnumber, rent, startdate, enddate)")
        conn.commit()
        cur.execute(f"INSERT INTO tenants VALUES ('{name}', '{plot}', '{phone}', '{room}' , '{rent}', '{startdate}', '{enddate}')")
        conn.commit()

        root.destroy()
    
    root = Tk()
    root.title("Add new tenant")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="Tenant name").grid(column=1, row=1)
    name_entry = ttk.Entry(mainframe, width=7)
    name_entry.grid(column=2, row=1)
    
    ttk.Label(mainframe, text="Plot number").grid(column=1, row=2)
    plot_entry = ttk.Entry(mainframe, width=7)
    plot_entry.grid(column=2, row=2)

    ttk.Label(mainframe, text="Phone number").grid(column=1, row=3)
    phone_entry = ttk.Entry(mainframe, width=7)
    phone_entry.grid(column=2, row=3)

    ttk.Label(mainframe, text="Room number").grid(column=1, row=4)
    room_entry = ttk.Entry(mainframe, width=7)
    room_entry.grid(column=2, row=4)

    ttk.Label(mainframe, text="Rent per month").grid(column=1, row=5)
    rent_entry = ttk.Entry(mainframe, width=7)
    rent_entry.grid(column=2, row=5)

    ttk.Label(mainframe, text="Start date").grid(column=1, row=6)
    start_entry = ttk.Entry(mainframe, width=7)
    start_entry.grid(column=2, row=6)

    ttk.Label(mainframe, text="End date").grid(column=1, row=7)
    end_entry = ttk.Entry(mainframe, width=7)
    end_entry.grid(column=2, row=7)

    ttk.Button(mainframe, text="Exit", command=exit).grid(column=1, row=8)
    ttk.Button(mainframe, text="Submit", command=on_submit).grid(column=2, row=8)



main()
    