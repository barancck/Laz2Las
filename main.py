import os
import laspy
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to convert .laz to .las
def convert_laz_to_las(input_file, output_file):
    try:
        with laspy.open(input_file) as laz_file:
            las_data = laz_file.read()
            las_data.write(output_file)
        messagebox.showinfo("Success", f"Converted {os.path.basename(input_file)} to {os.path.basename(output_file)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to open file explorer and select files
def select_files():
    files = filedialog.askopenfilenames(filetypes=[("LAZ files", "*.laz")], title="Select LAZ Files")
    if files:
        input_files_list.delete(0, tk.END)
        for file in files:
            input_files_list.insert(tk.END, file)

# Function to select output directory
def select_output_dir():
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if output_dir:
        output_dir_var.set(output_dir)

# Function to process all selected files
def process_files():
    output_dir = output_dir_var.get()
    if not output_dir:
        messagebox.showwarning("Warning", "Please select an output directory")
        return

    for idx in range(input_files_list.size()):
        input_file = input_files_list.get(idx)
        output_file = os.path.join(output_dir, os.path.basename(input_file).replace(".laz", ".las"))
        convert_laz_to_las(input_file, output_file)

# Setting up the GUI
root = tk.Tk()
root.title("LAZ to LAS Converter by Baran Çiçek")
root.geometry("600x400")

# Dark Mode Styling
bg_color = "#2e2e2e"  # Dark gray background
fg_color = "#ffffff"  # White text
button_bg = "#444444"  # Slightly lighter gray for buttons
button_fg = "#ffffff"  # White text on buttons
entry_bg = "#3d3d3d"  # Darker entry background
entry_fg = "#ffffff"  # White text in entries

root.configure(bg=bg_color)

# Input Files Section
input_files_label = tk.Label(root, text="Selected LAZ Files:", bg=bg_color, fg=fg_color)
input_files_label.pack(pady=5)

input_files_list = tk.Listbox(root, selectmode=tk.MULTIPLE, height=10, width=80, bg=entry_bg, fg=entry_fg)
input_files_list.pack(pady=5)

select_files_button = tk.Button(root, text="Select LAZ Files", command=select_files, bg=button_bg, fg=button_fg)
select_files_button.pack(pady=5)

# Output Directory Section
output_dir_label = tk.Label(root, text="Select Output Directory:", bg=bg_color, fg=fg_color)
output_dir_label.pack(pady=5)

output_dir_var = tk.StringVar()
output_dir_entry = tk.Entry(root, textvariable=output_dir_var, width=60, bg=entry_bg, fg=entry_fg, insertbackground=fg_color)
output_dir_entry.pack(pady=5)

select_output_dir_button = tk.Button(root, text="Select Output Directory", command=select_output_dir, bg=button_bg, fg=button_fg)
select_output_dir_button.pack(pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=process_files, bg="green", fg=button_fg, width=20)
convert_button.pack(pady=20)

root.mainloop()
