import networkx as nx 
import socket
import time

def receive_message_from_server(host, port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        # Send a "hello" message
        message = "Hello, server!"
        client_socket.sendall(message.encode())
        print(f"Sent message: {message}")

        # Receive a response from the server
        response = client_socket.recv(1024).decode()
        print(f"Received response: {response}")

    except ConnectionRefusedError:
        print(f"Connection refused. Ensure the server is running on {host}:{port}.")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the socket
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    host = "192.168.50.239"  # Use the same host as the server
    port = 3030

    while True:
        receive_message_from_server(host, port)
        time.sleep(5)  # Send the message every 5 seconds


