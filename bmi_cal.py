import tkinter as tk
from tkinter import messagebox

# Function
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # cm ko meter me convert
        
        if height <= 0 or weight <= 0:
            messagebox.showerror("Error", "Please enter valid values")
            return
            
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        
        # Result ke hisab se category
        if bmi < 18.5:
            category = "Underweight 😔"
            color = "#FFA726"
        elif bmi < 24.9:
            category = "Normal ✅"
            color = "#66BB6A"
        elif bmi < 29.9:
            category = "Overweight ⚠️"
            color = "#FFA726"
        else:
            category = "Obese ❌"
            color = "#EF5350"
        
        result_label.config(text=f"Your BMI: {bmi}\nCategory: {category}", fg=color)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only")

# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x350")
root.config(bg="#E8F5E9")

# Heading
tk.Label(root, text="BMI CALCULATOR", font=("Arial", 16, "bold"), bg="#E8F5E9", fg="#2E7D32").pack(pady=15)

# Weight
tk.Label(root, text="Enter Weight (kg):", font=("Arial", 12), bg="#E8F5E9").pack()
weight_entry = tk.Entry(root, font=("Arial", 12), width=20)
weight_entry.pack(pady=5)

# Height  
tk.Label(root, text="Enter Height (cm):", font=("Arial", 12), bg="#E8F5E9").pack()
height_entry = tk.Entry(root, font=("Arial", 12), width=20)
height_entry.pack(pady=5)

# Button
tk.Button(root, text="Calculate BMI", font=("Arial", 12, "bold"), 
          command=calculate_bmi, bg="#4CAF50", fg="white", width=20).pack(pady=20)

# Result
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#E8F5E9")
result_label.pack(pady=10)

# Info
tk.Label(root, text="BMI Formula: weight / height²", font=("Arial", 10), bg="#E8F5E9", fg="gray").pack()

root.mainloop()