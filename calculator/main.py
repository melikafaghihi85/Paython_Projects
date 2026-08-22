from tkinter import Tk, Entry, StringVar, Button


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""

        # صفحه نمایش
        Entry(
            master,
            width=17,
            bg="#ccddff",
            font=("Arial Bold", 28),
            textvariable=self.equation,
            justify="right"
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            padx=5,
            pady=5
        )

        # دکمه‌ها
        Button(
            master, text="(", bg="white", relief="flat",
            command=lambda: self.show("(")
        ).grid(row=1, column=0, padx=2, pady=2, sticky="nsew")

        Button(
            master, text=")", bg="white", relief="flat",
            command=lambda: self.show(")")
        ).grid(row=1, column=1, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="%", bg="white", relief="flat",
            command=lambda: self.show("%")
        ).grid(row=1, column=2, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="/", bg="white", relief="flat",
            command=lambda: self.show("/")
        ).grid(row=1, column=3, padx=2, pady=2, sticky="nsew")


        Button(
            master, text="7", bg="#F8C8DC", relief="flat",
            command=lambda: self.show(7)
        ).grid(row=2, column=0, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="8", bg="white", relief="flat",
            command=lambda: self.show(8)
        ).grid(row=2, column=1, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="9", bg="#F8C8DC", relief="flat",
            command=lambda: self.show(9)
        ).grid(row=2, column=2, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="x", bg="white", relief="flat",
            command=lambda: self.show("*")
        ).grid(row=2, column=3, padx=2, pady=2, sticky="nsew")


        Button(
            master, text="4", bg="white", relief="flat",
            command=lambda: self.show(4)
        ).grid(row=3, column=0, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="5", bg="#F8C8DC", relief="flat",
            command=lambda: self.show(5)
        ).grid(row=3, column=1, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="6", bg="white", relief="flat",
            command=lambda: self.show(6)
        ).grid(row=3, column=2, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="-", bg="white", relief="flat",
            command=lambda: self.show("-")
        ).grid(row=3, column=3, padx=2, pady=2, sticky="nsew")


        Button(
            master, text="1", bg="#F8C8DC", relief="flat",
            command=lambda: self.show(1)
        ).grid(row=4, column=0, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="2", bg="white", relief="flat",
            command=lambda: self.show(2)
        ).grid(row=4, column=1, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="3", bg="#F8C8DC", relief="flat",
            command=lambda: self.show(3)
        ).grid(row=4, column=2, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="+", bg="white", relief="flat",
            command=lambda: self.show("+")
        ).grid(row=4, column=3, padx=2, pady=2, sticky="nsew")


        Button(
            master, text="C", bg="white", relief="flat",
            command=self.clear
        ).grid(row=5, column=0, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="0", bg="white", relief="flat",
            command=lambda: self.show(0)
        ).grid(row=5, column=1, padx=2, pady=2, sticky="nsew")

        Button(
            master, text=".", bg="white", relief="flat",
            command=lambda: self.show(".")
        ).grid(row=5, column=2, padx=2, pady=2, sticky="nsew")

        Button(
            master, text="=", bg="lightblue", relief="flat",
            command=self.solve
        ).grid(row=5, column=3, padx=2, pady=2, sticky="nsew")
        Button(
            master, text="Back", bg="pink", relief="flat",
            command=self.backspace
        ).grid(row=5, column=0, padx=2, pady=2, sticky="nsew")
        
        # تنظیم اندازه مساوی ستون‌ها و ردیف‌ها
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

        for i in range(1, 6):
            master.grid_rowconfigure(i, weight=1)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)
    def backspace(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)


root = Tk()
calculator = Calculator(root)
root.mainloop()