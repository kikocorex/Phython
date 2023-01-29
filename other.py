import tkinter as tk


class Calculator:
    def add(self, x, y):
        return x + y


calc = Calculator()
root = tk.Tk()


def button_clicked():
    x = int(entry1.get())
    y = int(entry2.get())

    result = calc.add(x, y)

    label["text"] = result


entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
label = tk.Label(root)

button = tk.Button(root, text="Calculate", command=button_clicked)

entry1.pack()
entry2.pack()
label.pack()
button.pack()

root.mainloop()
