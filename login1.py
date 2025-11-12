import os
import tkinter.messagebox as msg
import customtkinter as tk
import csv
tk.set_appearance_mode("SYSTEM")
tk.set_default_color_theme("blue")

window1 = tk.CTk()
window1.geometry("400x400")
window1.title("Login System")

base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base_dir, "userlogin2.csv")


if not os.path.exists(filepath):
    with open(filepath, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["username", "password"])


def login():
    print(" Logged in Successfully")


def toggle_password():
    if show_pass_var.get() == 1:
        entry2.configure(show="")
    else:
        entry2.configure(show="*")


def checkuser():
    username = entry1.get()
    password = entry2.get()

    try:
        found = False

        with open(filepath, "r", newline='') as file:
            # print("file opened")
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 2:
                    continue
                stored_user, stored_pw = row
            # print(f"{stored_user},{stored_pw}")
                if username == stored_user:
                    found = True
                    if password == stored_pw:
                        window4 = tk.CTkToplevel(window1)
                        window4.geometry("300x300")
                        window4.title("Warning!")

                        lnewframe2 = tk.CTkFrame(master=window4)
                        lnewframe2.pack(padx=20, pady=20,
                                        fill="both", expand=True)

                        lnewlabel1 = tk.CTkLabel(
                            master=lnewframe2, text="Logged in Successfully", font=("Times New Roman", 18))
                        lnewlabel1.pack(padx=10, pady=12, anchor="s")

                        newbutton7 = tk.CTkButton(
                            master=lnewframe2, text="OK", command=window4.destroy)
                        newbutton7.pack(padx=10, pady=10, anchor="s")
                    else:

                        msg.showwarning("Error", "Invalid Password")
                    break
        if not found:
            print("NOT FOUND")
            msg.showwarning("Error", "No user found.\nPlease register first.")

    except FileNotFoundError:
        msg.showwarning("Error", "File not found!")


frame = tk.CTkFrame(master=window1)
frame.pack(padx=50, pady=20, fill="both", expand=True)

label1 = tk.CTkLabel(
    master=frame, text="Welcome, Dear! ", font=("Times New Roman", 21), )
label1.pack(padx=10, pady=12, anchor="s")

label2 = tk.CTkLabel(master=frame, text="Login to Continue",)
label2.pack(padx=10, pady=12, anchor="s")

entry1 = tk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(padx=10, pady=5, anchor="s")

entry2 = tk.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(padx=10, pady=5, anchor="s", )


# with open("C:\\Users\\SANJAYA\\python\\login program\\userlogin.txt", "r") as file:


show_pass_var = tk.IntVar(value=0)
checkbox1 = tk.CTkCheckBox(
    master=frame, text="Show Password", variable=show_pass_var, command=toggle_password)
checkbox1.pack(padx=10, pady=5)


def close_popup():
    window1.destroy()


button1 = tk.CTkButton(master=frame, text="Continue",
                       command=lambda: [login(), checkuser()])
button1.pack(padx=10, pady=10, anchor="s")


def create_account():
    print(" Registration panel opened.")
    window2 = tk.CTkToplevel(window1)
    window2.geometry("500x500")
    window2.title("Registration ")

    def save_user():
        username = newentry3.get().strip()
        password = newentry4.get().strip()

        filepath = os.path.join(base_dir, "userlogin2.csv")

        if os.path.exists(filepath):

            with open(filepath, "r", newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) != 2:
                        continue
                    stored_user, stored_pw = row
                    if username == stored_user:
                        msg.showwarning(
                            "Error", "Username already exists:\nTry another username")
                        return

        if username == "" or password == "":
            msg.showwarning("Error", "Please fill username and password")
            return

        with open(filepath, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
            success()

    # print("Saving file to:", os.getcwd())

    def register():
        print(" Registered Successfully")

    newframe = tk.CTkFrame(master=window2)
    newframe.pack(padx=20, pady=20, fill="both", expand=True)

    newlabel1 = tk.CTkLabel(
        master=newframe, text="Please fill all the fields, ", font=("Times New Roman", 16), )
    newlabel1.pack(padx=10, pady=12, anchor="w")

    newlabel2 = tk.CTkLabel(master=newframe, text="First name", )
    newlabel2.pack(padx=10, pady=12, anchor="w")

    newentry1 = tk.CTkEntry(
        master=newframe, placeholder_text="Firstname", font=("Times New Roman", 16), width=200)
    newentry1.pack(padx=10, pady=5, anchor="w")

    newlabel3 = tk.CTkLabel(master=newframe, text="Last name",)
    newlabel3.pack(padx=10, pady=12, anchor="w")

    newentry2 = tk.CTkEntry(master=newframe, placeholder_text="Lastname", font=(
        "Times New Roman", 16), width=200)
    newentry2.pack(padx=10, pady=5, anchor="w")

    newlabel4 = tk.CTkLabel(master=newframe, text="Username",)
    newlabel4.pack(padx=10, pady=12, anchor="w")

    newentry3 = tk.CTkEntry(master=newframe, placeholder_text="Username", font=(
        "Times New Roman", 16), width=200)
    newentry3.pack(padx=10, pady=5, anchor="w")

    newlabel5 = tk.CTkLabel(master=newframe, text="Password",)
    newlabel5.pack(padx=10, pady=12, anchor="w")

    newentry4 = tk.CTkEntry(master=newframe, placeholder_text="Password", font=(
        "Times New Roman", 16), width=200)
    newentry4.pack(padx=10, pady=5, anchor="w")

    newbutton1 = tk.CTkButton(master=newframe, text="Register",
                              command=lambda: [save_user(), register(),])
    newbutton1.pack(padx=10, pady=10, anchor="s")

    def success():
        window3 = tk.CTkToplevel(window2)
        window3.geometry("300x300")
        window3.title("Warning!")

        window3.lift()
        window3.attributes("-topmost", True)
        window3.after_idle(window3.attributes, "-topmost", False)

        newframe2 = tk.CTkFrame(master=window3)
        newframe2.pack(padx=20, pady=20, fill="both", expand=True)

        newlabel1 = tk.CTkLabel(
            master=newframe2, text="Registration Successful", font=("Times New Roman", 18))
        newlabel1.pack(padx=10, pady=12, anchor="s")

        def close():
            window3.destroy()
            window2.destroy()

        newbutton7 = tk.CTkButton(master=newframe2, text="OK", command=close)

        newbutton7.pack(padx=10, pady=10, anchor="s")


newbutton2 = tk.CTkButton(master=frame, text="Create Account", fg_color="transparent",
                          font=("Times New Roman", 13), hover_color="dark blue", border_width=0, command=create_account)
newbutton2.pack(padx=10, pady=10, anchor="s")

window1.mainloop()
