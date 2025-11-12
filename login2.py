import os
import customtkinter as tk
import tkinter.messagebox as msg

# === App setup ===
tk.set_appearance_mode("System")
tk.set_default_color_theme("blue")

window1 = tk.CTk()
window1.geometry("400x400")
window1.title("Login System")

# === File handling setup ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # current folder
DATA_FILE = os.path.join(BASE_DIR, "userlogin2.txt")

# Create the file if it doesn’t exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        f.write("")  # empty file


# === Helper Functions ===
def toggle_password():
    entry2.configure(show="" if show_pass_var.get() else "*")


def login():
    print("Checking credentials...")


def checkuser():
    username = entry1.get().strip()
    password = entry2.get().strip()

    window4 = tk.CTkToplevel(window1)
    window4.geometry("300x300")
    window4.title("Message")

    frame_msg = tk.CTkFrame(master=window4)
    frame_msg.pack(padx=20, pady=20, fill="both", expand=True)

    try:
        found = False
        with open(DATA_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 2:
                    continue  # skip bad lines

                stored_user, stored_pw = parts
                if username == stored_user:
                    found = True
                    if password == stored_pw:
                        msg_label = tk.CTkLabel(
                            master=frame_msg, text="✅ Logged in Successfully", font=("Times New Roman", 18))
                    else:
                        msg_label = tk.CTkLabel(
                            master=frame_msg, text="❌ Invalid Password", font=("Times New Roman", 18))
                    msg_label.pack(padx=10, pady=12)
                    break

        if not found:
            msg_label = tk.CTkLabel(
                master=frame_msg, text="⚠️ No user found.\nPlease register first.", font=("Times New Roman", 18))
            msg_label.pack(padx=10, pady=12)

    except Exception as e:
        msg_label = tk.CTkLabel(
            master=frame_msg, text=f"Error: {e}", font=("Times New Roman", 16))
        msg_label.pack(padx=10, pady=12)

    tk.CTkButton(master=frame_msg, text="OK",
                 command=window4.destroy).pack(padx=10, pady=10)


def create_account():
    window2 = tk.CTkToplevel(window1)
    window2.geometry("400x400")
    window2.title("Create Account")

    frame = tk.CTkFrame(master=window2)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    tk.CTkLabel(master=frame, text="Register New User", font=(
        "Times New Roman", 18)).pack(padx=10, pady=12)

    new_user = tk.CTkEntry(master=frame, placeholder_text="Username")
    new_user.pack(padx=10, pady=5)
    new_pass = tk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    new_pass.pack(padx=10, pady=5)

    def save_user():
        user = new_user.get().strip()
        pw = new_pass.get().strip()
        if not user or not pw:
            msg.showerror("Error", "Username and password cannot be empty!")
            return
        with open(DATA_FILE, "a") as file:
            file.write(f"{user},{pw}\n")
        msg.showinfo("Success", "Registration successful!")
        window2.destroy()

    tk.CTkButton(master=frame, text="Register",
                 command=save_user).pack(padx=10, pady=15)


# === UI Setup ===
frame = tk.CTkFrame(master=window1)
frame.pack(padx=50, pady=20, fill="both", expand=True)

tk.CTkLabel(master=frame, text="Welcome, Zenith!", font=(
    "Times New Roman", 21)).pack(padx=10, pady=12)
tk.CTkLabel(master=frame, text="Login to Continue").pack(padx=10, pady=12)

entry1 = tk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(padx=10, pady=5)
entry2 = tk.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(padx=10, pady=5)

show_pass_var = tk.IntVar(value=0)
tk.CTkCheckBox(master=frame, text="Show Password", variable=show_pass_var,
               command=toggle_password).pack(padx=10, pady=5)

tk.CTkButton(master=frame, text="Continue", command=lambda: [
             login(), checkuser()]).pack(padx=10, pady=10)
tk.CTkButton(master=frame, text="Create Account", fg_color="transparent",
             hover_color="dark blue", command=create_account).pack(padx=10, pady=5)

window1.mainloop()
