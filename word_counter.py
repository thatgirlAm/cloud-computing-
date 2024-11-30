# Author : Amaëlle DIOP - 461543

# --imports
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar

# --global
FILEPATH = None
FILE = None
COUNT = 0

# --finding the document
def load_file():
    global FILEPATH
    global FILE
    FILEPATH = filedialog.askopenfilename(title="Choisir un document texte", filetypes=(("documents texte", "*.txt"), ("Tous types", "*.*")))
    if FILEPATH:
        label_file.config(text=FILEPATH)
    else:
        label_file.config(text="No file selected")

# --count the words
def word_counter():
    global COUNT
    if FILEPATH is None:  # Ensure a file has been selected
        messagebox.showerror("Error", "No file selected! Please choose a file first.")
        return

    try:
        file = open(FILEPATH, "r")
        total_lines = sum(1 for _ in file)
        file.close()

        file = open(FILEPATH, "r")
        lines_processed = 0
        COUNT = 0

        progress_bar["maximum"] = total_lines  # Set progress bar max value

        for line in file:
            COUNT += len(line.split())
            lines_processed += 1
            progress_bar["value"] = lines_processed  # Update progress bar
            percent_label.config(text=f"{(lines_processed / total_lines) * 100:.2f}%")  # Update percentage label
            window.update_idletasks()  # Refresh the GUI

        file.close()
        percent_label.config(text=f"100.00%")
        result_label.config(text=f"Total words: {COUNT}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# --visual window
window = tk.Tk()
window.title("Word Counter Application")

# ----Buttons
button_pdf = tk.Button(window, text="Choose text file", command=load_file, padx=10, pady=5)
button_validation = tk.Button(window, text="Count words", command=word_counter, padx=10, pady=5)

# ----Text
label_file = tk.Label(window, text="Load the text file")
percent_label = tk.Label(window, text="0.00%")
result_label = tk.Label(window, text="Total words: 0")

# ----Progress Bar
progress_bar = Progressbar(window, orient="horizontal", length=200, mode="determinate")

# ----Loading buttons
label_file.pack()
button_pdf.pack()
button_validation.pack()
progress_bar.pack()
percent_label.pack()
result_label.pack()

window.mainloop()
