import tkinter as tk
from tkinter import ttk


def clear():
    entry_km.delete(0, tk.END)
    entry_meters.delete(0, tk.END)
    entry_cm.delete(0, tk.END)
    entry_kg.delete(0, tk.END)
    entry_liters.delete(0, tk.END)
    entry_celsius.delete(0, tk.END)
    
    label_result_km.config(text="")
    label_result_meters.config(text="")
    label_result_cm.config(text="")
    label_result_kg.config(text="")
    label_result_liters.config(text="")
    label_result_celsius.config(text="")

# Creating the main window
root = tk.Tk()
root.title("Metric to Imperial Converter")

# Frames for each conversion
frame_km = ttk.Frame(root, padding="10")
frame_km.grid(row=0, column=0, sticky=(tk.W, tk.E))
ttk.Label(frame_km, text="Kilometers:").grid(row=0, column=0, sticky=tk.W)
entry_km = ttk.Entry(frame_km)
entry_km.grid(row=0, column=1, sticky=(tk.W, tk.E))
label_result_km = ttk.Label(frame_km, text="")
label_result_km.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

frame_meters = ttk.Frame(root, padding="10")
frame_meters.grid(row=1, column=0, sticky=(tk.W, tk.E))
ttk.Label(frame_meters, text="Meters:").grid(row=0, column=0, sticky=tk.W)
entry_meters = ttk.Entry(frame_meters)
entry_meters.grid(row=0, column=1, sticky=(tk.W, tk.E))
label_result_meters = ttk.Label(frame_meters, text="")
label_result_meters.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

frame_cm = ttk.Frame(root, padding="10")
frame_cm.grid(row=2, column=0, sticky=(tk.W, tk.E))
ttk.Label(frame_cm, text="Centimeters:").grid(row=0, column=0, sticky=tk.W)
entry_cm = ttk.Entry(frame_cm)
entry_cm.grid(row=0, column=1, sticky=(tk.W, tk.E))
label_result_cm = ttk.Label(frame_cm, text="")
label_result_cm.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

frame_kg = ttk.Frame(root, padding="10")
frame_kg.grid(row=3, column=0, sticky=(tk.W, tk.E))
ttk.Label(frame_kg, text="Kilograms:").grid(row=0, column=0, sticky=tk.W)
entry_kg = ttk.Entry(frame_kg)
entry_kg.grid(row=0, column=1, sticky=(tk.W, tk.E))
label_result_kg = ttk.Label(frame_kg, text="")
label_result_kg.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

frame_liters = ttk.Frame(root, padding="10")
frame_liters.grid(row=4, column=0, sticky=(tk.W, tk.E))
ttk.Label(frame_liters, text="Liters:").grid(row=0, column=0, sticky=tk.W)
entry_liters = ttk.Entry(frame_liters)
entry_liters.grid(row=0, column=1, sticky=(tk.W, tk.E))
label_result_liters = ttk.Label(frame_liters, text="")
label_result_liters.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

frame_celsius = ttk.Frame(root, padding="10")
frame_celsius.grid(row=5, column=0, sticky=(tk.W, tk.E))
ttk.Label(frame_celsius, text="Celsius:").grid(row=0, column=0, sticky=tk.W)
entry_celsius = ttk.Entry(frame_celsius)
entry_celsius.grid(row=0, column=1, sticky=(tk.W, tk.E))
label_result_celsius = ttk.Label(frame_celsius, text="")
label_result_celsius.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Convert and Clear Buttons
buttons_frame = ttk.Frame(root, padding="10")
buttons_frame.grid(row=6, column=0, sticky=(tk.W, tk.E))
convert_button = ttk.Button(buttons_frame, text="Convert", command=convert)
convert_button.grid(row=0, column=0, padx=5)
clear_button = ttk.Button(buttons_frame, text="Clear", command=clear)
clear_button.grid(row=0, column=1, padx=5)

# Run the application
root.mainloop()
