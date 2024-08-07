import tkinter as tk
from tkinter import ttk

# Conversion functions
def km_to_miles(km):
    return km * 0.621371

def meters_to_feet(meters):
    return meters * 3.28084

def cm_to_inches(cm):
    return cm * 0.393701

def kg_to_pounds(kg):
    return kg * 2.20462

def liters_to_gallons(liters):
    return liters * 0.264172

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert():
    try:
        km = float(entry_km.get())
        miles = km_to_miles(km)
        label_result_km.config(text=f"{km} km = {miles:.2f} miles")
    except ValueError:
        label_result_km.config(text="Invalid input for km to miles")

    try:
        meters = float(entry_meters.get())
        feet = meters_to_feet(meters)
        label_result_meters.config(text=f"{meters} meters = {feet:.2f} feet")
    except ValueError:
        label_result_meters.config(text="Invalid input for meters to feet")

    try:
        cm = float(entry_cm.get())
        inches = cm_to_inches(cm)
        label_result_cm.config(text=f"{cm} cm = {inches:.2f} inches")
    except ValueError:
        label_result_cm.config(text="Invalid input for cm to inches")

    try:
        kg = float(entry_kg.get())
        pounds = kg_to_pounds(kg)
        label_result_kg.config(text=f"{kg} kg = {pounds:.2f} pounds")
    except ValueError:
        label_result_kg.config(text="Invalid input for kg to pounds")

    try:
        liters = float(entry_liters.get())
        gallons = liters_to_gallons(liters)
        label_result_liters.config(text=f"{liters} liters = {gallons:.2f} gallons")
    except ValueError:
        label_result_liters.config(text="Invalid input for liters to gallons")

    try:
        celsius = float(entry_celsius.get())
        fahrenheit = celsius_to_fahrenheit(celsius)
        label_result_celsius.config(text=f"{celsius} °C = {fahrenheit:.2f} °F")
    except ValueError:
        label_result_celsius.config(text="Invalid input for °C to °F")

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
