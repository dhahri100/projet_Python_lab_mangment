import socket

# Server information (same as the server setup)
HOST = '127.0.0.1'  # Localhost
PORT = 12345  # Port number the server is listening on


# Function to connect to the server and send data
def connect_to_server(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        client_socket.send(data.encode())
        response = client_socket.recv(1024).decode()
        print("Server Response:", response)
        return response

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()


# Register a new student
def register():
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    data = f"register,{student_name},{student_id}"
    connect_to_server(data)


# Authenticate an existing student
def authenticate():
    login_name = input("Enter your login name: ")
    password = input("Enter your password: ")
    data = f"authenticate,{login_name},{password}"
    response = connect_to_server(data)

    if "Authentication successful" in response:
        print("Access granted. Proceeding with the application...")
        # Add further client-side features here
    else:
        print("Authentication failed. Please try again.")


# Main function to manage client operations
def main():
    while True:
        print("\n1. Register")
        print("2. Authenticate")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            authenticate()
        elif choice == '3':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please select again.")


if __name__ == "__main__":
    main()
