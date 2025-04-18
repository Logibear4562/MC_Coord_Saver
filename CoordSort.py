import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Removed duplicate save_coordinates function


# Create the main window
root = tk.Tk()
root.geometry("600x800")
root.title("Coordinate Saver")

# Set a background color for the main window
root.configure(bg="lightblue")

# Add a frame to group widgets for better organization
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=20)

# Add a title label with a larger font and bold style
title_label = tk.Label(frame, text="Minecraft Coordinate Saver", font=("Arial", 28, "bold"), fg="darkblue", bg="lightblue")
title_label.pack(pady=10)

# Add a decorative separator line
separator = tk.Frame(frame, height=2, bd=1, relief="sunken", bg="darkblue")
separator.pack(fill="x", pady=10)

label = tk.Label(root, text="Minecraft Coordinate Saver")
label.config(font=("Arial", 26), fg="black", bg="white")
label.pack(padx=0, pady=0)

label2 = tk.Label(root, text="Enter X Coordinate ↓")
label2.config(font=("Arial", 16), fg="black", bg="white")
label2.pack(padx=0, pady=0)

textboxX = tk.Text(root, height=2, width=20)
textboxX.config(bg="white", fg="black", font=("Arial", 16))
textboxX.pack(padx=0, pady=0)

label3 = tk.Label(root, text="Enter Y Coordinate ↓")
label3.config(font=("Arial", 16), fg="black", bg="white")
label3.pack(padx=0, pady=0)

textboxY = tk.Text(root, height=2, width=20)
textboxY.config(bg="white", fg="black", font=("Arial", 16))
textboxY.pack(padx=0, pady=0)

label4 = tk.Label(root, text="Enter Z Coordinate ↓")
label4.config(font=("Arial", 16), fg="black", bg="white")
label4.pack(padx=0, pady=0)

textboxZ = tk.Text(root, height=2, width=20)
textboxZ.config(bg="white", fg="black", font=("Arial", 16))
textboxZ.pack(padx=0, pady=0)


Label6 = tk.Label(root, text="Enter Description ↓")
Label6.config(font=("Arial", 16), fg="black", bg="white")
Label6.pack(padx=0, pady=0)

textboxDesc = tk.Text(root, height=2, width=20)
textboxDesc.config(bg="white", fg="black", font=("Arial", 16))
textboxDesc.pack(padx=0, pady=0)

def save_coordinates():
    global selected_file
    if not selected_file:
        messagebox.showerror("Error", "Please select a file first!")
        return

    # Get the input values from the text boxes
    coordinateX = textboxX.get("1.0", "end").strip()
    coordinateY = textboxY.get("1.0", "end").strip()
    coordinateZ = textboxZ.get("1.0", "end").strip()
    desc = textboxDesc.get("1.0", "end").strip()

    # Validate inputs
    if not coordinateX or not coordinateY or not coordinateZ:
        messagebox.showerror("Error", "Please fill in all coordinate fields!")
        return

    try:
        # Open the file and write the coordinates
        with open(selected_file, 'a', encoding='utf-8') as f:
            f.write(f"{coordinateX}, {coordinateY}, {coordinateZ}: {desc}\n")
        messagebox.showinfo("Success", "Coordinates saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save coordinates: {e}")

button = tk.Button(root, text="Save Coordinates", command=save_coordinates)
button.config(font=("Arial", 16), fg="black", bg="white")
button.pack(padx=10, pady=10)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
def sort_coordinates(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Parse and sort the coordinates
        def distance_from_origin(line):
            try:
                coords = line.split(":")[0].split(",")
                x, y, z = map(float, coords)
                return (x**2 + y**2 + z**2)**0.5
            except ValueError:
                return float('inf')  # Handle invalid lines gracefully

        valid_lines = [line for line in lines if distance_from_origin(line) != float('inf')]
        invalid_lines = [line for line in lines if distance_from_origin(line) == float('inf')]

        if valid_lines:
            sorted_lines = sorted(valid_lines, key=distance_from_origin)

            # Write the sorted coordinates back to the file
            with open(file_name, 'w', encoding='utf-8') as f:
                f.writelines(sorted_lines)

            if invalid_lines:
                messagebox.showwarning("Warning", f"Some invalid lines were skipped:\n{''.join(invalid_lines)}")
            messagebox.showinfo("Success", "Coordinates sorted successfully!")
        else:
            messagebox.showerror("Error", "No valid coordinates to sort!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to sort coordinates: {e}")



selected_file = None

def choose_file():
    global selected_file
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        selected_file = file_path
        messagebox.showinfo("File Selected", f"Selected file: {selected_file}")

def save_coordinates():
    global selected_file
    if not selected_file:
        messagebox.showerror("Error", "Please select a file first!")
        return

    # Get the input values from the text boxes
    coordinateX = textboxX.get("1.0", "end").strip()
    coordinateY = textboxY.get("1.0", "end").strip()
    coordinateZ = textboxZ.get("1.0", "end").strip()
    desc = textboxDesc.get("1.0", "end").strip()

    # Validate inputs
    if not coordinateX or not coordinateY or not coordinateZ:
        messagebox.showerror("Error", "Please fill in all coordinate fields!")
        return

    try:
        # Open the file and write the coordinates
        with open(selected_file, 'a', encoding='utf-8') as f:
            f.write(f"{coordinateX}, {coordinateY}, {coordinateZ}: {desc}\n")
        messagebox.showinfo("Success", "Coordinates saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save coordinates: {e}")

def sort_coordinates():
    global selected_file
    if not selected_file:
        messagebox.showerror("Error", "Please select a file first!")
        return

    try:
        with open(selected_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Parse and sort the coordinates
        def distance_from_origin(line):
            try:
                coords = line.split(":")[0].split(",")
                x, y, z = map(float, coords)
                return (x**2 + y**2 + z**2)**0.5
            except ValueError:
                return float('inf')  # Handle invalid lines gracefully

        sorted_lines = sorted(lines, key=distance_from_origin)

        # Write the sorted coordinates back to the file
        with open(selected_file, 'w', encoding='utf-8') as f:
            f.writelines(sorted_lines)

        messagebox.showinfo("Success", "Coordinates sorted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to sort coordinates: {e}")

# Add a button to choose the file
file_button = tk.Button(root, text="Choose File", command=choose_file)
file_button.config(font=("Arial", 16), fg="black", bg="white")
file_button.pack(padx=10, pady=10)

# Add a button to sort the coordinates
sort_button = tk.Button(root, text="Sort Coordinates", command=sort_coordinates)
sort_button.config(font=("Arial", 16), fg="black", bg="white")
sort_button.pack(padx=10, pady=10)

# Apply a dark mode theme

# Adjust the size of the "Sort Coordinates" button to match the "Save Coordinates" button
sort_button.config(height=2, width=20)
def apply_dark_mode():
    root.configure(bg="black")
    frame.configure(bg="black")
    title_label.configure(fg="white", bg="black")
    separator.configure(bg="white")
    label.configure(fg="white", bg="black")
    label2.configure(fg="white", bg="black")
    label3.configure(fg="white", bg="black")
    label4.configure(fg="white", bg="black")
    Label6.configure(fg="white", bg="black")
    textboxX.configure(bg="gray20", fg="white", insertbackground="white")
    textboxY.configure(bg="gray20", fg="white", insertbackground="white")
    textboxZ.configure(bg="gray20", fg="white", insertbackground="white")
    textboxDesc.configure(bg="gray20", fg="white", insertbackground="white")
    button.configure(fg="white", bg="gray30")
    file_button.configure(fg="white", bg="gray30")
    sort_button.configure(fg="white", bg="gray30")

apply_dark_mode()

# Adjust all buttons to have the same size
button.config(height=2, width=20)
file_button.config(height=2, width=20)
sort_button.config(height=2, width=20)
# Update all fonts to Consolas
title_label.configure(font=("Consolas", 28, "bold"))
label.configure(font=("Consolas", 26))
label2.configure(font=("Consolas", 16))
label3.configure(font=("Consolas", 16))
label4.configure(font=("Consolas", 16))
Label6.configure(font=("Consolas", 16))
textboxX.configure(font=("Consolas", 16))
textboxY.configure(font=("Consolas", 16))
textboxZ.configure(font=("Consolas", 16))
textboxDesc.configure(font=("Consolas", 16))
button.configure(font=("Consolas", 16))
file_button.configure(font=("Consolas", 16))
sort_button.configure(font=("Consolas", 16))

root.mainloop()