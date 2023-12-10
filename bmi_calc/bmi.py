import time
import tkinter as tk

def weight_label():
    kg_label = tk.Label(display_frame, text='kg', font=('Arial', 25), bg='white')
    kg_label.place(relx=0, rely=0, anchor='nw')

def height_label():
    cm_label = tk.Label(display_frame, text='cm', font=('Arial', 25), bg='white')
    cm_label.place(relx=0, rely=0, anchor='nw')

def bmi_label():
    bmi_label = tk.Label(display_frame, text='bmi', font=('Arial', 25), bg='white')
    bmi_label.place(relx=0, rely=0, anchor='nw')

def result_label():
    result_label = tk.Label(display_frame, text='res', font=('Arial', 25), bg='white')
    result_label.place(relx=0, rely=0, anchor='nw')

def add_to_display(value):
    current_text = display_var.get()
    if current_text == '0' and value != '.':
        display_var.set(value)
    else:
        display_var.set(current_text + str(value))

def clear_display():
    display_var.set('0')

def enter_pressed():
    global weight, height, calc_state
    bmi = 0
    if calc_state == 0:
        weight_label()
        weight = float(display_var.get())
        display_var.set('0')
        calc_state = 1
        height_label()
    elif calc_state == 1:
        height = float(display_var.get())
        display_var.set('0')
        bmi_label()
        bmi = calculate_bmi(weight, height)
        display_var.set(f"{bmi:.2f}")
        calc_state = 2
        # Calculate BMI
    elif calc_state == 2:
        result_label()
        bmi = calculate_bmi(weight, height)
        if bmi < 18.5:
            display_var.set('Underweight')
        elif 18.5 <= bmi <= 25.0:
            display_var.set('Normal')
        else :
            display_var.set('Overweight')
        calc_state = 0
        
def calculate_bmi(weight, height):
    height_meters = height / 100  # Convert height from cm to meters
    bmi = weight / ((height_meters) ** 2)
    return bmi

root = tk.Tk()
root.geometry('300x500')
root.configure(bg="#333333")

# Display Frame
display_frame = tk.Frame(root, width=280, height=70, bg='white', highlightthickness=2, highlightbackground='black')
display_frame.pack(padx=10, pady=10)

display_var = tk.StringVar()
display_var.set('0')

weight = 0.0
height = 0.0
calc_state = 0  # State: 0 - Enter weight, 1 - Enter height, 2 - Calculate BMI
display = tk.Label(display_frame, textvariable=display_var, font=('Arial', 20), width=16, anchor='e', relief='ridge', bd=5)
display.pack(expand=True, fill='both')
weight_label()

# Button Frame
button_frame = tk.Frame(root, bg="#333333")
button_frame.pack()

# Number Buttons
button_values = [
    ('7', '8', '9'),
    ('4', '5', '6'),
    ('1', '2', '3'),
    ('.', '0', 'Clear')
]

for i, row in enumerate(button_values):
    for j, value in enumerate(row):
        if value != 'Clear':
            tk.Button(button_frame, text=value, width=5, height=2, font=('Arial', 12), command=lambda v=value: add_to_display(v)).grid(row=i, column=j, padx=5, pady=5)
        else:
            tk.Button(button_frame, text=value, width=5, height=2, font=('Arial', 12), command=clear_display).grid(row=i, column=j, padx=5, pady=5)

# Enter Button
enter_button = tk.Button(root, text="Enter", width=10, height=2, font=('Arial', 12), command=enter_pressed)
enter_button.pack(pady=20)

root.mainloop()
