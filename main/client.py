import socket


# Function to connect to the server and send student data
def connect_to_server(student_name, student_id):
    # Server information (same as the server setup)
    host = '127.0.0.1'  # Localhost
    port = 12345  # Port number the server is listening on

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))

        # Prepare the data to send to the server
        student_data = f"{student_name},{student_id}"

        # Send the student data to the server
        client_socket.send(student_data.encode())

        # Receive the response from the server
        response = client_socket.recv(1024).decode()

        # Display the response from the server (login and password)
        print("Server Response:", response)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the client socket connection
        client_socket.close()


# Main function to take student input and connect to the server
def main():
    # Get student name and ID from the user
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    # Connect to the server and send data
    connect_to_server(student_name, student_id)


if __name__ == "__main__":
    main()
