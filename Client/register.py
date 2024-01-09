import customtkinter, socket, main
from tkinter import messagebox

def login_operation():
    host_addr, host_port = link_entry.get().split(':')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host_addr, int(host_port)))
    username = username_entry.get()
    password = password_entry.get()
    try:
        login_message = f"LOGIN:{username}:{password}"
        client_socket.send(login_message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')

        if response == "LOGIN_SUCCESS":
            print("Login successful!")
            client_socket.close()
            main.open_chat_window(app, username, host_addr, host_port)
        else:
            messagebox.showinfo("Signup Error", "this user does not exist")
    except:
        print("server is shutdown")
    client_socket.close()

def signup_operation():
    host_addr, host_port = link_entry.get().split(':')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host_addr, int(host_port)))
    username = username_entry.get()
    password = password_entry.get()
    try:
        signup_message = f"SIGNUP:{username}:{password}"
        client_socket.send(signup_message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')

        if response == "SIGNUP_SUCCESS":
            print("Signup successful!")
            client_socket.close()
            main.open_chat_window(app, username, host_addr, host_port)
        elif response == "SIGNUP_FAILURE":
            print("Signup failed: Account already exists.")
            messagebox.showinfo("Signup Error", "This account already exists.")
        else:
            print("Unexpected response from the server during signup.")
            messagebox.showinfo("Signup Error", "Unexpected response from the server.")
    except Exception as e:
        print(f"Error during signup: {e}")
        messagebox.showinfo("Signup Error", "Failed to connect to the server.")
    client_socket.close()

app = customtkinter.CTk()
app.title("Register")
app.resizable(width=False, height=False)
app.geometry("500x500")
customtkinter.set_appearance_mode("dark")

customtkinter.CTkLabel(app, text="Registration", fg_color="transparent", font=('', 40)).place(relx= 0.3, rely= 0.1)

username_entry = customtkinter.CTkEntry(master=app, width= 200, placeholder_text="Username")
username_entry.place(relx= 0.5, rely=0.4, anchor= customtkinter.CENTER)

password_entry = customtkinter.CTkEntry(master=app, width= 200, show= '*', placeholder_text="password")
password_entry.place(relx= 0.5, rely= 0.5, anchor= customtkinter.CENTER)

link_entry = customtkinter.CTkEntry(master=app, width= 200, placeholder_text="link")
link_entry.place(relx= 0.5, rely= 0.6, anchor= customtkinter.CENTER)

btn_login = customtkinter.CTkButton(master=app, width= 85, text="Login", command= login_operation)
btn_login.place(relx= 0.6, rely= 0.7, anchor= customtkinter.CENTER)

btn_signup = customtkinter.CTkButton(master=app, width= 85, text="Sign up", command= signup_operation)
btn_signup.place(relx= 0.4, rely= 0.7, anchor= customtkinter.CENTER)

app.mainloop()
