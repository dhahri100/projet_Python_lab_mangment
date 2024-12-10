import random
import socket
import string
import threading
import sqlite3
import bcrypt

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345


# Hash the password before saving
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# Verify provided password with stored hashed password
def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode(), stored_password.encode())

# Save credentials to the database
def save_to_db(student_name, student_id, login_name, password):
    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()

    try:
        hashed_password = hash_password(password)
        cursor.execute("INSERT INTO clients (student_name, student_id, login_name, password) VALUES (?, ?, ?, ?)",
                       (student_name, student_id, login_name, hashed_password))
        conn.commit()
        print(f"Saved {login_name} to the database.")
        return f"Registration successful. Login Name: {login_name}, Password: {password}"
    except sqlite3.IntegrityError:
        return f"Credentials for {login_name} already exist."
    finally:
        conn.close()

# Authenticate an existing user
def authenticate_user(login_name, provided_password):
    conn = sqlite3.connect("clients.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM clients WHERE login_name = ?", (login_name,))
    result = cursor.fetchone()
    conn.close()

    if result and verify_password(result[0], provided_password):
        return "Authentication successful."
    else:
        return "Authentication failed."

# Handle client connections
def handle_client(client_socket, client_address):
    print(f"Connection from {client_address} established.")
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            try:
                command, *args = data.split(',')

                if command == "register" and len(args) == 2:
                    student_name, student_id = args
                    login_name = f"{student_name}@{student_id}"
                    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                    response = save_to_db(student_name, student_id, login_name, password)

                elif command == "authenticate" and len(args) == 2:
                    login_name, password = args
                    response = authenticate_user(login_name, password)

                else:
                    response = "Invalid input. Use correct format."

                client_socket.send(response.encode())

            except ValueError:
                client_socket.send("Invalid input. Use correct format.".encode())

    except Exception as e:
        print(f"Error when handling client {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"Connection with {client_address} closed.")


# Start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


if __name__ == "__main__":
    start_server()
