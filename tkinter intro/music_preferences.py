import tkinter as tk


default_font = ("Arial", 20)

window = tk.Tk()
window.title(" My Music Preferences")
window.geometry("600x600")

label = tk.Label(window, 
                 text="Welcome to My Music Preferences!",
                 fg="purple",
                 font=default_font,).pack()

label = tk.Label(window, 
                 text="Who is your favorite atist or band?",
                 fg="black",
                 bd=20,
                 font=("arial", 17)).pack()

fav_band = tk.Entry(window, 
                 font=default_font,
                 width=18).pack()
fav_band.insert(0, "Band Here")

label = tk.Label(window, 
                 text="Select your favorite music genres:",
                 fg="black",
                 bd=20,
                 font=("arial", 17)).pack()

check_rock = tk.IntVar()
checkbox_rock = tk.Checkbutton(
    window, text="Rock", variable=check_rock).pack(anchor="w")

check_pop = tk.IntVar()
checkbox_pop = tk.Checkbutton(
    window, text="Pop", variable=check_pop).pack(anchor="w")

check_jazz = tk.IntVar()
checkbox_jazz = tk.Checkbutton(
    window, text="Jazz", variable=check_jazz).pack(anchor="w")

label = tk.Label(window, 
                 text="Choose your preferred listening method:",
                 fg="black",
                 bd=20,
                 font=("arial", 17)).pack()

tk.Radiobutton(window, font=("arial", 10), text="Streaming", 
               value="Mr. James Klins").pack(anchor="w")
tk.Radiobutton(window, font=("arial", 10), text="CDs", 
               value="James Clark").pack(anchor="w")
tk.Radiobutton(window, font=("arial", 10), text="Vinyl", 
               value="Coby Hughes").pack(anchor="w")

def get_data():
    window = tk.Tk()
    window.title("Music Preferences")
    window.geometry("300x150")
    band = fav_band.get()
    label = tk.Label(window, 
                 text=band,
                 fg="black",
                 font=("Arial", 5))
    label.pack()
    window.mainlooop()

tk.Button(window, text="Submit", bg="blue", fg="white", command=get_data).pack()


window.mainloop()