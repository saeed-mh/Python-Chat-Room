# Chat Room Application - University Project

## Overview
Welcome to the Chat Room Application! This project is a Python-based chat room with a graphical user interface (GUI) built using the Custom Tkinter library. The application has been developed as part of a university project to demonstrate skills in socket programming, multi-threading, and database.

## Features
+ **Graphical User Interface (GUI)**: The application boasts a user-friendly GUI, powered by the Custom Tkinter library, providing an intuitive and visually appealing chat room experience.

+ **Socket Communication**: The application utilizes sockets for communication, allowing users to send and receive messages in real-time.

+ **Multi-User Support**: Threading is employed to handle multiple users simultaneously, ensuring efficient and responsive communication within the chat room.

+ **Database Integration**: The application leverages SQLAlchemy for seamless integration with a PostgreSQL database, providing a robust and persistent storage solution for user data.

+ **Password Security**: User passwords are securely hashed using the bcrypt module in Python, ensuring a high level of security for user accounts.

## Getting Started
### Installation

1. Clone the repository to your local machine:
`
git clone https://github.com/saeed-mh/Python-Chat-Room.git
`
2. Install the required dependencies:
`
pip install -r requirements.txt
`
3. Set up the PostgreSQL database:
  + Update the database connection details in the server file.
4. Run the server:
`
python server.py
`
5. Now you can run the client:
`
python register.py
`
+ it should be like this:

  ![image](https://github.com/saeed-mh/Python-Chat-Room/assets/75900669/de7c6dff-0086-41af-9724-01fed8231297)


  ![image](https://github.com/saeed-mh/Python-Chat-Room/assets/75900669/f1763475-d791-44ab-bb0e-15933ce6d41b)


  ![image](https://github.com/saeed-mh/Python-Chat-Room/assets/75900669/9e3059a2-6aad-4849-92e6-cb2be1c0f657)

  

## Configuration
The application's configuration is stored in the config.py file. Update this file to customize settings such as the default port, IP address, etc.
+ **Default Port**: The default port for communication is set to 65432. Users can easily customize this port based on their preferences.

