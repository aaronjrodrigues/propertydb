import sqlite3

from tkinter import *
from tkinter import ttk

import sv_ttk

root = Tk()

def main():
    sv_ttk.set_theme("dark")
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
    ttk.Button(mainframe, text="View current tenants", command=tenantlist).grid(column=2, row=3)
    ttk.Button(mainframe, text="Add a new payment",command=addpayment).grid(column=2, row=4)
    ttk.Button(mainframe, text="Exit", command=quit).grid(column=2, row=5)

    root.mainloop()

def addpayment():

    def on_submit():
        
        name = name_entry.get()
        paymentdate = paymentdate_entry.get()
        amount = amount_entry.get()
        id = id_entry.get()

        conn = sqlite3.connect("database1")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS payments(name, paymentdate, amount, id)")
        conn.commit()
        cur.execute(f"INSERT INTO payments VALUES ('{name}', '{paymentdate}', '{amount}', '{id}')")
        conn.commit()
        top.destroy()

    top = Toplevel(root)
    sv_ttk.set_theme("dark")
    top.title("Add a payment")
    mainframe = ttk.Frame(top, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    top.columnconfigure(0, weight=1)
    top.columnconfigure(0, weight=1)

    ttk.Label(mainframe, text="Please enter the following details: ").grid(column=1, row=1)

    ttk.Label(mainframe, text="Name").grid(column=1, row=2)
    name_entry = ttk.Entry(mainframe, width=7)
    name_entry.grid(column=2, row=2)

    ttk.Label(mainframe, text="Payment date").grid(column=1, row=3)
    paymentdate_entry = ttk.Entry(mainframe, width=7)
    paymentdate_entry.grid(column=2, row=3)

    ttk.Label(mainframe, text="Payment amount").grid(column=1, row=4)
    amount_entry = ttk.Entry(mainframe, width=7)
    amount_entry.grid(column=2, row=4)

    ttk.Label(mainframe, text="Omang/Passport number").grid(column=1, row=5)
    id_entry = ttk.Entry(mainframe, width=7)
    id_entry.grid(column=2, row=5)

    ttk.Button(mainframe, text="Exit", command=exit).grid(column=1, row=6)
    ttk.Button(mainframe, text="Submit", command=on_submit).grid(column=2, row=6) 


def tenantlist():
    conn = sqlite3.connect("database1")
    cur = conn.cursor()
    try:
        response = cur.execute("SELECT * FROM TENANTS")
        
        tenants = response.fetchall()

        top = Toplevel(root)
        sv_ttk.set_theme("dark")
        top.title("Tenant list")
        mainframe = ttk.Frame(top, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        top.columnconfigure(0, weight=1)
        top.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="Here is the following list of tenants\n").grid(column=1, row=1)

        ttk.Label(mainframe, text="Name, Omang/Passport, Plot number, Phone number, Room number, Rent, Start date, End date\n").grid(column=1, row=2)
        row = 3
        for x in tenants:
            ttk.Label(mainframe, text=f"{str(x)}").grid(column=1, row=row)
            print(x)
            row = row + 1
            print(row)

        ttk.Label(mainframe, text=f"\nThere are currently {len(tenants)} tenants").grid(column=1, row=row)
        row = row + 1

    except sqlite3.OperationalError:
        error = Toplevel(root)
        sv_ttk.set_theme("dark")
        error.title("Database is empty")
        mainframe1 = ttk.Frame(error, padding="3 3 12 12")
        mainframe1.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(mainframe1, text="ERROR: No tenant found, please add a new tenant\n").grid(column=1, row=1)
        ttk.Button(mainframe1, text="Okay", command=error.destroy).grid(column=1, row=2)    
        ttk.Button(mainframe1, text="Exit", command=exit).grid(column=2, row=2)

def addtenant():

    def on_submit():
        name = name_entry.get()
        id = name_entry.get()
        plot = plot_entry.get()
        phone = plot_entry.get()
        room = room_entry.get()
        rent = rent_entry.get()
        startdate = start_entry.get()
        enddate = end_entry.get()

        conn = sqlite3.connect("database1")
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS tenants(name, id, plotnumber, phone, roomnumber, rent, startdate, enddate)")
        conn.commit()
        cur.execute(f"INSERT INTO tenants VALUES ('{name}', '{id}', '{plot}', '{phone}', '{room}' , '{rent}', '{startdate}', '{enddate}')")
        conn.commit()

        top.destroy()
    
    top = Toplevel(root)
    sv_ttk.set_theme("dark")
    top.title("Add new tenant")
    mainframe = ttk.Frame(top, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    top.columnconfigure(0, weight=1)
    top.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="Tenant name").grid(column=1, row=1)
    name_entry = ttk.Entry(mainframe, width=7)
    name_entry.grid(column=2, row=1)

    ttk.Label(mainframe, text="Omang/Passport number").grid(column=1, row=2)
    name_entry = ttk.Entry(mainframe, width=7)
    name_entry.grid(column=2, row=2)
    
    ttk.Label(mainframe, text="Plot number").grid(column=1, row=3)
    plot_entry = ttk.Entry(mainframe, width=7)
    plot_entry.grid(column=2, row=3)

    ttk.Label(mainframe, text="Phone number").grid(column=1, row=4)
    phone_entry = ttk.Entry(mainframe, width=7)
    phone_entry.grid(column=2, row=4)

    ttk.Label(mainframe, text="Room number").grid(column=1, row=5)
    room_entry = ttk.Entry(mainframe, width=7)
    room_entry.grid(column=2, row=5)

    ttk.Label(mainframe, text="Rent per month").grid(column=1, row=6)
    rent_entry = ttk.Entry(mainframe, width=7)
    rent_entry.grid(column=2, row=6)

    ttk.Label(mainframe, text="Start date").grid(column=1, row=7)
    start_entry = ttk.Entry(mainframe, width=7)
    start_entry.grid(column=2, row=7)

    ttk.Label(mainframe, text="End date").grid(column=1, row=8)
    end_entry = ttk.Entry(mainframe, width=7)
    end_entry.grid(column=2, row=8)

    ttk.Button(mainframe, text="Exit", command=exit).grid(column=1, row=9)
    ttk.Button(mainframe, text="Submit", command=on_submit).grid(column=2, row=9)



main()
    