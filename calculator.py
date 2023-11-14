import tkinter as tk

def add_number(number):
    active_entry.insert(tk.END, number)

def select_entry(entry):
    global active_entry
    active_entry = entry

def clear_entry():
    active_entry.delete(0, tk.END)

def clear_all():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ", bg='black', fg='white')

def calculate():
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    operation = operation_var.get()

    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        else:
            result = "Invalid operation"

        label_result.config(text=f"Result: {result}", bg='red', fg='white')
    except ValueError:
        label_result.config(text="Error: Invalid input", bg='red', fg='white')


root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='black')
root.geometry('500x450')


entry_num1 = tk.Entry(root, width=15, font=('Arial', 14))
entry_num1.grid(row=0, column=0, padx=10, pady=10)

operation_var = tk.StringVar()
operation_choices = ["+", "-", "*", "/"]
operation_dropdown = tk.OptionMenu(root, operation_var, *operation_choices)
operation_var.set("+")
operation_dropdown.config(width=5, font=('Arial', 14), bg='yellow')
operation_dropdown.grid(row=0, column=1, padx=10, pady=10)

entry_num2 = tk.Entry(root, width=15, font=('Arial', 14))
entry_num2.grid(row=0, column=2, padx=10, pady=10)


number_buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '='
]

row_val = 1
col_val = 0

for button in number_buttons:
    tk.Button(root,
              text=button,
              width=5,
              height=2,
              font=('Arial', 14),
              bg='gray',
              fg='black',
              command=lambda b=button: add_number(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1


clear_entry_button = tk.Button(root, text="Clear Entry", command=clear_entry, font=('Arial', 14), bg='yellow', fg='black')
clear_entry_button.grid(row=row_val, column=0, padx=5, pady=5)


clear_all_button = tk.Button(root, text="Clear All", command=clear_all, font=('Arial', 14), bg='yellow', fg='black')
clear_all_button.grid(row=row_val, column=1, padx=5, pady=5)


calculate_button = tk.Button(root, text="Calculate", command=calculate, font=('Arial', 14), bg='yellow', fg='black')
calculate_button.grid(row=row_val, column=2, padx=5, pady=5)


label_result = tk.Label(root, text="Result: ", font=('Arial', 14), bg='red', fg='white')
label_result.grid(row=row_val+1, column=0, columnspan=3, pady=5)

active_entry = entry_num1

entry_num1.bind("<Button-1>", lambda event: select_entry(entry_num1))
entry_num2.bind("<Button-1>", lambda event: select_entry(entry_num2))

root.mainloop()
