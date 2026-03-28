import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ----------------- DATABASE -----------------
def connect_db():
    conn = sqlite3.connect("hostel.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bookings(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            roll TEXT,
            room TEXT,
            department TEXT
        )
    """)
    conn.commit()
    conn.close()

connect_db()

# ----------------- MAIN CLASS -----------------
class HostelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hostel Room Allotment System")
        self.root.geometry("800x500")
        
        title = tk.Label(self.root, text="Hostel Room Allotment Booking System",
                         font=("Arial", 20, "bold"))
        title.pack(pady=10)

        # ------- Variables -------
        self.name_var = tk.StringVar()
        self.roll_var = tk.StringVar()
        self.room_var = tk.StringVar()
        self.dept_var = tk.StringVar()

        # ------- FORM FRAME -------
        form = tk.Frame(self.root)
        form.pack(pady=10)

        tk.Label(form, text="Name:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(form, textvariable=self.name_var, width=25).grid(row=0, column=1)

        tk.Label(form, text="Roll No:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(form, textvariable=self.roll_var, width=25).grid(row=1, column=1)

        tk.Label(form, text="Room No:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(form, textvariable=self.room_var, width=25).grid(row=2, column=1)

        tk.Label(form, text="Department:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(form, textvariable=self.dept_var, width=25).grid(row=3, column=1)

        # ------- BUTTONS -------
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Booking", width=15, command=self.add_data).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update", width=15, command=self.update_data).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete", width=15, command=self.delete_data).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Clear", width=15, command=self.clear_fields).grid(row=0, column=3, padx=5)

        # ------- TABLE -------
        table_frame = tk.Frame(self.root)
        table_frame.pack(pady=10)

        self.table = ttk.Treeview(table_frame, columns=("id", "name", "roll", "room", "dept"),
                                  show="headings", height=10)

        self.table.heading("id", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("roll", text="Roll No")
        self.table.heading("room", text="Room No")
        self.table.heading("dept", text="Department")

        self.table.column("id", width=40)
        self.table.column("name", width=150)
        self.table.column("roll", width=100)
        self.table.column("room", width=80)
        self.table.column("dept", width=120)

        self.table.bind("<ButtonRelease-1>", self.get_selected_row)
        self.table.pack()

        self.load_data()

    # ----------------- FUNCTIONS -----------------

    def add_data(self):
        if self.name_var.get() == "" or self.roll_var.get() == "" or self.room_var.get() == "":
            messagebox.showwarning("Error", "Please fill all fields!")
            return
        
        conn = sqlite3.connect("hostel.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO bookings(name, roll, room, department) VALUES (?, ?, ?, ?)",
                    (self.name_var.get(), self.roll_var.get(), self.room_var.get(), self.dept_var.get()))
        conn.commit()
        conn.close()
        
        self.load_data()
        self.clear_fields()
        messagebox.showinfo("Success", "Booking added!")

    def load_data(self):
        conn = sqlite3.connect("hostel.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM bookings")
        rows = cur.fetchall()
        conn.close()

        self.table.delete(*self.table.get_children())
        for row in rows:
            self.table.insert("", tk.END, values=row)

    def get_selected_row(self, event):
        selected = self.table.focus()
        values = self.table.item(selected, "values")
        if values:
            self.selected_id = values[0]
            self.name_var.set(values[1])
            self.roll_var.set(values[2])
            self.room_var.set(values[3])
            self.dept_var.set(values[4])

    def update_data(self):
        try:
            conn = sqlite3.connect("hostel.db")
            cur = conn.cursor()
            cur.execute("""
                UPDATE bookings SET name=?, roll=?, room=?, department=? WHERE id=?
            """, (self.name_var.get(), self.roll_var.get(), self.room_var.get(),
                  self.dept_var.get(), self.selected_id))
            conn.commit()
            conn.close()
            self.load_data()
            messagebox.showinfo("Updated", "Booking updated!")
        except:
            messagebox.showwarning("Error", "Select a record first!")

    def delete_data(self):
        try:
            conn = sqlite3.connect("hostel.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM bookings WHERE id=?", (self.selected_id,))
            conn.commit()
            conn.close()
            self.load_data()
            self.clear_fields()
            messagebox.showinfo("Deleted", "Booking deleted!")
        except:
            messagebox.showwarning("Error", "Select a record first!")

    def clear_fields(self):
        self.name_var.set("")
        self.roll_var.set("")
        self.room_var.set("")
        self.dept_var.set("")


# ----------------- MAIN -----------------
root = tk.Tk()
app = HostelApp(root)
root.mainloop()
