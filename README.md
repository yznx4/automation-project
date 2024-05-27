# overview
Regex Validator Project
Using Python, Tkinter, and Regular Expressions
By Yazan Rajab
5/22/2024

# imports i used
import re
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

# The regular expression pattern
pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*(\d+(\.\d+)?|".*?"|true|True|false|False)$'


# To see if the String from user is valid by our pattern
def validate_line(line):
    match = re.match(pattern, line)
    if match:
        return f"({line}) is valid."
    else:
        return f"({line}) is not valid."


# Adding text from user to the window
def add_to_result(content):
    results = [validate_line(line.strip()) for line in content]
    results_text = "\n".join(results)  # insert the line into result_text
    result_window = tk.Toplevel(root)  # create the window
    result_window.title("Validation Results")  # Title
    result_text = tk.Text(result_window, wrap='word')
    result_text.pack(expand=True, fill='both')
    result_text.insert('1.0', results_text)  # insert the text into the window
    result_text.config(state='disabled')  # user can't change on the result


# To take a file from user
def read_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        add_to_result(content)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# To read a text from the user
def read_text():
    content = (simpledialog.askstring("Input", "Enter text to validate:"))
    content = content.strip()
    if content is None:
        return
    lines = content.splitlines()
    add_to_result(lines)


# Set up the main application window
root = tk.Tk()
root.title("Regex Validator")
root.geometry("400x400")

# Frame to center buttons
button_frame = tk.Frame(root)
button_frame.pack(expand=True)

# button to open the file
open_button = tk.Button(button_frame, text="Open File", command=read_file)
open_button.pack(pady=10)

# button to enter text
text_button = tk.Button(button_frame, text="Enter Text", command=read_text)
text_button.pack(pady=10)

# Start the GUI
root.mainloop()
