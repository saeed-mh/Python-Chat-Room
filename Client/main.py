import customtkinter, socket, threading, config

def open_chat_window(root, name, host_addr, host_port):
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host_addr, int(host_port)))

    def send_to_server(message):
        try:
            client_socket.send(f"{name}: {message}".encode('utf-8'))
        except:
            print("Error in sending message")

    def send_message():
        message = input_message.get()
        if message:
            input_message.delete(0, 'end')
            send_to_server(message)

    def listen_for_messages():
        counter_line = 0
        while True:
            try:
                message = client_socket.recv(config.BUFFER_SIZE).decode()
                if message.startswith(name + ": "):
                    message = message.replace(name, "you")
                    _text_color = "green"
                else:
                    _text_color = "white"
                    
                message = customtkinter.CTkLabel(master=scrollable_frame, text_color= _text_color, text=f"{message}")
                message.grid(row=counter_line, column=0, padx=5, sticky = "w", pady=(0, 1))
                counter_line += 1

            except Exception as e:
                print("Error while receiving message:", e)
                break

    def on_exit():
        root.destroy()

    root.withdraw()
    app = customtkinter.CTkToplevel(root)
    app.geometry("600x600")
    app.resizable(width=True, height=True)
    app.title(name)

    input_message = customtkinter.CTkEntry(app, width = 480, placeholder_text = "Message")
    input_message.place(relx = 0.42, rely = 0.95, anchor = customtkinter.CENTER)

    btn_send = customtkinter.CTkButton(app, width=70, text="Send", corner_radius=50, command=send_message)
    btn_send.place(relx = 0.91, rely = 0.95, anchor= customtkinter.CENTER)

    scrollable_frame = customtkinter.CTkScrollableFrame(app, width= 550, height=525)
    scrollable_frame.place(relx = 0.5, rely = 0.46, anchor= customtkinter.CENTER)

    app.protocol("WM_DELETE_WINDOW", on_exit)

    listen_thread = threading.Thread(target=listen_for_messages)
    listen_thread.daemon = True
    listen_thread.start()


