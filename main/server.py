import socket
import random
import string


# Function to generate a random password
def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# Main server function
def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server will run on localhost and port 12345
    host = '127.0.0.1'  # Localhost (you can also use '0.0.0.0' for all available interfaces)
    port = 12345  # Port to listen on

    # Bind the server to the IP address and port
    server_socket.bind((host, port))

    # Start listening for incoming connections (max 5 clients in the waiting queue)
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")

    while True:
        # Accept new client connections
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        try:
            # Receive data from the client (maximum of 1024 bytes)
            student_data = client_socket.recv(1024).decode()

            if student_data:
                # Split the student data (name, ID) based on a comma
                student_name, student_id = student_data.split(',')

                # Generate the login name by combining student name and ID
                login_name = f"{student_name}@{student_id}"

                # Generate a random password for the student
                password = generate_password()

                # Send back the login name and password to the client
                response = f"Login Name: {login_name}, Password: {password}"
                client_socket.send(response.encode())
            else:
                client_socket.send("Invalid input".encode())

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Close the client connection
            client_socket.close()


if __name__ == "__main__":
    start_server()
