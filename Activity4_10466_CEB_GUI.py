import tkinter as tk

def show_details():
    details_window = tk.Toplevel()
    details_window.title("Submitted Details")
    details_window.geometry("400x300")
    details_window.config(bg="plum")

    details_label = tk.Label(details_window, text="Submitted Details", font=("Arial", 16), bg="plum")
    details_label.pack(pady=10)

    details_text = f"Username: {entry_username.get()}\n" \
                   f"Email: {entry_email.get()}\n" \
                   f"Gender: {gender_var.get()}\n" \
                   f"Country: {country_var.get()}"
    details_display = tk.Label(details_window, text=details_text, font=("", 12), bg="plum")
    details_display.pack(pady=10)

    close_button = tk.Button(details_window, text="Close", command=details_window.destroy, font=("Arial", 14))
    close_button.pack(pady=10)

root = tk.Tk()
root.title("Registration Form")

root.geometry("500x450")
root.config(bg="mediumpurple")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

label_username = tk.Label(root, text="Username:", font=("Arial", 14), bg="mediumpurple")
label_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_username = tk.Entry(root, font=("Arial", 14))
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:", font=("Arial", 14), bg="mediumpurple")
label_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_email = tk.Entry(root, font=("Arial", 14))
entry_email.grid(row=1, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:", font=("Arial", 14), bg="mediumpurple")
label_password.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_password = tk.Entry(root, show="*", font=("Arial", 14))
entry_password.grid(row=2, column=1, padx=10, pady=10)

label_gender = tk.Label(root, text="Gender:", font=("Arial", 14), bg="mediumpurple")
label_gender.grid(row=3, column=0, padx=10, pady=10, sticky="e")

gender_var = tk.StringVar()
radio_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", font=("Arial", 14), bg="mediumpurple")
radio_male.grid(row=3, column=1, padx=70, pady=5, sticky="w")
radio_male.deselect()

radio_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", font=("Arial", 14), bg="mediumpurple")
radio_female.grid(row=3, column=1, padx=150, pady=5, sticky="w")

label_country = tk.Label(root, text="Country:", font=("Arial", 14), bg="mediumpurple")
label_country.grid(row=4, column=0, padx=10, pady=10, sticky="e")

countries = ["Select Country", "USA", "India", "Canada", "UK", "Australia", "Germany", "France"]
country_var = tk.StringVar()
country_var.set(countries[0])

country_dropdown = tk.OptionMenu(root, country_var, *countries)
country_dropdown.config(font=("Arial", 14))
country_dropdown.grid(row=4, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=show_details)
submit_button.grid(row=5, column=0, columnspan=3, pady=20)

root.mainloop()

